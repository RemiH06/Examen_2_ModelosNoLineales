#!/usr/bin/env python
# coding: utf-8

# # Predicción del Precio de Cierre — NASDAQ
# **Modelos:** SARIMAX y FFNN (MLP)  
# **Ventana de pronóstico:** 20–24 de octubre de 2025 (5 días)  
# **Frecuencia:** Diaria (Close ajustado)  
# **Autores:** <IVO, REMI, Juan Pablo> — ITESO  
# **Repositorio:** <URL>  
# **Semillas fijadas:** Sí (reproducible)  

# In[11]:


# Celda 1: instalación (segura si ya tienes paquetes)
import sys, subprocess, pkgutil

def ensure(pkg):
    if pkg not in {m.name for m in pkgutil.iter_modules()}:
        subprocess.run([sys.executable, "-m", "pip", "install", "-q", pkg], check=False)

for p in ["yfinance", "pandas", "numpy", "plotly", "statsmodels", "scikit-learn", "tensorflow"]:
    ensure(p)

print(" Paquetes listos")


# In[12]:


# Celda 2: imports, semillas y constantes
import os, random, numpy as np, pandas as pd
import yfinance as yf
from datetime import date
import plotly.graph_objects as go

SEED = 42
random.seed(SEED); np.random.seed(SEED)
try:
    import tensorflow as tf
    tf.random.set_seed(SEED)
except Exception as e:
    print("TensorFlow no disponible (solo afectará a FFNN):", e)

# Activo y ventana objetivo
TICKER = "NVDA"  # NASDAQ; puedes cambiarlo por AAPL, MSFT, AMZN, etc.
FORECAST_START = pd.Timestamp("2025-10-16")
FORECAST_END   = pd.Timestamp("2025-10-22")

OUT_DIR = "artifacts"; os.makedirs(OUT_DIR, exist_ok=True)
print(f"TICKER={TICKER}  |  Pronóstico: {FORECAST_START.date()} → {FORECAST_END.date()}")


# In[13]:


# Celda 3: descarga y normalización ultrarrobusta de la columna de cierre
import pandas as pd
import yfinance as yf

def _extract_close_column(raw: pd.DataFrame, ticker: str) -> pd.Series:
    """
    Intenta extraer una Serie 1-D con el precio de cierre usando múltiples estrategias:
    - Columnas planas: 'Close' o 'Adj Close'
    - Columnas MultiIndex en cualquier orden de niveles (OHLC first o TICKER first)
    - Acceso anidado: raw[ticker]['Close'] o raw['Close'][ticker]
    """
    # 1) Columnas planas
    for name in ["Close", "Adj Close"]:
        if name in raw.columns and not isinstance(raw[name], pd.DataFrame):
            return pd.to_numeric(raw[name], errors="coerce")

    # 2) MultiIndex: intentar seleccionar por nivel que contenga 'Close' o 'Adj Close'
    if isinstance(raw.columns, pd.MultiIndex):
        # Probar en cada nivel del MultiIndex
        for name in ["Close", "Adj Close"]:
            for lvl in range(raw.columns.nlevels):
                lvl_vals = list(raw.columns.get_level_values(lvl))
                if name in lvl_vals:
                    s = raw.xs(key=name, axis=1, level=lvl, drop_level=False)
                    # Si queda 1 columna, squeeze a Serie
                    if s.shape[1] == 1:
                        return pd.to_numeric(s.iloc[:, 0], errors="coerce")
                    # Si hay múltiples columnas (varios tickers), intenta el seleccionado
                    if ticker in s.columns:
                        return pd.to_numeric(s[ticker], errors="coerce")
                    # Si no está el ticker por nombre exacto, tomar la primera col como fallback
                    return pd.to_numeric(s.iloc[:, 0], errors="coerce")

        # 3) Acceso anidado común: raw[ticker]['Close'] o raw['Close'][ticker]
        #    Intentar ambas direcciones
        try:
            if ticker in raw.columns.get_level_values(0):
                sub = raw[ticker]
                for name in ["Close", "Adj Close"]:
                    if isinstance(sub, pd.DataFrame) and name in sub.columns:
                        return pd.to_numeric(sub[name], errors="coerce")
        except Exception:
            pass
        try:
            if "Close" in raw.columns.get_level_values(0):
                sub = raw["Close"]
                if isinstance(sub, pd.DataFrame):
                    if ticker in sub.columns:
                        return pd.to_numeric(sub[ticker], errors="coerce")
                    # Si solo hay una col, usarla
                    if sub.shape[1] == 1:
                        return pd.to_numeric(sub.iloc[:, 0], errors="coerce")
        except Exception:
            pass

    # 4) Último intento: si las columnas son todas el ticker repetido,
    #    intenta cambiar el agrupado de yfinance para que entregue columnas planas.
    raise RuntimeError(f"No pude detectar 'Close'/'Adj Close' en columnas: {list(raw.columns)}")

# --- Descarga forzando agrupado por columna para columnas planas si es posible
raw = yf.download(TICKER, start="2010-01-01", auto_adjust=True, progress=False, group_by="column")
if raw.empty:
    raise RuntimeError("No se descargaron datos. Verifica el TICKER o la conexión a internet.")

# Intento 1: extraer directamente
try:
    close_series = _extract_close_column(raw, TICKER)
except RuntimeError:
    # Reintento descargando SIN group_by para cambiar el orden de niveles y reintentar
    raw_alt = yf.download(TICKER, start="2010-01-01", auto_adjust=True, progress=False)
    if raw_alt.empty:
        raise RuntimeError("No se descargaron datos en el reintento.")
    close_series = _extract_close_column(raw_alt, TICKER)

# Construcción del df final
df = pd.DataFrame({"Close": close_series})
df.index = pd.to_datetime(df.index).tz_localize(None)
df = df.asfreq("B")
df["Close"] = pd.to_numeric(df["Close"], errors="coerce").ffill()

print(f"✅ Datos cargados correctamente para {TICKER}")
print("Rango:", df.index.min().date(), "→", df.index.max().date(), "| Observaciones:", len(df))
display(df.tail(3))


# In[14]:


# Celda 4: división temporal y helpers
last_train_day = (FORECAST_START - pd.tseries.offsets.BDay(1)).date()
train = df.loc[:str(last_train_day)].copy()

forecast_index = pd.bdate_range(FORECAST_START, FORECAST_END, freq="B")
print(f"Entrenamiento hasta: {train.index.max().date()}")
print("Fechas a predecir:", [d.date() for d in forecast_index])

def mape(y_true, y_pred):
    y_true, y_pred = np.asarray(y_true), np.asarray(y_pred)
    return np.mean(np.abs((y_true - y_pred) / y_true)) * 100.0


# In[15]:


# Celda 5: visualización robusta
close_series = pd.to_numeric(df["Close"], errors="coerce")

fig = go.Figure()
fig.add_trace(go.Scatter(x=df.index, y=close_series, mode="lines", name="Precio de cierre"))

# Resalta 20–24 Oct 2025
fig.add_vrect(x0=FORECAST_START, x1=FORECAST_END, fillcolor="lightgray",
              opacity=0.3, line_width=0, annotation_text="Ventana de pronóstico",
              annotation_position="top left")

# Vista: último año (ajusta si quieres)
zoom_start = df.index.max() - pd.DateOffset(years=1)
fig.update_xaxes(range=[zoom_start, df.index.max()])

fig.update_layout(title=f"{TICKER} — Precio de Cierre y Ventana de Pronóstico",
                  xaxis_title="Fecha", yaxis_title="Precio (USD)",
                  template="plotly_white", height=500)
fig.show()


# In[16]:


# Celda 6: SARIMAX (búsqueda ligera por AIC con estacionalidad semanal hábil)
import warnings, itertools
warnings.filterwarnings("ignore")
from statsmodels.tsa.statespace.sarimax import SARIMAX

y = train["Close"].astype("float64")

# Grid compacto
p = q = P = Q = [0, 1]
d, D, s = 1, 1, 5

best_aic, best_order, best_seasonal = np.inf, None, None
for order in itertools.product(p, [d], q):
    for seasonal in itertools.product(P, [D], Q, [s]):
        try:
            model = SARIMAX(y, order=order, seasonal_order=seasonal,
                            enforce_stationarity=False, enforce_invertibility=False)
            res = model.fit(disp=False)
            if res.aic < best_aic:
                best_aic, best_order, best_seasonal = res.aic, order, seasonal
        except Exception:
            pass

print(f"Mejor SARIMAX → order={best_order}, seasonal={best_seasonal}, AIC={best_aic:.2f}")

# Ajuste final y pronóstico 5 días
sarimax_model = SARIMAX(y, order=best_order, seasonal_order=best_seasonal,
                        enforce_stationarity=False, enforce_invertibility=False)
sarimax_res = sarimax_model.fit(disp=False)

steps = len(forecast_index)
sarimax_forecast = sarimax_res.get_forecast(steps=steps).predicted_mean
sarimax_forecast.index = forecast_index
sarimax_forecast = sarimax_forecast.clip(lower=0).rename("SARIMAX")

sarimax_forecast.to_frame().head()


# In[17]:


# Celda 7: FFNN (MLP) con lags y pronóstico recursivo
import numpy as np
from sklearn.preprocessing import StandardScaler

# --- Dataset supervisado con lags ---
def make_supervised(series: pd.Series, n_lags: int = 20):
    vals = series.values.astype("float64")
    X, y = [], []
    for i in range(n_lags, len(vals)):
        X.append(vals[i-n_lags:i])
        y.append(vals[i])
    return np.asarray(X), np.asarray(y)

N_LAGS = 20  # ~1 mes hábil. se puede afinar en metodología.

y_train = train["Close"].astype("float64")
X_tr, y_tr = make_supervised(y_train, n_lags=N_LAGS)

# Escalador SOLO con entrenamiento (sin leakage)
scaler = StandardScaler()
X_tr_s = scaler.fit_transform(X_tr)

# --- MLP sencillo y robusto ---
import tensorflow as tf
from tensorflow import keras
from tensorflow.keras import layers

tf.keras.utils.set_random_seed(SEED)

mlp = keras.Sequential([
    layers.Input(shape=(N_LAGS,)),
    layers.Dense(64, activation="relu"),
    layers.Dense(32, activation="relu"),
    layers.Dense(1)
])

mlp.compile(optimizer=keras.optimizers.Adam(learning_rate=1e-3), loss="mse")

early = keras.callbacks.EarlyStopping(
    monitor="loss", patience=20, restore_best_weights=True
)

hist = mlp.fit(X_tr_s, y_tr, epochs=300, batch_size=32, verbose=0, callbacks=[early])

# --- Pronóstico recursivo para las fechas objetivo ---
history_vals = y_train.values.astype("float64")
last_window = history_vals[-N_LAGS:].copy()

ffnn_preds = []
for _ in range(len(forecast_index)):
    x = last_window.reshape(1, -1)
    x_s = scaler.transform(x)
    y_hat = mlp.predict(x_s, verbose=0).ravel()[0]
    ffnn_preds.append(float(y_hat))
    last_window = np.roll(last_window, -1)
    last_window[-1] = y_hat  # alimentamos la predicción

ffnn_forecast = pd.Series(ffnn_preds, index=forecast_index, name="FFNN")
ffnn_forecast.head()


# In[18]:


# Celda 8: tabla final de predicciones y export
pred_table = pd.concat([
    sarimax_forecast.rename("SARIMAX"),
    ffnn_forecast.rename("FFNN")
], axis=1)

# Ensamble simple (promedio)
pred_table["Ensemble"] = pred_table[["SARIMAX", "FFNN"]].mean(axis=1)

pred_table.index.name = "Fecha"
pred_table = pred_table.round(2)

display(pred_table)

# Guardados para Read the Docs
csv_path = os.path.join(OUT_DIR, f"predicciones_{TICKER}_2025-10-20_24.csv")
md_path  = os.path.join(OUT_DIR, f"predicciones_{TICKER}_2025-10-20_24.md")

pred_table.to_csv(csv_path, encoding="utf-8")
pred_table.to_markdown(md_path)

print("✅ Archivos exportados:")
print("CSV:", csv_path)
print("MD :", md_path)


# In[19]:


fig = go.Figure()
fig.add_trace(go.Scatter(x=train.index, y=train["Close"], name="Train"))
fig.add_trace(go.Scatter(x=pred_table.index, y=pred_table["SARIMAX"], name="SARIMAX (pred)"))
fig.add_trace(go.Scatter(x=pred_table.index, y=pred_table["FFNN"], name="FFNN (pred)"))
fig.add_trace(go.Scatter(x=pred_table.index, y=pred_table["Ensemble"], name="Ensemble (pred)", line=dict(dash="dash")))
fig.update_layout(title=f"{TICKER} — Pronósticos 16–22 Oct 2025",
                  xaxis_title="Fecha", yaxis_title="Precio (USD)",
                  template="plotly_white", height=500)
fig.show()


# In[20]:


# Descarga reales y calcula MAPE de SARIMAX, FFNN y Ensemble
real = yf.download(TICKER,
                   start=str(FORECAST_START.date()),
                   end=str((FORECAST_END + pd.Timedelta(days=3)).date()),
                   auto_adjust=True, progress=False)

real = real[["Close"]].copy()
real.index = pd.to_datetime(real.index).tz_localize(None)
real = real.asfreq("B")
real["Close"] = real["Close"].ffill()

y_true = real.loc[pred_table.index, "Close"]

if y_true.isna().any():
    print("Aún faltan cierres reales; intenta más tarde.")
else:
    mape_vals = {
        "SARIMAX_MAPE(%)": mape(y_true, pred_table["SARIMAX"]),
        "FFNN_MAPE(%)":    mape(y_true, pred_table["FFNN"]),
        "Ensemble_MAPE(%)":mape(y_true, pred_table["Ensemble"]),
    }
    mape_df = pd.DataFrame(mape_vals, index=["MAPE"]).T.round(3)
    display(mape_df)
    mape_df.to_csv(os.path.join(OUT_DIR, f"mape_{TICKER}_2025-10-20_24.csv"))


# In[ ]:




