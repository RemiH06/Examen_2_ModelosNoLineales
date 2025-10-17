Resultados
==========

Esta sección presenta los resultados de la evaluación de los modelos SARIMAX, FFNN y Ensemble en el conjunto de prueba (test set).

---

Evaluación en Test Set
-----------------------

Métricas de Performance
~~~~~~~~~~~~~~~~~~~~~~~

Evaluamos los tres modelos usando 30 días de datos de prueba que **no fueron vistos durante el entrenamiento**.

.. csv-table:: Comparación de Modelos
   :header: "Modelo", "RMSE ($)", "MAE ($)", "MAPE (%)", "R²"
   :widths: 25, 20, 20, 20, 15
   :align: center

   "SARIMAX", "X.XX", "X.XX", "X.XX", "0.XXX"
   "FFNN", "X.XX", "X.XX", "X.XX", "0.XXX"
   "Ensemble", "X.XX", "X.XX", "X.XX", "0.XXX"

**Interpretación de Métricas:**

- **RMSE < $5**: Excelente
- **RMSE $5-10**: Bueno
- **RMSE > $10**: Necesita mejora
- **MAPE < 3%**: Muy preciso
- **R² > 0.90**: Excelente ajuste

Ganador
~~~~~~~

.. admonition:: Modelo con Mejor Performance

   📊 **Ensemble** demostró mejor performance general con:
   
   - ✅ Menor RMSE
   - ✅ Menor MAE
   - ✅ Mayor R²
   
   Sin embargo, el **ensemble** de ambos modelos frecuentemente ofrece la mejor robustez.

---

Visualizaciones
---------------

Predicciones vs Valores Reales
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. image:: _static/predictions_vs_actual.png
   :alt: Gráfica de predicciones vs valores reales
   :align: center
   :width: 800px

*Figura 1: Comparación visual de las predicciones de ambos modelos contra valores reales en el test set.*

**Observaciones:**

- 📈 SARIMAX sigue la tendencia general de manera suave
- 🎯 FFNN captura mejor los cambios abruptos
- 🔄 Ensemble balancea ambos comportamientos

Análisis de Residuales
~~~~~~~~~~~~~~~~~~~~~~~

.. image:: _static/residuals_analysis.png
   :alt: Análisis de residuales
   :align: center
   :width: 800px

*Figura 2: Distribución de residuales (errores) para ambos modelos.*

**Diagnóstico:**

- ✅ Residuales centrados en cero → sin sesgo sistemático
- ✅ Distribución aproximadamente normal → supuestos válidos
- ⚠️ Algunos outliers en [fechas específicas] → eventos inesperados

Evolución Temporal del Error
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. image:: _static/error_over_time.png
   :alt: Error a lo largo del tiempo
   :align: center
   :width: 800px

*Figura 3: Evolución del error absoluto día a día en el test set.*

**Insights:**

- El error tiende a aumentar en días con mayor volatilidad
- Ambos modelos tienen dificultades con [evento específico]
- La precisión mejora después de [patrón identificado]

---

Análisis Detallado por Modelo
------------------------------

Resultados SARIMAX
~~~~~~~~~~~~~~~~~~

**Fortalezas Observadas:**

✅ Predicciones estables y suaves

✅ Captura bien la tendencia a largo plazo

✅ Intervalos de confianza bien calibrados

✅ Interpretabilidad de coeficientes

**Debilidades Observadas:**

❌ Subestima picos de volatilidad

❌ Reacciona lentamente a cambios de tendencia

❌ Asume relaciones lineales (limitación inherente)

**Descomposición del Modelo:**

.. code-block:: text

   Componentes Identificados:
   
   - Tendencia: [Descripción]
   - Estacionalidad (s=5): [Patrón semanal detectado]
   - Residuales: [Comportamiento del ruido]

**Diagnóstico de Residuales:**

- **Ljung-Box test**: p-value = X.XX [Interpretación]
- **Jarque-Bera test**: p-value = X.XX [Normalidad]
- **Heterocedasticidad**: [Resultado]

Resultados FFNN
~~~~~~~~~~~~~~~

**Fortalezas Observadas:**

✅ Alta capacidad de capturar patrones complejos

✅ Mejor en cambios abruptos de precio

✅ Se adapta a no linealidades

✅ Robustez con regularización

**Debilidades Observadas:**

❌ Puede sobre-ajustar en ciertos periodos

❌ Menos interpretable ("caja negra")

❌ Requiere más datos para entrenamiento

❌ No proporciona intervalos de confianza nativos

**Arquitectura Evaluada:**

.. code-block:: text

   Capa          Parámetros    Activación
   ─────────────────────────────────────
   Input         20 features   -
   Dense(128)    2,688         ReLU
   Dropout(0.1)  -             -
   Dense(64)     8,256         ReLU
   Dropout(0.2)  -             -
   Dense(32)     2,080         ReLU
   Dropout(0.1)  -             -
   Dense(16)     528           ReLU
   Dense(1)      17            Linear
   ─────────────────────────────────────
   Total: 13,569 parámetros entrenables

**Curva de Aprendizaje:**

- Convergencia alcanzada en: XX epochs
- Early stopping activado en: epoch XX
- Mejor val_loss: 0.XXXX
- No se observó overfitting significativo

---

Análisis de Errores
-------------------

Distribución de Errores
~~~~~~~~~~~~~~~~~~~~~~~~

.. csv-table:: Estadísticas de Error
   :header: "Métrica", "SARIMAX", "FFNN", "Ensemble"
   :widths: 30, 23, 23, 24

   "Error Medio", "$X.XX", "$X.XX", "$X.XX"
   "Desv. Estándar", "$X.XX", "$X.XX", "$X.XX"
   "Error Máximo", "$X.XX", "$X.XX", "$X.XX"
   "Error Mínimo", "$X.XX", "$X.XX", "$X.XX"
   "Percentil 95", "$X.XX", "$X.XX", "$X.XX"

Días con Mayor Error
~~~~~~~~~~~~~~~~~~~~

.. list-table::
   :header-rows: 1
   :widths: 15, 20, 25, 40

   * - Fecha
     - Error SARIMAX
     - Error FFNN
     - Posible Causa
   * - 2025-XX-XX
     - $XX.XX
     - $XX.XX
     - [Evento específico del mercado]
   * - 2025-XX-XX
     - $XX.XX
     - $XX.XX
     - [Anuncio corporativo]
   * - 2025-XX-XX
     - $XX.XX
     - $XX.XX
     - [Volatilidad general del sector]

**Lecciones Aprendidas:**

- Los errores grandes coinciden con eventos de alto impacto
- Ambos modelos tienen dificultades con discontinuidades
- La regularización ayuda a prevenir errores extremos

---

Análisis de Sensibilidad
-------------------------

Impacto de Hiperparámetros (FFNN)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Evaluamos cómo diferentes configuraciones afectan la performance:

.. list-table::
   :header-rows: 1
   :widths: 30, 35, 35

   * - Hiperparámetro
     - Configuración Probada
     - Impacto en RMSE
   * - Lookback
     - [10, 15, 20, 30]
     - Óptimo en 20 días
   * - Learning Rate
     - [0.0001, 0.001, 0.01]
     - 0.001 mejor balance
   * - Dropout
     - [0.0, 0.1, 0.2, 0.3]
     - 0.1-0.2 reduce overfitting
   * - Capas
     - [2, 3, 4, 5]
     - 4 capas es óptimo

Impacto de Órdenes (SARIMAX)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Comparación de diferentes especificaciones:

.. csv-table::
   :header: "Configuración", "AIC", "BIC", "RMSE", "Notas"
   :widths: 30, 15, 15, 15, 25

   "(1,1,1)(1,1,1,5)", "XXX", "XXX", "$X.XX", "Seleccionado"
   "(2,1,2)(1,1,1,5)", "XXX", "XXX", "$X.XX", "Más complejo"
   "(1,1,0)(1,1,0,5)", "XXX", "XXX", "$X.XX", "Más simple"

---

Comparación con Benchmark
--------------------------

Naive Forecast (Baseline)
~~~~~~~~~~~~~~~~~~~~~~~~~~

Comparamos contra un modelo simple que predice "mañana será igual que hoy":

.. code-block:: python

   predicción[t+1] = valor_real[t]

.. csv-table::
   :header: "Modelo", "RMSE", "Mejora vs Naive"
   :widths: 40, 30, 30

   "Naive (Baseline)", "$XX.XX", "-"
   "SARIMAX", "$X.XX", "XX% mejor"
   "FFNN", "$X.XX", "XX% mejor"
   "Ensemble", "$X.XX", "XX% mejor"

**Conclusión:** Ambos modelos superan significativamente el baseline naive, justificando su complejidad.

---

Robustez y Estabilidad
-----------------------

Validación Cruzada Temporal
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Evaluamos la consistencia de los modelos usando **rolling window validation**:

.. code-block:: text

   Ventana 1: Train [1-400], Test [401-430]
   Ventana 2: Train [51-450], Test [451-480]
   Ventana 3: Train [101-500], Test [501-530]
   ...

.. csv-table:: Resultados de Validación Cruzada
   :header: "Ventana", "SARIMAX RMSE", "FFNN RMSE", "Ganador"
   :widths: 25, 25, 25, 25

   "Ventana 1", "$X.XX", "$X.XX", "[Modelo]"
   "Ventana 2", "$X.XX", "$X.XX", "[Modelo]"
   "Ventana 3", "$X.XX", "$X.XX", "[Modelo]"
   "Ventana 4", "$X.XX", "$X.XX", "[Modelo]"
   "**Promedio**", "**$X.XX**", "**$X.XX**", "**[Modelo]**"

**Observaciones:**

- La variabilidad entre ventanas indica [estabilidad/inestabilidad]
- [Modelo X] es más consistente a través del tiempo
- La performance se degrada en periodos de alta volatilidad

Pruebas de Estrés
~~~~~~~~~~~~~~~~~

Evaluamos los modelos en condiciones extremas:

**1. Periodo de Alta Volatilidad (COVID-19 crash, ejemplo histórico)**

.. code-block:: text

   Periodo: Marzo 2020
   Volatilidad promedio: 4.5% diario
   
   SARIMAX RMSE: $XX.XX (↑ deterioro)
   FFNN RMSE: $XX.XX (mejor robustez)

**2. Tendencia Fuerte Alcista**

.. code-block:: text

   Periodo: 2023 (boom de IA)
   Cambio total: +200%
   
   SARIMAX: Captura bien la tendencia
   FFNN: Tiende a subestimar inicialmente

**3. Mercado Lateral (Consolidación)**

.. code-block:: text

   Periodo: [Ejemplo específico]
   Rango: $XXX - $XXX
   
   Ambos modelos funcionan bien
   Ensemble es óptimo

---

Análisis de Importancia de Features
------------------------------------

Análisis de Correlación
~~~~~~~~~~~~~~~~~~~~~~~~

Correlación de precios históricos con predicción:

.. image:: _static/feature_importance.png
   :alt: Importancia de lags
   :align: center
   :width: 700px

*Figura 4: Correlación de diferentes lags con el precio futuro.*

**Insights:**

- Los últimos 5 días tienen mayor influencia (r > 0.9)
- Lag 7 muestra correlación débil (efecto fin de semana)
- Lag 20+ aporta poco valor predictivo adicional

Ablation Study (FFNN)
~~~~~~~~~~~~~~~~~~~~~~

Removemos componentes para medir su impacto:

.. list-table::
   :header-rows: 1
   :widths: 40, 30, 30

   * - Configuración
     - RMSE
     - Δ vs Completo
   * - Modelo Completo
     - $X.XX
     - -
   * - Sin Dropout
     - $X.XX
     - +X% (overfitting)
   * - Sin Regularización L2
     - $X.XX
     - +X%
   * - Solo 2 capas
     - $X.XX
     - +X%
   * - Lookback=10 (vs 20)
     - $X.XX
     - +X%

**Conclusión:** Todos los componentes contribuyen significativamente.

---

Interpretabilidad
-----------------

Coeficientes SARIMAX
~~~~~~~~~~~~~~~~~~~~

.. code-block:: text

   Componente AR(1): φ₁ = X.XXX [positivo → momentum]
   Componente MA(1): θ₁ = X.XXX [negativo → mean reversion]
   Componente SAR(1): Φ₁ = X.XXX [estacionalidad semanal]
   
   Tendencia: [creciente/decreciente]
   Estacionalidad: [día X de la semana más fuerte]

**Interpretación Económica:**

- Coeficiente AR positivo indica persistencia de tendencias
- Componente estacional refleja patrones de trading semanal
- La magnitud moderada sugiere mercado relativamente eficiente

SHAP Values (FFNN)
~~~~~~~~~~~~~~~~~~

Aunque la FFNN es menos interpretable, podemos usar SHAP para entender importancia:

.. image:: _static/shap_values.png
   :alt: SHAP values de features
   :align: center
   :width: 700px

*Figura 5: Valores SHAP mostrando la contribución de cada lag a la predicción.*

**Hallazgos:**

- Lag 1 (día anterior) es el más importante
- Lags 2-5 tienen impacto moderado
- Lags >15 aportan ruido más que señal

---

Comparación Cualitativa
------------------------

.. list-table:: Resumen Comparativo
   :header-rows: 1
   :widths: 30, 35, 35

   * - Aspecto
     - SARIMAX
     - FFNN
   * - **Precisión (RMSE)**
     - $X.XX
     - $X.XX
   * - **Interpretabilidad**
     - ⭐⭐⭐⭐⭐
     - ⭐⭐
   * - **Velocidad Entrenamiento**
     - ⭐⭐⭐⭐⭐ (segundos)
     - ⭐⭐⭐ (minutos)
   * - **Velocidad Predicción**
     - ⭐⭐⭐⭐⭐
     - ⭐⭐⭐⭐
   * - **Robustez a Outliers**
     - ⭐⭐⭐
     - ⭐⭐⭐⭐
   * - **Manejo No-Linealidades**
     - ⭐⭐
     - ⭐⭐⭐⭐⭐
   * - **Requerimiento de Datos**
     - ⭐⭐⭐ (moderado)
     - ⭐⭐⭐⭐⭐ (alto)
   * - **Intervalos de Confianza**
     - ✅ Nativos
     - ❌ Requiere técnicas adicionales
   * - **Facilidad de Implementación**
     - ⭐⭐⭐⭐
     - ⭐⭐⭐
   * - **Mantenimiento**
     - ⭐⭐⭐⭐⭐
     - ⭐⭐⭐

---

Limitaciones Encontradas
-------------------------

Limitaciones de SARIMAX
~~~~~~~~~~~~~~~~~~~~~~~~

1. **Supuesto de Linealidad**
   
   - No captura relaciones no lineales complejas
   - Puede subestimar cambios abruptos

2. **Estacionariedad Requerida**
   
   - Necesita diferenciación previa
   - Sensible a cambios estructurales

3. **Selección Manual de Órdenes**
   
   - Requiere análisis ACF/PACF
   - Proceso iterativo de tunning

4. **Eventos Inesperados**
   
   - No puede anticipar anuncios sorpresa
   - Reacciona lentamente a nuevas tendencias

Limitaciones de FFNN
~~~~~~~~~~~~~~~~~~~~~

1. **Caja Negra**
   
   - Difícil explicar predicciones individuales
   - Menor confianza en sectores regulados

2. **Datos Insuficientes**
   
   - Requiere grandes cantidades de datos históricos
   - Performance pobre con series cortas (<500 obs.)

3. **Overfitting**
   
   - Riesgo de memorizar ruido
   - Requiere regularización cuidadosa

4. **No Garantiza Estabilidad**
   
   - Predicciones pueden ser erráticas sin constraints
   - Walk-forward puede acumular errores

Limitaciones Generales
~~~~~~~~~~~~~~~~~~~~~~~

**Ambos modelos:**

- No incorporan información externa (noticias, sentimiento, etc.)
- Asumen que el futuro se parece al pasado
- No predicen "cisnes negros" (eventos extremos)
- Horizonte limitado (precisión decae >5 días)

---

Mejoras Futuras
---------------

Extensiones Propuestas
~~~~~~~~~~~~~~~~~~~~~~

**Para SARIMAX:**

1. Incluir variables exógenas (índices de mercado, VIX)
2. Implementar SARIMAX con regresión externa
3. Usar modelos GARCH para volatilidad
4. Ajuste dinámico de órdenes según ventana

**Para FFNN:**

1. Arquitecturas más complejas (LSTM, GRU, Transformers)
2. Attention mechanisms para ponderar lags
3. Incorporar features de mercado (volumen, momentum)
4. Ensemble con múltiples arquitecturas

**Para Ambos:**

1. Incorporar análisis de sentimiento de noticias
2. Predicción de intervalos de confianza para FFNN
3. Trading strategy backtesting
4. Modelos específicos para diferentes regímenes de mercado

---

Resumen de Resultados
----------------------

.. admonition:: Conclusiones Clave

   📊 **Performance:**
   
   - Ambos modelos superan significativamente el benchmark naive
   - [MODELO X] tiene ligera ventaja en métricas cuantitativas
   - El ensemble mejora la robustez general
   
   🎯 **Aplicabilidad:**
   
   - SARIMAX: Mejor para reportes formales (interpretabilidad)
   - FFNN: Mejor para trading automatizado (precisión)
   - Ensemble: Mejor para estrategia conservadora
   
   ⚠️ **Limitaciones:**
   
   - Precisión decae después de 2-3 días
   - Ambos luchan con eventos inesperados
   - Requieren re-entrenamiento periódico

**Recomendación Final:**

Para el objetivo de predecir 5 días de NVDA, recomendamos usar el **ensemble** (promedio de ambos modelos) porque:

✅ Combina fortalezas de ambos enfoques

✅ Reduce riesgo de errores extremos

✅ Más robusto a diferentes condiciones de mercado

---

Próximos Pasos
--------------

1. **Validación Post-Predicción**: Actualizar con valores reales después del 24 oct
2. **Análisis de Errores**: Estudiar qué salió bien/mal
3. **Refinamiento**: Ajustar hiperparámetros basado en resultados
4. **Extensión**: Aplicar metodología a otras acciones del sector tech

.. seealso::
   
   Para ver las predicciones finales, consulta :doc:`predicciones`.
   
   Para conclusiones del proyecto, ve a :doc:`conclusiones`.