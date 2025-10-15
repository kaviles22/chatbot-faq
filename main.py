from chain import get_banking_agent
import sys

def main():
    print("🏦 Bienvenido al Asistente Bancario Virtual del Banco de Guayaquil")
    print("=" * 60)
    print("Puedo ayudarte con:")
    print("• Consulta de saldo de cuenta")
    print("• Información de tarjeta de crédito")
    print("• Estado de créditos bancarios") 
    print("• Descuentos y ofertas disponibles")
    print("• Ubicación de sucursales cercanas")
    print("• Información de pólizas de seguros")
    print("• Preguntas frecuentes")
    print("=" * 60)
    print('Escribe "salir" para terminar la conversación')
    print()

    # Inicializar el agente
    try:
        agent = get_banking_agent()
        print("✅ Agente bancario listo para ayudarte\n")
    except Exception as e:
        print(f"❌ Error al inicializar el agente: {e}")
        print("Verifica que tengas configurada tu API key de OpenAI")
        sys.exit(1)

    while True:
        try:
            query = input('💬 ¿En qué puedo ayudarte? ')
            
            if query.lower() in ["salir", "exit", "quit"]:
                print('👋 ¡Gracias por usar nuestro servicio! Que tengas un buen día.')
                sys.exit()
            
            if not query.strip():
                continue
                
            print("\n🤖 Procesando tu consulta...")
            response = agent.invoke({"input": query})
            
            print(f"\n📝 Respuesta: {response['output']}")
            print("-" * 60)
            
        except KeyboardInterrupt:
            print('\n👋 ¡Hasta luego!')
            sys.exit()
        except Exception as e:
            print(f"\n❌ Error al procesar tu consulta: {e}")
            print("Por favor, intenta de nuevo.")
            print("-" * 60)

if __name__ == "__main__":
    main()