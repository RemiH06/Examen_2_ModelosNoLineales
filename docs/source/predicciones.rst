Predicciones
============

Esta página contiene las predicciones oficiales de los modelos SARIMAX, FFNN y Ensemble para los días **20-24 de octubre de 2025**.

.. note::
   Las predicciones se generaron el **16 de octubre de 2025** utilizando datos históricos hasta el **15 de octubre de 2025**.
   Todos los valores están en dólares estadounidenses (USD).

---

Tabla de Predicciones Oficiales
--------------------------------

.. csv-table:: Predicciones NVDA - Octubre 20-24, 2025
   :header: "Fecha", "SARIMAX ($)", "FFNN ($)", "Ensemble ($)", "Confianza"
   :widths: 20, 20, 20, 20, 20
   :align: center

   "2025-10-20", "179.57", "170.54", "175.05", "Alta"
   "2025-10-21", "179.79", "167.79", "173.79", "Alta"
   "2025-10-22", "180.28", "165.93", "173.1", "Media"
   "2025-10-23", "180.28", "165.93", "173.1", "Media"
   "2025-10-24", "180.28", "165.93", "173.1", "Media-Baja"

.. important::
   **Confianza** se refiere a la certidumbre estadística de la predicción:
   
   - **Alta**: Horizonte cercano (1-2 días)
   - **Media**: Horizonte medio (3-4 días)
   - **Baja**: Horizonte lejano (5+ días)

---

Detalles por Modelo
--------------------

Predicciones SARIMAX
~~~~~~~~~~~~~~~~~~~~

El modelo SARIMAX generó las siguientes predicciones con sus intervalos de confianza:

.. list-table::
   :header-rows: 1
   :widths: 20 20 25 25

   * - Fecha
     - Predicción
     - IC 95% Inferior
     - IC 95% Superior
   * - 2025-10-20
     - $179.57
     - $XXX.XX
     - $XXX.XX
   * - 2025-10-21
     - $179.79
     - $XXX.XX
     - $XXX.XX
   * - 2025-10-22
     - $180.28
     - $XXX.XX
     - $XXX.XX
   * - 2025-10-23
     - $180.28
     - $XXX.XX
     - $XXX.XX
   * - 2025-10-24
     - $180.28
     - $XXX.XX
     - $XXX.XX

**Características de las Predicciones SARIMAX:**

- ✅ Incluye intervalos de confianza (ventaja sobre FFNN)
- ✅ Captura tendencias lineales y estacionalidad
- ⚠️ Puede subestimar cambios abruptos
- ⚠️ Los intervalos se amplían con el horizonte

Predicciones FFNN
~~~~~~~~~~~~~~~~~

El modelo de red neuronal generó estas predicciones:

.. list-table::
   :header-rows: 1
   :widths: 20 20 30 30

   * - Fecha
     - Predicción
     - Cambio vs día anterior
     - Cambio porcentual
   * - 2025-10-20
     - $170.54
     - +$X.XX
     - +X.XX%
   * - 2025-10-21
     - $167.79
     - +$X.XX
     - +X.XX%
   * - 2025-10-22
     - $165.93
     - -$X.XX
     - -X.XX%
   * - 2025-10-23
     - $165.93
     - +$X.XX
     - +X.XX%
   * - 2025-10-24
     - $165.93
     - +$X.XX
     - +X.XX%

**Características de las Predicciones FFNN:**

- ✅ Captura patrones no lineales complejos
- ✅ Puede anticipar cambios bruscos
- ⚠️ No proporciona intervalos de confianza nativos
- ⚠️ Más sensible a datos recientes

---

Consenso y Estrategia
---------------------

Predicción Ensamblada
~~~~~~~~~~~~~~~~~~~~~~

El **promedio simple** de ambos modelos suele ofrecer mejor robustez:

.. code-block:: python

   Predicción_final = (SARIMAX + FFNN) / 2

**Ventajas del ensamble:**

1. Reduce el sesgo individual de cada modelo
2. Promedia errores aleatorios
3. Más estable que predicciones individuales

Señales de Trading (Ilustrativo)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. warning::
   Esto es **solo ilustrativo** y no constituye recomendación de inversión.

Basado en las predicciones:

.. list-table::
   :header-rows: 1
   :widths: 20 20 30 30

   * - Fecha
     - Precio Estimado
     - Tendencia
     - Señal Indicativa
   * - 2025-10-20
     - $175.05
     - ↗️ Alcista
     - HOLD / BUY
   * - 2025-10-21
     - $173.79
     - ↗️ Alcista
     - HOLD
   * - 2025-10-22
     - $173.10
     - ➡️ Lateral
     - HOLD
   * - 2025-10-23
     - $173.10
     - ↘️ Bajista
     - HOLD / CAUTION
   * - 2025-10-24
     - $173.10
     - ➡️ Lateral
     - HOLD

---

Contexto de Mercado
-------------------

Factores a Considerar
~~~~~~~~~~~~~~~~~~~~~

Al interpretar estas predicciones, considerar:

**Factores Internos (NVIDIA)**

- 📊 Próximos reportes de ganancias (earnings)
- 🚀 Lanzamientos de productos (e.g., nuevas GPUs)
- 👔 Cambios en dirección ejecutiva
- 📰 Anuncios de alianzas estratégicas

**Factores Externos (Mercado)**

- 📈 Tendencia del NASDAQ y S&P 500
- 💵 Decisiones de la Reserva Federal (tasas de interés)
- 🌍 Tensiones geopolíticas (e.g., China-Taiwan)
- 🤖 Sentimiento general sobre IA y tecnología

**Factores Técnicos**

- 📉 Niveles de soporte: $XXX, $XXX
- 📈 Niveles de resistencia: $XXX, $XXX
- 📊 Volumen de trading reciente
- 🔄 Índices técnicos (RSI, MACD, Bollinger Bands)

Eventos Programados
~~~~~~~~~~~~~~~~~~~

Durante el periodo de predicción (20-24 octubre 2025):

.. list-table::
   :header-rows: 1
   :widths: 30 70

   * - Fecha
     - Evento Potencial
   * - Lunes 20
     - Apertura semanal, posible reacción a noticias del fin de semana
   * - Martes 21
     - [Verificar calendario económico]
   * - Miércoles 22
     - [Verificar si hay earnings de empresas relacionadas]
   * - Jueves 23
     - [Posibles anuncios de Fed o datos macroeconómicos]
   * - Viernes 24
     - Cierre semanal, ajuste de posiciones antes del fin de semana

---

Comparación con Analistas
--------------------------

.. note::
   Sección a completar después de la predicción real.

Estimaciones de Wall Street (si disponibles):

- **Precio objetivo promedio**: $XXX.XX
- **Precio objetivo máximo**: $XXX.XX
- **Precio objetivo mínimo**: $XXX.XX
- **Número de analistas**: XX

**Comparación:**

- Nuestro modelo SARIMAX: **[X% diferencia]**
- Nuestro modelo FFNN: **[X% diferencia]**
- Promedio ensamblado: **[X% diferencia]**

---

Actualización Post-Predicción
------------------------------

.. attention::
   Esta sección se actualizará después del 24 de octubre de 2025 con los valores reales.

Valores Reales Observados
~~~~~~~~~~~~~~~~~~~~~~~~~~

.. csv-table:: Comparación: Predicción vs Real
   :header: "Fecha", "Real ($)", "SARIMAX ($)", "FFNN ($)", "Error SARIMAX", "Error FFNN"
   :widths: 15, 17, 17, 17, 17, 17

   "2025-10-20", "---", "179.57", "170.54", "---", "---"
   "2025-10-21", "---", "179.79", "167.79", "---", "---"
   "2025-10-22", "---", "180.28", "165.93", "---", "---"
   "2025-10-23", "---", "180.28", "165.93", "---", "---"
   "2025-10-24", "---", "180.28", "165.93", "---", "---"

*(Pendiente de actualización)*

---

Descarga de Datos
-----------------

Las predicciones están disponibles para descarga en varios formatos:

📄 **CSV**: `predictions_nvda_oct2025.csv <_static/predictions_nvda_oct2025.csv>`_

📊 **Excel**: `predictions_nvda_oct2025.xlsx <_static/predictions_nvda_oct2025.xlsx>`_

📋 **JSON**: `predictions_nvda_oct2025.json <_static/predictions_nvda_oct2025.json>`_

Formato del archivo CSV:

.. code-block:: text

   date,pred_close_sarimax,pred_close_ffnn,pred_close_ensemble
   2025-10-20,179.57,170.54,175.05
   2025-10-21,179.79,167.79,173.79
   ...

---

Referencias y Código
--------------------

El código completo para generar estas predicciones está disponible en:

🔗 `GitHub Repository <>`_

📓 `Jupyter Notebook <>`_

🐍 `Script Python <>`_
