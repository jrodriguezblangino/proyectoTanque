from time import sleep
from datetime import datetime
from tanque import Tanque, Valvula, TipoValvula

def imprimir_estado(tanque, mensaje="Estado actual"):
    """Imprime el estado actual del tanque de forma formateada."""
    print("\n" + "="*50)
    print(f"📊 {mensaje} - {datetime.now().strftime('%H:%M:%S')}")
    print("="*50)
    
    nivel = tanque.calcularNivel()
    print(f"📏 Nivel actual: {nivel['metros']:.2f}m ({nivel['porcentaje']:.1f}%)")
    print(f"🌊 Volumen actual: {float(tanque.volumenActual):.2f}L")
    
    print("\n📈 Estado de válvulas:")
    for i, valvula in enumerate(tanque.valvulas, 1):
        tipo = "entrada ⬆️ " if valvula.tipo == TipoValvula.ENTRADA else "salida ⬇️ "
        estado = "ABIERTA" if valvula.caudalActual != 0 else "CERRADA"
        caudal = abs(float(valvula.caudalActual))
        print(f"  Válvula {i} ({tipo}): {estado} - Caudal: {caudal:.2f} L/s")
    print("-"*50)

def main():
    # Crear un tanque de 2m de diámetro y 3m de altura
    print("\n🏭 Creando sistema de tanque...")
    tanque = Tanque(diametro=2, altura=3)
    
    # Crear válvulas
    v_entrada1 = Valvula(TipoValvula.ENTRADA, caudal=20)  # 20 L/s
    v_entrada2 = Valvula(TipoValvula.ENTRADA, caudal=15)  # 15 L/s
    v_salida = Valvula(TipoValvula.SALIDA, caudal=25)    # 25 L/s
    
    tanque.valvulas = [v_entrada1, v_entrada2, v_salida]
    
    # Mostrar estado inicial
    imprimir_estado(tanque, "Estado inicial del tanque")
    
    # Iniciar llenado
    print("\n🚰 Iniciando proceso de llenado...")
    tanque.cargarTanque()
    
    # Simular 5 segundos de llenado
    for i in range(5):
        sleep(1)  # Esperar 1 segundo
        tanque.update(tiempo=1)
        imprimir_estado(tanque, f"Llenado en progreso - Segundo {i+1}")
    
    # Cambiar a vaciado
    print("\n🚯 Iniciando proceso de vaciado...")
    tanque.vaciarTanque()
    
    # Simular 3 segundos de vaciado
    for i in range(3):
        sleep(1)  # Esperar 1 segundo
        tanque.update(tiempo=1)
        imprimir_estado(tanque, f"Vaciado en progreso - Segundo {i+1}")
    
    # Detener todas las válvulas cerrándolas manualmente
    print("\n🛑 Deteniendo todas las operaciones...")
    for valvula in tanque.valvulas:
        valvula.cerrarValvula()
    
    # Mostrar estado final
    tanque.update(tiempo=1)
    imprimir_estado(tanque, "Estado final del sistema")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\n⚠️  Programa interrumpido por el usuario")
    except Exception as e:
        print(f"\n❌ Error: {str(e)}")
    finally:
        print("\n🏁 Programa finalizado")