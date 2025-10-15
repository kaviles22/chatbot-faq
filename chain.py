import os
from langchain.document_loaders.csv_loader import CSVLoader
from langchain.memory import ConversationBufferMemory
from langchain_openai import OpenAIEmbeddings
from langchain_community.vectorstores import FAISS
from langchain_openai import ChatOpenAI
from langchain.agents import AgentExecutor, create_openai_tools_agent
from langchain.tools.retriever import create_retriever_tool
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from banking_tools import get_banking_tools
from dotenv import load_dotenv

load_dotenv()

def get_banking_agent():
    # Cargar documentos FAQ para el retriever
    if os.environ.get('RAG_FILE') and os.path.exists(os.environ['RAG_FILE']):
        loader = CSVLoader(file_path=os.environ['RAG_FILE'])
        documents = loader.load()
        vectorstore = FAISS.from_documents(documents, OpenAIEmbeddings())
        
        # Crear tool de retrieval para FAQs
        retriever_tool = create_retriever_tool(
            vectorstore.as_retriever(),
            "faq_search",
            "Busca información en las preguntas frecuentes del banco. Útil para responder preguntas generales sobre servicios bancarios."
        )
        
        # Combinar herramientas bancarias con el retriever
        tools = get_banking_tools() + [retriever_tool]
    else:
        # Solo usar herramientas bancarias si no hay archivo FAQ
        tools = get_banking_tools()
    
    # Configurar el LLM
    llm = ChatOpenAI(model="gpt-3.5-turbo", temperature=0.3)
    
    # Crear el prompt del agente
    prompt = ChatPromptTemplate.from_messages([
        ("system", """Eres un asistente bancario virtual del Banco de Guayaquil. Ayudas a los clientes con sus consultas bancarias.

HERRAMIENTAS DISPONIBLES:
- saldo_cuenta: Consultar saldo actual
- info_tarjeta_credito: Información de tarjeta de crédito (montos, fechas)
- credito_bancario: Información de créditos bancarios
- info_polizas: Información de pólizas de seguros del cliente
- faq_search: Preguntas frecuentes (si disponible)

REGLAS IMPORTANTES:
1. Para consultas simples (saldo, tarjeta, etc.), usa EXACTAMENTE UNA herramienta
2. Para saludos ("hola", "buenas", etc.), responde directamente SIN usar herramientas
3. Si usas una herramienta, presenta la información de forma clara
4. Si no tienes la herramienta apropiada, explica qué puedes hacer
5. Mantén un tono profesional y amable
6. Recuerda las conversaciones anteriores para dar un mejor servicio

EJEMPLOS:
- "¿mi saldo?" → Usar saldo_cuenta
- "hola" → Responder sin herramientas: "¡Hola! Soy tu asistente bancario..."
- "tarjeta" → Usar info_tarjeta_credito
- "crédito" → Usar credito_bancario
- "pólizas" o "seguros" → Usar info_polizas"""),
        MessagesPlaceholder(variable_name="chat_history", optional=True),
        ("user", "{input}"),
        MessagesPlaceholder(variable_name="agent_scratchpad")
    ])
    
    # Crear el agente
    agent = create_openai_tools_agent(llm, tools, prompt)
    
    # Configurar memoria conversacional
    memory = ConversationBufferMemory(
        memory_key="chat_history",
        return_messages=True,
        output_key="output"
    )
    
    # Crear el executor del agente con memoria
    agent_executor = AgentExecutor(
        agent=agent, 
        tools=tools,
        memory=memory,
        verbose=os.environ.get('AGENT_DEBUG_MODE'),  # Para debug
        handle_parsing_errors=True,
        max_iterations=4,  # Aumentar un poco por la memoria
        early_stopping_method="generate",
        return_intermediate_steps=False,
        max_execution_time=30  # Timeout de 30 segundos
    )
    
    return agent_executor