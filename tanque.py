#El programa define dos objetos, un tanque y valvulas, para luego poder simular llenado/vaciado

from enum import Enum
from math import pi
from typing import List, Optional
from decimal import Decimal

#Definimos las clases de tipo de valvula y valvula

class TipoValvula(Enum):
    ENTRADA = "E"
    SALIDA = "S"

class Valvula:
    def __init__(self, tipo: str, caudal: float):
        """
        Inicializa una válvula.
        
        Args:
            tipo: Tipo de válvula ('E' para entrada, 'S' para salida)
            caudal: Caudal máximo de la válvula
        """
        if not isinstance(tipo, TipoValvula):
            tipo = TipoValvula(tipo)
        self.tipo = tipo
        self.caudal = caudal
        self.caudalActual = 0

    def abrirValvula(self) -> None:
        """Abre la válvula estableciendo el caudal según el tipo."""
        self.caudalActual = self.caudal if self.tipo == TipoValvula.ENTRADA else -self.caudal

    def cerrarValvula(self) -> None:
        """Cierra la válvula estableciendo el caudal a cero."""
        self.caudalActual = 0

#Definimos la clase Tanque

class Tanque:
    def __init__(self, diametro: float, altura: float, valvulas: Optional[List[Valvula]] = None):
        """
        Inicializa un tanque con sus dimensiones y válvulas.
        
        Args:
            diametro: Diámetro del tanque en metros
            altura: Altura del tanque en metros
            valvulas: Lista opcional de válvulas
        """
        if diametro <= 0 or altura <= 0:
            raise ValueError("Las dimensiones del tanque deben ser positivas")
        
        self.diametro = Decimal(str(diametro))
        self.altura = Decimal(str(altura))
        self.valvulas = valvulas or []
        self.volumenActual = Decimal('0')

    def calcular_volumen_maximo(self) -> Decimal:
        """Calcula el volumen máximo del tanque en litros."""
        return self.altura * Decimal(str(pi)) * (self.diametro / 2) ** 2 * 1000

    def calcularNivel(self) -> dict:
        """
        Calcula el nivel actual del tanque.
        
        Returns:
            dict: Diccionario con el nivel en porcentaje y metros
        """
        volumenMaximo = self.calcular_volumen_maximo()
        if volumenMaximo == 0:
            return {"porcentaje": 0, "metros": 0}
            
        nivelCalculado = self.volumenActual / volumenMaximo
        nivelMetros = nivelCalculado * self.altura
        
        return {
            "porcentaje": float(round(nivelCalculado * 100, 2)),
            "metros": float(round(nivelMetros, 2))
        }

    def update(self, tiempo: float = 1) -> None:
        """
        Actualiza el volumen del tanque según el caudal de las válvulas.
        
        Args:
            tiempo: Tiempo transcurrido en segundos
        """
        if tiempo <= 0:
            raise ValueError("El tiempo debe ser positivo")
            
        caudalResultante = sum(valvula.caudalActual for valvula in self.valvulas)
        aguaEntrante = Decimal(str(caudalResultante * tiempo))
        self.volumenActual += aguaEntrante
        
        # Limitar el volumen entre 0 y el máximo
        volumenMaximo = self.calcular_volumen_maximo()
        self.volumenActual = max(Decimal('0'), min(self.volumenActual, volumenMaximo))

    def cargarTanque(self) -> None:
        """Abre las válvulas de entrada y cierra las de salida."""
        self._operarValvulas(abrir_entrada=True)

    def vaciarTanque(self) -> None:
        """Abre las válvulas de salida y cierra las de entrada."""
        self._operarValvulas(abrir_entrada=False)
        
    def _operarValvulas(self, abrir_entrada: bool) -> None:
        """
        Método auxiliar para operar las válvulas según el tipo.
        
        Args:
            abrir_entrada: Si True, abre las válvulas de entrada y cierra las de salida.
                         Si False, hace lo contrario.
        """
        for valvula in self.valvulas:
            if (valvula.tipo == TipoValvula.ENTRADA) == abrir_entrada:
                valvula.abrirValvula()
            else:
                valvula.cerrarValvula()