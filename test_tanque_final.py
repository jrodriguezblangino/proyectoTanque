from time import sleep
from datetime import datetime
from decimal import Decimal
from typing import List
from tanque import Tanque, Valvula, TipoValvula

class DemostracionTanque:
    def __init__(self):
        """Inicializa la demostración con diferentes configuraciones de tanques."""
        # Tanque principal para pruebas generales
        self.tanque_principal = Tanque(diametro=2, altura=3)
        
        # Tanque pequeño para pruebas de límites
        self.tanque_pequeno = Tanque(diametro=1, altura=1)
        
        # Tanque grande para pruebas de volumen
        self.tanque_grande = Tanque(diametro=5, altura=10)

    def imprimir_estado(self, tanque: Tanque, mensaje: str = "Estado actual") -> None:
        """Imprime el estado actual del tanque de forma detallada."""
        print("\n" + "="*70)
        print(f"📊 {mensaje} - {datetime.now().strftime('%H:%M:%S')}")
        print("="*70)
        
        nivel = tanque.calcularNivel()
        volumen_max = float(tanque.calcular_volumen_maximo())
        
        print(f"📐 Dimensiones: {float(tanque.diametro)}m (diámetro) x {float(tanque.altura)}m (altura)")
        print(f"📏 Nivel actual: {nivel['metros']:.2f}m ({nivel['porcentaje']:.1f}%)")
        print(f"🌊 Volumen actual: {float(tanque.volumenActual):.2f}L / {volumen_max:.2f}L")
        
        print("\n📈 Estado de válvulas:")
        for i, valvula in enumerate(tanque.valvulas, 1):
            tipo = "entrada ⬆️ " if valvula.tipo == TipoValvula.ENTRADA else "salida ⬇️ "
            estado = "ABIERTA" if valvula.caudalActual != 0 else "CERRADA"
            caudal = abs(float(valvula.caudalActual))
            print(f"  Válvula {i} ({tipo}): {estado} - Caudal: {caudal:.2f} L/s")
        print("-"*70)

    def ejecutar_demostracion_completa(self):
        """Ejecuta una demostración completa del sistema."""
        try:
            print("\n🏭 INICIANDO DEMOSTRACIÓN COMPLETA DEL SISTEMA DE TANQUE")
            
            # 1. Demostración de configuración de válvulas
            self._demo_configuracion_valvulas()
            
            # 2. Demostración de llenado normal
            self._demo_llenado_normal()
            
            # 3. Demostración de vaciado normal
            self._demo_vaciado_normal()
            
            # 4. Demostración de límites y casos extremos
            self._demo_limites()
            
            # 5. Demostración de operaciones mixtas
            self._demo_operaciones_mixtas()
            
            # 6. Demostración de casos de error
            self._demo_casos_error()
            
            # 7. Demostración de rendimiento
            self._demo_rendimiento()

        except KeyboardInterrupt:
            print("\n\n⚠️  Demostración interrumpida por el usuario")
        except Exception as e:
            print(f"\n❌ Error en la demostración: {str(e)}")
        finally:
            print("\n🏁 Demostración finalizada")

    def _demo_configuracion_valvulas(self):
        """Demuestra la configuración de diferentes tipos de válvulas."""
        print("\n🔧 PRUEBA 1: CONFIGURACIÓN DE VÁLVULAS")
        
        # Crear diferentes tipos de válvulas
        valvulas = [
            Valvula(TipoValvula.ENTRADA, caudal=20),  # Entrada rápida
            Valvula(TipoValvula.ENTRADA, caudal=10),  # Entrada lenta
            Valvula(TipoValvula.SALIDA, caudal=15),   # Salida media
            Valvula(TipoValvula.SALIDA, caudal=25)    # Salida rápida
        ]
        
        self.tanque_principal.valvulas = valvulas
        self.imprimir_estado(self.tanque_principal, "Configuración inicial de válvulas")

    def _demo_llenado_normal(self):
        """Demuestra el proceso de llenado normal."""
        print("\n🚰 PRUEBA 2: PROCESO DE LLENADO NORMAL")
        
        self.tanque_principal.cargarTanque()
        
        for i in range(10):
            sleep(1)
            self.tanque_principal.update(tiempo=1)
            self.imprimir_estado(self.tanque_principal, f"Llenado normal - Segundo {i+1}")

    def _demo_vaciado_normal(self):
        """Demuestra el proceso de vaciado normal."""
        print("\n🚯 PRUEBA 3: PROCESO DE VACIADO NORMAL")
        
        self.tanque_principal.vaciarTanque()
        
        for i in range(8):
            sleep(1)
            self.tanque_principal.update(tiempo=1)
            self.imprimir_estado(self.tanque_principal, f"Vaciado normal - Segundo {i+1}")

    def _demo_limites(self):
        """Demuestra comportamiento en casos límite."""
        print("\n🔍 PRUEBA 4: CASOS LÍMITE")
        
        # Prueba de sobrellenado
        print("\n📈 Intentando sobrepasar capacidad máxima...")
        self.tanque_pequeno.valvulas = [Valvula(TipoValvula.ENTRADA, caudal=1000)]
        self.tanque_pequeno.cargarTanque()
        self.tanque_pequeno.update(tiempo=10)
        self.imprimir_estado(self.tanque_pequeno, "Intento de sobrellenado")
        
        # Prueba de vaciado excesivo
        print("\n📉 Intentando vaciar más allá de cero...")
        self.tanque_pequeno.vaciarTanque()
        self.tanque_pequeno.update(tiempo=10)
        self.imprimir_estado(self.tanque_pequeno, "Intento de vaciado excesivo")

    def _demo_operaciones_mixtas(self):
        """Demuestra operaciones mezcladas de llenado y vaciado."""
        print("\n🔄 PRUEBA 5: OPERACIONES MIXTAS")
        
        # Configurar algunas válvulas abiertas y otras cerradas
        for i, valvula in enumerate(self.tanque_principal.valvulas):
            if i % 2 == 0:
                valvula.abrirValvula()
            else:
                valvula.cerrarValvula()
        
        for i in range(5):
            self.tanque_principal.update(tiempo=1)
            self.imprimir_estado(self.tanque_principal, f"Operación mixta - Segundo {i+1}")

    def _demo_casos_error(self):
        """Demuestra el manejo de casos de error."""
        print("\n⚠️ PRUEBA 6: CASOS DE ERROR")
        
        print("\nProbando tiempo negativo...")
        try:
            self.tanque_principal.update(tiempo=-1)
        except ValueError as e:
            print(f"Error capturado correctamente: {e}")
        
        print("\nProbando dimensiones inválidas...")
        try:
            tanque_invalido = Tanque(diametro=-1, altura=0)
        except ValueError as e:
            print(f"Error capturado correctamente: {e}")

    def _demo_rendimiento(self):
        """Demuestra el rendimiento con operaciones intensivas."""
        print("\n⚡ PRUEBA 7: PRUEBA DE RENDIMIENTO")
        
        # Configurar tanque grande con múltiples válvulas
        valvulas_masivas = [
            Valvula(TipoValvula.ENTRADA, caudal=100) for _ in range(5)
        ] + [
            Valvula(TipoValvula.SALIDA, caudal=80) for _ in range(5)
        ]
        
        self.tanque_grande.valvulas = valvulas_masivas
        
        print("\nRealizando 100 actualizaciones rápidas...")
        inicio = datetime.now()
        
        for i in range(100):
            self.tanque_grande.update(tiempo=0.1)
            if i % 20 == 0:  # Mostrar estado cada 20 iteraciones
                self.imprimir_estado(self.tanque_grande, f"Iteración {i+1}/100")
        
        tiempo_total = (datetime.now() - inicio).total_seconds()
        print(f"\n⏱️  Tiempo total de procesamiento: {tiempo_total:.2f} segundos")

if __name__ == "__main__":
    demo = DemostracionTanque()
    demo.ejecutar_demostracion_completa()