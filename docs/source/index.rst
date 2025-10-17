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

**Menú**
.. toctree::
   :maxdepth: 2
   :caption: 📚 Contenido del Proyecto:

   portada
   motivacion
   metodologia
   predicciones
   resultados
   conclusiones

Resumen Rápido
==============

**Acción analizada:** NVIDIA (NVDA) - NASDAQ

**Modelos implementados:**

- 📊 **SARIMAX** (1,1,1)(1,1,1,5) - Modelo estadístico con estacionalidad semanal
- 🤖 **FFNN** (MLP) - Red neuronal con 20 lags de entrada

**Período de predicción:** 16-17 y 20-22 de octubre de 2025 (5 días hábiles)

**Datos:** Históricos desde 2010 hasta 15 de octubre de 2025

**Reproducibilidad:** Semilla fija SEED=42

Predicciones Destacadas
========================

.. csv-table:: 
   :header: "Fecha", "SARIMAX", "FFNN", "Ensemble"
   :widths: 25, 25, 25, 25

   "2025-10-16", "$179.47", "$175.90", "$177.68"
   "2025-10-17", "$179.61", "$173.70", "$176.65"
   "2025-10-20", "$179.57", "$170.54", "$175.05"
   "2025-10-21", "$179.79", "$167.79", "$173.79"
   "2025-10-22", "$180.28", "$165.93", "$173.10"

Para ver el análisis completo de las predicciones, consulta :doc:`predicciones`.

Navegación Rápida
=================

* :ref:`genindex`
* :ref:`search`

Contacto
--------

Para preguntas o comentarios sobre este proyecto:

- **Email**: [remi.hexagon@gmail.com]
- **Issues**: [https://github.com/RemiH06/Examen_2_ModelosNoLineales]/issues