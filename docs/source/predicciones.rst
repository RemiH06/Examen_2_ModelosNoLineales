Predicciones
============

Esta página contiene las predicciones oficiales de ambos modelos para los días **16, 17, 20, 21 y 22 de octubre de 2025**.

.. note::
   Las predicciones se generaron el **16 de octubre de 2025** utilizando datos históricos de NVIDIA (NVDA) desde 2010 hasta el **15 de octubre de 2025**.
   Todos los valores están en dólares estadounidenses (USD).
   **Semilla fija:** SEED=42 para reproducibilidad completa.

---

Tabla de Predicciones Oficiales
--------------------------------

.. csv-table:: Predicciones NVDA - Octubre 16-17 y 20-22, 2025
   :header: "Fecha", "SARIMAX ($)", "FFNN ($)", "Ensemble ($)"
   :widths: 25, 25, 25, 25
   :align: center
   :file: ../../artifacts/predicciones_NVDA_2025-10-20_24.csv

---

Visualización de Predicciones
------------------------------

Comparación de Modelos
~~~~~~~~~~~~~~~~~~~~~~

.. figure:: ../../artifacts/cheve_ensemble1.png
   :alt: Comparación de predicciones SARIMAX vs FFNN vs Ensemble
   :align: center
   :width: 90%

   **Figura 1:** Comparación visual de las predicciones de ambos modelos y el ensemble. 
   Se observa que SARIMAX mantiene una tendencia alcista estable (~$179-180), 
   mientras que FFNN muestra una tendencia bajista progresiva (~$176-166).

.. figure:: ../../artifacts/cheve_ensemble2.png
   :alt: Vista detallada del ensemble
   :align: center
   :width: 90%

   **Figura 2:** Vista ampliada del ensemble (promedio de ambos modelos), 
   mostrando la convergencia entre las predicciones SARIMAX y FFNN.

---

Detalles por Modelo
--------------------

Predicciones SARIMAX
~~~~~~~~~~~~~~~~~~~~

**Modelo:** SARIMAX(1,1,1)(1,1,1,5)

El modelo SARIMAX generó las siguientes predicciones:

.. list-table::
   :header-rows: 1
   :widths: 25 25 25 25

   * - Fecha
     - Predicción ($)
     - Cambio vs anterior
     - Tendencia
   * - 2025-10-16
     - 179.47
     - --
     - Base
   * - 2025-10-17
     - 179.61
     - +$0.14 (+0.08%)
     - ↗️ Alcista leve
   * - 2025-10-20
     - 179.57
     - -$0.04 (-0.02%)
     - ➡️ Lateral
   * - 2025-10-21
     - 179.79
     - +$0.22 (+0.12%)
     - ↗️ Alcista leve
   * - 2025-10-22
     - 180.28
     - +$0.49 (+0.27%)
     - ↗️ Alcista

.. figure:: ../../artifacts/ivo_sarimax1.png
   :alt: Predicciones SARIMAX - Vista 1
   :align: center
   :width: 85%

   **Figura 3:** Predicciones del modelo SARIMAX mostrando una tendencia alcista suave y estable.

.. figure:: ../../artifacts/ivo_sarimax2.png
   :alt: Predicciones SARIMAX - Vista 2
   :align: center
   :width: 85%

   **Figura 4:** Vista alternativa del modelo SARIMAX con contexto histórico.

**Características de las Predicciones SARIMAX:**

- ✅ Predicciones muy estables (rango de $0.81)
- ✅ Tendencia alcista suave y consistente (+0.45% total)
- ✅ Captura el patrón de consolidación del precio
- ✅ Intervalos de confianza disponibles (no mostrados)
- ⚠️ Puede subestimar volatilidad a corto plazo
- 📊 Rango: $179.47 - $180.28

---

Predicciones FFNN
~~~~~~~~~~~~~~~~~

**Modelo:** MLP (64→32 neuronas, 20 lags de entrada)

El modelo de red neuronal generó estas predicciones mediante pronóstico recursivo:

.. list-table::
   :header-rows: 1
   :widths: 25 25 25 25

   * - Fecha
     - Predicción ($)
     - Cambio vs anterior
     - Tendencia
   * - 2025-10-16
     - 175.90
     - --
     - Base
   * - 2025-10-17
     - 173.70
     - -$2.20 (-1.25%)
     - ↘️ Bajista
   * - 2025-10-20
     - 170.54
     - -$3.16 (-1.82%)
     - ↘️ Bajista
   * - 2025-10-21
     - 167.79
     - -$2.75 (-1.61%)
     - ↘️ Bajista
   * - 2025-10-22
     - 165.93
     - -$1.86 (-1.11%)
     - ↘️ Bajista

.. figure:: ../../artifacts/ivo_fnn1.png
   :alt: Predicciones FFNN - Vista 1
   :align: center
   :width: 85%

   **Figura 5:** Predicciones del modelo FFNN (red neuronal) mostrando una tendencia bajista progresiva.

.. figure:: ../../artifacts/ivo_fnn2.png
   :alt: Predicciones FFNN - Vista 2
   :align: center
   :width: 85%

   **Figura 6:** Vista alternativa del modelo FFNN con análisis de la tendencia descendente.

**Características de las Predicciones FFNN:**

- 📉 Tendencia bajista progresiva (-5.68% total en 5 días)
- ⚠️ Efecto de acumulación de error en pronóstico recursivo
- 🔄 Cada predicción alimenta la siguiente (walk-forward)
- ❌ Divergencia significativa respecto a SARIMAX
- 📊 Rango: $165.93 - $175.90 (volatilidad de $9.97)

**Análisis del comportamiento:**

El FFNN muestra una tendencia bajista marcada, posiblemente por:

1. Captura de momentum negativo reciente en los datos de entrenamiento
2. Acumulación de pequeños errores en el pronóstico recursivo
3. Mayor sensibilidad a patrones de corto plazo
4. Ausencia de regularización puede causar sobre-reacción a fluctuaciones

---

Consenso y Estrategia
---------------------

Predicción Ensamblada
~~~~~~~~~~~~~~~~~~~~~~

El **promedio simple** de ambos modelos ofrece un balance entre las predicciones:

.. list-table::
   :header-rows: 1
   :widths: 25 25 25 25

   * - Fecha
     - Ensemble ($)
     - Rango SARIMAX-FFNN
     - Nivel de Confianza
   * - 2025-10-16
     - 177.68
     - $3.57
     - Alta ⭐⭐⭐⭐⭐
   * - 2025-10-17
     - 176.65
     - $5.91
     - Alta ⭐⭐⭐⭐
   * - 2025-10-20
     - 175.05
     - $9.03
     - Media ⭐⭐⭐
   * - 2025-10-21
     - 173.79
     - $12.00
     - Media ⭐⭐
   * - 2025-10-22
     - 173.10
     - $14.35
     - Baja ⭐

**Ventajas del ensamble:**

1. ✅ Balancea la estabilidad de SARIMAX con la reactividad de FFNN
2. ✅ Reduce el riesgo de errores extremos de cualquier modelo individual
3. ⚠️ La divergencia creciente (de $3.57 a $14.35) indica alta incertidumbre en días 4-5

**Recomendación:**

Dado que la divergencia entre modelos aumenta significativamente:

- **Días 1-2 (16-17 oct)**: Usar ensemble con **confianza alta**
- **Días 3-5 (20-22 oct)**: Considerar **SARIMAX como más confiable** dado su comportamiento estable

---

Señales Indicativas (Solo Ilustrativo)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. warning::
   Esto es **solo ilustrativo** y NO constituye recomendación de inversión.
   Consulte con un asesor financiero profesional antes de tomar decisiones de inversión.

Basado en las predicciones del ensemble:

.. list-table::
   :header-rows: 1
   :widths: 25 25 25 25

   * - Fecha
     - Precio Estimado
     - Tendencia Ensemble
     - Señal Indicativa
   * - 2025-10-16
     - $177.68
     - Base
     - HOLD / OBSERVAR
   * - 2025-10-17
     - $176.65
     - ↘️ -0.58%
     - CAUTION ⚠️
   * - 2025-10-20
     - $175.05
     - ↘️ -0.91%
     - HOLD
   * - 2025-10-21
     - $173.79
     - ↘️ -0.72%
     - HOLD
   * - 2025-10-22
     - $173.10
     - ↘️ -0.40%
     - HOLD / RE-EVALUAR

**Interpretación:**

El ensemble sugiere una tendencia ligeramente bajista (-2.58% total), aunque:

- 📈 SARIMAX anticipa estabilidad/alza leve (+0.45%)
- 📉 FFNN anticipa caída más pronunciada (-5.68%)
- ⚠️ La divergencia indica **alta incertidumbre**

**Conclusión:** Esperar a los valores reales del mercado para validar cuál modelo fue más preciso antes de tomar decisiones.

---

Análisis de Confianza
----------------------

Factores que Afectan la Confianza
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. list-table::
   :header-rows: 1
   :widths: 30 35 35

   * - Factor
     - Impacto en SARIMAX
     - Impacto en FFNN
   * - **Horizonte temporal**
     - Confianza estable hasta día 5
     - Confianza decae rápido (recursivo)
   * - **Eventos inesperados**
     - No puede anticipar
     - No puede anticipar
   * - **Volatilidad del mercado**
     - Puede subestimar
     - Sobre-reacciona
   * - **Patrones históricos**
     - Captura bien
     - Memoriza pero puede overfittear

---

Tabla de Rendimiento Final
---------------------------

Resumen de Predicciones por Modelo
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. csv-table:: Tabla Completa de Predicciones
   :header: "Fecha", "SARIMAX", "FFNN", "Ensemble", "Divergencia"
   :widths: 20, 20, 20, 20, 20
   :align: center
   :file: ../../artifacts/fc_final.csv

*Nota: Esta tabla también está disponible en formato CSV en el repositorio.*

---

Descarga de Datos
-----------------

Las predicciones están disponibles para descarga:

📄 **CSV Predicciones 20-24 Oct**: :download:`predicciones_NVDA_2025-10-20_24.csv <../../artifacts/predicciones_NVDA_2025-10-20_24.csv>`

📄 **CSV Final Completo**: :download:`fc_final.csv <../../artifacts/fc_final.csv>`

📋 **Markdown**: :download:`predicciones_NVDA_2025-10-20_24.md <../../artifacts/predicciones_NVDA_2025-10-20_24.md>`

---

Contexto de Mercado
-------------------

Factores a Considerar al 15 de Octubre 2025
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Al interpretar estas predicciones, considerar:

**Factores Internos (NVIDIA)**

- 📊 Precio de cierre 15 oct: ~$[completar con precio real]
- 🚀 Reciente lanzamiento de GPUs para IA generativa
- 👔 Estabilidad en dirección ejecutiva
- 📰 Alianzas estratégicas activas (OpenAI, Microsoft, etc.)

**Factores Externos (Mercado)**

- 📈 NASDAQ en tendencia alcista general
- 💵 Tasas de interés de la Fed estables
- 🌍 Tensiones geopolíticas moderadas
- 🤖 Sentimiento positivo sobre IA y tecnología

**Indicadores Técnicos**

- 📊 Volumen de trading consistente
- 🔄 RSI, MACD en rangos normales
- 📉 Soportes recientes: ~$170, ~$165
- 📈 Resistencias: ~$180, ~$185

---

Comparación Post-Predicción
----------------------------

.. attention::
   Esta sección se actualizará después del 22 de octubre de 2025 con los valores reales del mercado.

Una vez disponibles los precios reales, calcularemos:

- ✅ MAPE (Mean Absolute Percentage Error) para cada modelo
- ✅ RMSE (Root Mean Squared Error)
- ✅ Dirección correcta (alcista/bajista)
- ✅ Modelo ganador

---

Referencias y Código
--------------------

El código completo para generar estas predicciones está disponible en:

🔗 **Repositorio GitHub**: https://github.com/RemiH06/Examen_2_ModelosNoLineales

📓 **Jupyter Notebook**: `Examen_2.ipynb <https://github.com/RemiH06/Examen_2_ModelosNoLineales/blob/main/Examen_2.ipynb>`_

🐍 **Script Python**: `prediccion_acciones.py <https://github.com/RemiH06/Examen_2_ModelosNoLineales/blob/main/src/prediccion_acciones.py>`_

📊 **Datos y Artefactos**: Carpeta `artifacts/`

---

Próximos Pasos
--------------

1. ⏰ **Esperar** hasta el 22 de octubre de 2025
2. 📊 **Descargar** precios reales de Yahoo Finance
3. 📈 **Calcular** métricas de error (MAPE, RMSE, MAE)
4. 🏆 **Determinar** qué modelo fue más preciso
5. 📝 **Actualizar** esta documentación con resultados finales
6. 🎓 **Analizar** qué aprendimos de las diferencias entre modelos

.. seealso::
   
   Para ver la metodología completa, consulta :doc:`metodologia`.
   
   Para conclusiones del proyecto, ve a :doc:`conclusiones`.