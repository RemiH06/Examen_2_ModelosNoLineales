Información del Proyecto
-------------------------

:Título: Predicción de Precios de Acciones con SARIMAX y FFNN
:Autores:
    - Ivo
    - Remi
    - Juan Pablo

:Universidad: ITESO (Instituto Tecnológico y de Estudios Superiores de Occidente)
:Curso: [Modelos no Lineales para Pronósticos]
:Profesor: [Pedro Martinez]
:Fecha: Octubre 2025

Repositorio
-----------

El código fuente y datos del proyecto están disponibles en:

🔗 [https://github.com/RemiH06/Examen_2_ModelosNoLineales]

Resumen Ejecutivo
-----------------

Este proyecto implementa y compara dos enfoques distintos para la predicción de series temporales financieras:

**Modelo 1: SARIMAX**
    Modelo estadístico clásico que captura patrones autoregresivos, de media móvil y estacionales en los datos. Configuración óptima: order=(1,1,1), seasonal_order=(1,1,1,5).

**Modelo 2: FFNN (Feed-Forward Neural Network / MLP)**
    Red neuronal profunda que aprende representaciones no lineales de los datos históricos con 20 días de lookback.

**Objetivo Principal**
    Predecir el precio de cierre diario de NVIDIA (NVDA) para los días 16, 17, 20, 21 y 22 de octubre de 2025.

**Resultados Clave**
    - Análisis exhaustivo de datos desde 2010
    - Implementación robusta con semilla fija (SEED=42) para reproducibilidad
    - Búsqueda automática de hiperparámetros óptimos para SARIMAX (por AIC)
    - Arquitectura MLP de 2 capas ocultas (64→32 neuronas)
    - Ensemble promediando ambos modelos para mayor robustez
    - Validación con datos reales del mercado

Contacto
--------

Para preguntas o comentarios sobre este proyecto:

- **Email**: [remi.hexagon@gmail.com]
- **Issues**: [https://github.com/RemiH06/Examen_2_ModelosNoLineales]/issues