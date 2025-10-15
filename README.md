# Agente Bancario Virtual

Un agente inteligente que puede ayudar a los clientes con consultas bancarias específicas usando herramientas especializadas.

## Características

El agente puede manejar las siguientes consultas:

### Herramientas Bancarias Disponibles
- **Saldo de Cuenta**: Consulta el saldo actual de la cuenta
- **Información de Tarjeta de Crédito**: 
  - Mínimo a pagar
  - Total a pagar  
  - Fecha próxima de pago
  - Fecha de corte
- **Crédito Bancario**:
  - Valor total del crédito
  - Valor ya pagado
  - Fecha próxima de pago
- **Descuentos**: Descuentos disponibles esta semana con la tarjeta de crédito
- **Sucursales Cercanas**: Localización de la sucursal bancaria más cercana
- **Pólizas de Seguros**: Información completa de pólizas activas:
  - Seguro de vida, vehicular y hogar
  - Número de póliza y cobertura
  - Prima mensual y fecha de vencimiento
- **FAQs**: Búsqueda en preguntas frecuentes (si hay archivo CSV configurado)
- **Memoria Conversacional**: El agente recuerda interacciones anteriores para mejor contexto

## Requisitos

- requirements.txt
- Archivo CSV con FAQs (opcional)

## Instalación

1. **Instalar dependencias**:
```bash
pip install -r requirements.txt
```

2. **Configurar variables de entorno**:

Editar .env con tu API key de OpenAI


3. **Configurar el archivo .env**:
```
OPENAI_API_KEY=tu_api_key_de_openai
RAG_FILE=FAQ.csv  # Opcional
AGENT_DEBUG_MODE=false  # true para ver logs detallados del agente
```

## Uso

### Ejecutar el Agente Interactivo
```bash
python agent.py
```

### Ejemplos de Consultas

- "¿Cuál es mi saldo actual?"
- "Información de mi tarjeta de crédito"
- "¿Cuándo vence mi próximo pago del crédito?"
- "¿Qué descuentos tengo disponibles?"
- "¿Dónde está la sucursal más cercana?"
- "¿Cuáles son mis pólizas de seguros?"
- "Información de mis seguros activos"
- "¿Cómo puedo cambiar mi PIN?" (busca en FAQs)

### Ejemplos de Conversación con Memoria

```
Usuario: "¿Cuál es mi saldo?"
Agente: "Su saldo actual es de $2,450.30 USD"

Usuario: "¿Y mi tarjeta?"
Agente: [Recuerda consulta anterior] "Información de su tarjeta de crédito: ..."

Usuario: "¿Tengo descuentos disponibles?"
Agente: "Sí, tiene los siguientes descuentos esta semana: ..."
```

## Arquitectura

```
├── agent.py              # Interfaz de línea de comandos
├── chain.py            # Configuración del agente principal
├── banking_tools.py    # Herramientas bancarias especializadas
├── FAQ.csv            # Archivo de preguntas frecuentes (opcional)
├── requirements.txt   # Dependencias
└── .env              # Variables de entorno
```

## Datos Simulados

**Nota**: Las herramientas actuales devuelven datos simulados para demostración. En producción, estas deberían conectarse a:
- APIs bancarias reales
- Bases de datos de clientes
- Sistemas core bancarios
- Servicios de geolocalización para sucursales
- Sistemas de seguros y pólizas

## Características Avanzadas

### Memoria Conversacional
- El agente mantiene el contexto de la conversación
- Puede referenciar consultas anteriores
- Proporciona una experiencia más natural y personalizada

### Manejo de Errores
- Timeout de 30 segundos por consulta
- Máximo 4 iteraciones por consulta para evitar bucles
- Manejo robusto de errores de parsing

### Debug y Monitoreo
- Modo debug configurable via `AGENT_DEBUG_MODE`
- Logs detallados para troubleshooting
- Manejo de errores graceful

## Herramientas Técnicas

| Nombre Técnico | Descripción | Ejemplo de Uso |
|---|---|---|
| `saldo_cuenta` | Consulta saldo actual | "¿Cuál es mi saldo?" |
| `info_tarjeta_credito` | Información de tarjeta de crédito | "Info de mi tarjeta" |
| `credito_bancario` | Estado de créditos bancarios | "¿Cómo está mi préstamo?" |
| `descuentos` | Ofertas y descuentos disponibles | "¿Qué descuentos tengo?" |
| `sucursal_cercana` | Ubicación de sucursales | "¿Dónde hay una sucursal?" |
| `info_polizas` | Información de pólizas de seguros | "¿Cuáles son mis seguros?" |
| `faq_search` | Búsqueda en FAQs | "¿Cómo cambio mi PIN?" |