# Sistema Simulador de Tanques
[English version below](#tank-system-simulator)

Un simulador basado en Python que modela la dinámica de fluidos en tanques industriales con múltiples válvulas para el control de flujo de entrada y salida.

## Descripción General

Este proyecto simula un sistema de tanques industriales con dimensiones configurables y múltiples válvulas. Proporciona monitoreo en tiempo real de niveles de fluido, estados de válvulas y tasas de flujo, haciéndolo ideal para propósitos educativos o simulación de procesos industriales.

## Características

- **Dimensiones Configurables del Tanque**: Crea tanques con diámetro y altura personalizados
- **Soporte para Múltiples Válvulas**: Agrega válvulas tanto de entrada como de salida con diferentes tasas de flujo
- **Monitoreo en Tiempo Real**: Seguimiento de niveles de fluido, volúmenes y estados de válvulas
- **Controles de Seguridad**: Protección incorporada contra desbordamiento y vaciado
- **Pruebas Completas**: Incluye suites de pruebas básicas y avanzadas

## Suites de Prueba

El proyecto incluye dos archivos de prueba:

1. **testtanque.py**: Suite de pruebas básica que demuestra:
   - Inicialización del tanque
   - Operaciones básicas de válvulas
   - Ciclos de llenado y vaciado
   - Monitoreo del estado del sistema

2. **test_tanque_final.py**: Suite de pruebas avanzada con pruebas exhaustivas:
   - Pruebas de configuración de válvulas
   - Operaciones normales de llenado
   - Operaciones normales de vaciado
   - Manejo de casos límite
   - Operaciones mixtas
   - Manejo de errores
   - Pruebas de rendimiento

## Ejemplo de Uso

```python
from tanque import Tanque, Valvula, TipoValvula

# Crear un tanque (2m de diámetro, 3m de altura)
tanque = Tanque(diametro=2, altura=3)

# Agregar válvulas
valvulas = [
    Valvula(TipoValvula.ENTRADA, caudal=20),  # Válvula de entrada: 20 L/s
    Valvula(TipoValvula.SALIDA, caudal=15)    # Válvula de salida: 15 L/s
]
tanque.valvulas = valvulas

# Iniciar operación de llenado
tanque.cargarTanque()

# Actualizar estado del sistema
tanque.update(tiempo=1)
```

## Ejecutar Pruebas

### Suite de Pruebas Básica
```bash
python testtanque.py
```

### Suite de Pruebas Avanzada
```bash
python test_tanque_final.py
```

## Requisitos del Sistema

- Python 3.x
- Módulos requeridos:
  - `time`
  - `datetime`
  - `decimal`
  - `typing`

## Características Demostradas en las Pruebas

- Monitoreo en tiempo real del nivel del tanque
- Cálculos de volumen
- Control de tasa de flujo
- Gestión de múltiples válvulas
- Manejo de errores y límites del sistema
- Rendimiento bajo condiciones de estrés

## Notas

- Todas las medidas utilizan el sistema métrico
- Los volúmenes están en litros
- Las tasas de flujo están en litros por segundo
- Las dimensiones están en metros

## Manejo de Errores

El sistema incluye un robusto manejo de errores para:
- Dimensiones inválidas del tanque
- Valores negativos de tiempo
- Condiciones de desbordamiento
- Condiciones de vaciado
- Configuraciones inválidas de válvulas

---

# Tank System Simulator

A Python-based tank system simulator that models fluid dynamics in industrial tanks with multiple valves for input and output flow control.

## Overview

This project simulates an industrial tank system with configurable dimensions and multiple valves. It provides real-time monitoring of fluid levels, valve states, and flow rates, making it ideal for educational purposes or industrial process simulation.

## Features

- **Configurable Tank Dimensions**: Create tanks with custom diameter and height
- **Multiple Valve Support**: Add both input and output valves with different flow rates
- **Real-time Monitoring**: Track fluid levels, volumes, and valve states
- **Safety Controls**: Built-in overflow and underflow protection
- **Comprehensive Testing**: Includes both basic and advanced test suites

## Test Suites

The project includes two test files:

1. **testtanque.py**: Basic test suite that demonstrates:
   - Tank initialization
   - Basic valve operations
   - Fill and drain cycles
   - System state monitoring

2. **test_tanque_final.py**: Advanced test suite with comprehensive testing:
   - Valve configuration testing
   - Normal filling operations
   - Normal draining operations
   - Edge case handling
   - Mixed operations
   - Error handling
   - Performance testing

## Usage Example

```python
from tanque import Tanque, Valvula, TipoValvula

# Create a tank (2m diameter, 3m height)
tanque = Tanque(diametro=2, altura=3)

# Add valves
valvulas = [
    Valvula(TipoValvula.ENTRADA, caudal=20),  # Input valve: 20 L/s
    Valvula(TipoValvula.SALIDA, caudal=15)    # Output valve: 15 L/s
]
tanque.valvulas = valvulas

# Start filling operation
tanque.cargarTanque()

# Update system state
tanque.update(tiempo=1)
```

## Running Tests

### Basic Test Suite
```bash
python testtanque.py
```

### Advanced Test Suite
```bash
python test_tanque_final.py
```

## System Requirements

- Python 3.x
- Required modules:
  - `time`
  - `datetime`
  - `decimal`
  - `typing`

## Features Demonstrated in Tests

- Real-time tank level monitoring
- Volume calculations
- Flow rate control
- Multiple valve management
- Error handling and system limits
- Performance under stress conditions

## Notes

- All measurements use the metric system
- Volumes are in liters
- Flow rates are in liters per second
- Dimensions are in meters

## Error Handling

The system includes robust error handling for:
- Invalid tank dimensions
- Negative time values
- Overflow conditions
- Underflow conditions
- Invalid valve configurations
