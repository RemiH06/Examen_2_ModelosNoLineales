Metodología
===========

Esta sección detalla la metodología completa utilizada para construir y evaluar los modelos SARIMAX y FFNN.

Pipeline General del Proyecto
------------------------------

.. code-block:: text

   1. Descarga de datos (yfinance)
          ↓
   2. Análisis exploratorio (EDA)
          ↓
   3. Pruebas de estacionariedad
          ↓
   4. Preparación de datos (train/test/future)
          ↓
   5. Entrenamiento de modelos
          ↓
   6. Evaluación y comparación
          ↓
   7. Predicciones finales (5 días)

---

Modelo 1: SARIMAX
-----------------

**SARIMAX** significa *Seasonal AutoRegressive Integrated Moving Average with eXogenous variables*.

Estructura del Modelo
~~~~~~~~~~~~~~~~~~~~~

Un modelo SARIMAX se define por dos conjuntos de órdenes:

**Componente No Estacional: (p, d, q)**

- **p**: Orden autoregresivo (AR) - número de lags de la variable dependiente
- **d**: Grado de diferenciación (I) - veces que se diferencia la serie
- **q**: Orden de media móvil (MA) - número de lags de los errores

**Componente Estacional: (P, D, Q, s)**

- **P**: Orden autoregresivo estacional
- **D**: Diferenciación estacional
- **Q**: Media móvil estacional
- **s**: Periodo estacional (e.g., 5 para días de la semana, 12 para meses)

Ecuación General
~~~~~~~~~~~~~~~~

.. math::

   \Phi_P(B^s)\phi_p(B)\nabla^D_s\nabla^d Y_t = \Theta_Q(B^s)\theta_q(B)\epsilon_t

Donde:

- :math:`Y_t`: Serie temporal en el tiempo t
- :math:`B`: Operador de retardo (lag)
- :math:`\nabla`: Operador de diferenciación
- :math:`\epsilon_t`: Error o ruido blanco

Selección de Órdenes
~~~~~~~~~~~~~~~~~~~~

Para determinar los valores óptimos de (p, d, q) y (P, D, Q, s):

1. **Diferenciación (d)**
   
   - Aplicar prueba ADF (Augmented Dickey-Fuller)
   - Si p-value > 0.05 → serie NO estacionaria → aumentar d
   - Confirmar con prueba KPSS

2. **Órdenes AR y MA (p, q)**
   
   - Analizar gráficas ACF (Autocorrelation Function)
   - Analizar gráficas PACF (Partial Autocorrelation Function)
   - Reglas empíricas:
     
     - Si ACF decae lentamente → componente AR significativo
     - Si PACF corta en lag k → p = k
     - Si ACF corta en lag k → q = k

3. **Componente Estacional (P, D, Q, s)**
   
   - Observar patrones repetitivos en ACF/PACF
   - Para acciones: s = 5 (semana bursátil) o s = 21 (mes aproximado)

4. **Criterios de Información**
   
   - **AIC** (Akaike Information Criterion): penaliza complejidad
   - **BIC** (Bayesian Information Criterion): penaliza más fuertemente
   - Menor AIC/BIC → mejor modelo

Configuración Final
~~~~~~~~~~~~~~~~~~~

Basado en el análisis exploratorio, seleccionamos:

.. code-block:: python

   order = (1, 1, 1)           # (p, d, q)
   seasonal_order = (1, 1, 1, 5)  # (P, D, Q, s)

**Justificación:**

- **d=1**: Una diferenciación es suficiente para estacionariedad
- **p=1, q=1**: Patrones simples en ACF/PACF
- **s=5**: Ciclo semanal (5 días hábiles)
- **P=1, D=1, Q=1**: Estacionalidad moderada

Criterios de Validación
~~~~~~~~~~~~~~~~~~~~~~~~

- ✅ Residuos deben ser ruido blanco (Ljung-Box test)
- ✅ AIC y BIC minimizados
- ✅ Predicciones estables (sin explosión)

---

Modelo 2: FFNN (Feed-Forward Neural Network)
---------------------------------------------

Una **FFNN** es una red neuronal artificial donde la información fluye en una sola dirección (sin ciclos).

Arquitectura de la Red
~~~~~~~~~~~~~~~~~~~~~~

Nuestra FFNN tiene la siguiente estructura:

.. code-block:: text

   Input Layer (lookback días)
         ↓
   Dense(128) + ReLU + L2(0.0001) + Dropout(0.1)
         ↓
   Dense(64) + ReLU + L2(0.0001) + Dropout(0.2)
         ↓
   Dense(32) + ReLU + L2(0.00001) + Dropout(0.1)
         ↓
   Dense(16) + ReLU
         ↓
   Output Layer: Dense(1) - Predicción del precio

**Número total de capas**: 5 (4 ocultas + 1 salida)

Hiperparámetros Seleccionados
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. list-table::
   :header-rows: 1
   :widths: 30 30 40

   * - Hiperparámetro
     - Valor
     - Justificación
   * - **Lookback**
     - 20 días
     - Balance entre memoria histórica y overfitting
   * - **Capas ocultas**
     - 4
     - Suficiente profundidad sin complejidad excesiva
   * - **Neuronas (L1)**
     - 128
     - Capa ancha para capturar patrones iniciales
   * - **Neuronas (L2)**
     - 64
     - Reducción progresiva (pirámide)
   * - **Neuronas (L3)**
     - 32
     - Extracción de features de alto nivel
   * - **Neuronas (L4)**
     - 16
     - Consolidación final antes de salida
   * - **Función de activación**
     - ReLU
     - Previene vanishing gradient, computacionalmente eficiente
   * - **Regularización L2**
     - [1e-4, 1e-5, 1e-6]
     - Previene overfitting en pesos grandes
   * - **Dropout**
     - [0.1, 0.2]
     - Desactiva neuronas aleatoriamente (generalización)
   * - **Learning rate**
     - 0.001
     - Tasa estándar para Adam optimizer
   * - **Batch size**
     - 32
     - Balance entre velocidad y estabilidad
   * - **Epochs**
     - 100 (con Early Stopping)
     - Suficiente para convergencia

Función de Activación: ReLU
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. math::

   f(x) = \max(0, x)

**Ventajas:**

- No saturación en valores positivos
- Derivada simple (0 o 1)
- Computacionalmente eficiente

Regularización
~~~~~~~~~~~~~~

**1. L2 Regularization (Ridge)**

Añade penalización a la función de pérdida:

.. math::

   L_{total} = L_{MSE} + \lambda \sum_{i} w_i^2

Esto previene que los pesos crezcan excesivamente.

**2. Dropout**

Durante entrenamiento, "apaga" aleatoriamente un porcentaje de neuronas en cada iteración.

- **Efecto**: Fuerza redundancia en la red
- **Resultado**: Mejor generalización al test set

Optimizador: Adam
~~~~~~~~~~~~~~~~~

**Adam** (Adaptive Moment Estimation) combina las ventajas de AdaGrad y RMSprop.

**Actualización de pesos:**

.. math::

   m_t = \beta_1 m_{t-1} + (1-\beta_1) g_t
   
   v_t = \beta_2 v_{t-1} + (1-\beta_2) g_t^2
   
   w_t = w_{t-1} - \alpha \frac{m_t}{\sqrt{v_t} + \epsilon}

Donde:

- :math:`m_t`: Primer momento (media de gradientes)
- :math:`v_t`: Segundo momento (varianza de gradientes)
- :math:`\alpha`: Learning rate (0.001)
- :math:`\beta_1, \beta_2`: Tasas de decaimiento (0.9, 0.999)

**Ventajas de Adam:**

✅ Adaptación individual de learning rate por parámetro

✅ Funciona bien con gradientes ruidosos

✅ Requiere poca tunning manual

Walk-Forward Validation
~~~~~~~~~~~~~~~~~~~~~~~

Para predicciones de múltiples días, usamos un enfoque de **rolling window**:

.. code-block:: text

   Día 1: Usar ventana [t-20:t] → Predecir t+1
   Día 2: Usar ventana [t-19:t+1] → Predecir t+2
   Día 3: Usar ventana [t-18:t+2] → Predecir t+3
   ...

Este método simula condiciones reales de trading.

Early Stopping
~~~~~~~~~~~~~~

Implementamos Early Stopping para prevenir overfitting:

.. code-block:: python

   EarlyStopping(
       monitor='val_loss',    # Vigilar pérdida en validación
       patience=15,           # Esperar 15 epochs sin mejora
       restore_best_weights=True  # Regresar a mejor modelo
   )

Si la pérdida en validación no mejora en 15 epochs consecutivos, el entrenamiento se detiene.

---

Preprocesamiento de Datos
--------------------------

Escalado con MinMaxScaler
~~~~~~~~~~~~~~~~~~~~~~~~~~

Para la FFNN, escalamos los datos al rango [0, 1]:

.. math::

   X_{scaled} = \frac{X - X_{min}}{X_{max} - X_{min}}

**Razones:**

1. Convergencia más rápida del optimizador
2. Evita dominancia de features con mayor magnitud
3. Previene problemas numéricos (overflow/underflow)

**Importante:** El scaler se ajusta SOLO con datos de entrenamiento para evitar data leakage.

División de Datos
~~~~~~~~~~~~~~~~~

.. code-block:: python

   Total de datos: ~500 días (2 años)
   
   Train: 470 días (94%)
   Test:   30 días (6%)
   Future:  5 días (predicción)

**Train Set:** Para entrenar los modelos

**Test Set:** Para evaluar performance antes de predicción final

**Future Set:** Predicciones objetivo (20-24 octubre 2025)

Creación de Secuencias
~~~~~~~~~~~~~~~~~~~~~~

Para la FFNN, transformamos datos de serie temporal en pares (X, y):

.. code-block:: python

   # Ejemplo con lookback=3
   Precios: [100, 102, 105, 108, 110, 112]
   
   Secuencias:
   X=[100, 102, 105] → y=108
   X=[102, 105, 108] → y=110
   X=[105, 108, 110] → y=112

Esto permite a la red aprender patrones históricos.

---

Métricas de Evaluación
-----------------------

Para comparar ambos modelos, usamos tres métricas estándar:

1. RMSE (Root Mean Squared Error)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. math::

   RMSE = \sqrt{\frac{1}{n}\sum_{i=1}^{n}(y_i - \hat{y}_i)^2}

- **Unidad**: Misma que la variable (dólares)
- **Interpretación**: Error promedio en predicciones
- **Sensible a outliers**: Penaliza errores grandes

2. MAE (Mean Absolute Error)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. math::

   MAE = \frac{1}{n}\sum_{i=1}^{n}|y_i - \hat{y}_i|

- **Unidad**: Dólares
- **Interpretación**: Error absoluto promedio
- **Más robusto** a outliers que RMSE

3. MAPE (Mean Absolute Percentage Error)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. math::

   MAPE = \frac{100}{n}\sum_{i=1}^{n}\left|\frac{y_i - \hat{y}_i}{y_i}\right|

- **Unidad**: Porcentaje (%)
- **Interpretación**: Error relativo promedio
- **Ventaja**: Independiente de la escala del precio

Criterios de Éxito
~~~~~~~~~~~~~~~~~~

Un modelo se considera "bueno" si:

- ✅ RMSE < $10 (para acciones ~$100-500)
- ✅ MAE < $7
- ✅ MAPE < 5%
- ✅ Predicciones estables (sin saltos abruptos)

---

Reproducibilidad
----------------

Para garantizar que los resultados sean reproducibles:

Semilla Fija
~~~~~~~~~~~~

.. code-block:: python

   SEED = 42
   
   np.random.seed(SEED)
   tf.random.set_seed(SEED)
   random.seed(SEED)

Esto asegura que:

- División train/test sea idéntica
- Inicialización de pesos de FFNN sea consistente
- Dropout y shuffle sean determinísticos

Control de Versiones
~~~~~~~~~~~~~~~~~~~~~

Todas las dependencias tienen versiones fijas en ``requirements.txt``:

.. code-block:: text

   tensorflow==2.13.0
   statsmodels==0.14.0
   numpy==1.24.3
   ...

Entorno de Ejecución
~~~~~~~~~~~~~~~~~~~~

- **Python**: 3.8+
- **Sistema**: Compatible con Linux, macOS, Windows
- **Hardware**: CPU suficiente (GPU opcional para FFNN)

---

Limitaciones y Consideraciones
-------------------------------

Limitaciones del Proyecto
~~~~~~~~~~~~~~~~~~~~~~~~~~

1. **Horizonte corto**: Solo 5 días (dificultad aumenta exponencialmente)
2. **Datos históricos únicamente**: No incorpora noticias o sentimiento
3. **Eventos imprevistos**: No puede anticipar anuncios sorpresa
4. **Suposición de mercado eficiente**: Los patrones del pasado pueden cambiar

Supuestos del Modelo
~~~~~~~~~~~~~~~~~~~~

- 📊 Los datos históricos contienen información predictiva
- 📅 Los patrones temporales son relativamente estables
- 💹 No hay cambios estructurales drásticos durante predicción
- 🔄 Los mercados operan normalmente (no crisis inesperadas)

Consideraciones Éticas
~~~~~~~~~~~~~~~~~~~~~~~

- ⚠️ Este proyecto es **académico**, no constituye asesoría financiera
- ⚠️ No debe usarse para decisiones reales de inversión sin análisis adicional
- ⚠️ Los mercados financieros son inherentemente impredecibles

---

Resumen de la Metodología
--------------------------

.. list-table::
   :header-rows: 1
   :widths: 25 35 40

   * - Aspecto
     - SARIMAX
     - FFNN
   * - **Tipo de modelo**
     - Estadístico paramétrico
     - Aprendizaje profundo
   * - **Hiperparámetros clave**
     - (p,d,q), (P,D,Q,s)
     - Capas, neuronas, dropout, LR
   * - **Preprocesamiento**
     - Diferenciación
     - Escalado MinMax
   * - **Ventajas**
     - Interpretable, teóricamente fundamentado
     - Captura no linealidades complejas
   * - **Desventajas**
     - Asume linealidad, estacionariedad
     - Caja negra, requiere muchos datos
   * - **Tiempo de entrenamiento**
     - Rápido (~segundos)
     - Moderado (~minutos)

Ambos modelos son complementarios y su comparación permite evaluar si métodos estadísticos clásicos o deep learning son más efectivos para este problema específico.