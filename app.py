import streamlit as st
import pandas as pd
import numpy as np

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LinearRegression

# ==========================================================
# PAGE CONFIG
# ==========================================================
st.set_page_config(
    page_title="💼 Salary Prediction App",
    layout="wide",
    page_icon="💰"
)

# ==========================================================
# CUSTOM STYLING
# ==========================================================
st.markdown(
    """
    <style>
        /* Background gradient */
        .main {
            background: linear-gradient(145deg, #141E30 0%, #243B55 100%);
        }

        /* Text */
        h1, h2, h3, h4, h5, h6, div, p {
            color: #f1f1f1 !important;
            font-family: 'Segoe UI', sans-serif;
        }

        /* Card design */
        .block-container {
            padding-top: 2rem;
        }

        .card {
            background: rgba(255, 255, 255, 0.07);
            padding: 20px;
            border-radius: 15px;
            border: 1px solid rgba(255,255,255,0.1);
            backdrop-filter: blur(10px);
        }

        /* Prediction text */
        .prediction-box {
            background: rgba(0, 255, 150, 0.15);
            border-left: 5px solid #00ff9d;
            padding: 15px;
            border-radius: 10px;
            font-size: 1.3rem;
        }

        /* Button styling */
        .stButton>button {
            background-color: #00BFFF;
            color: white;
            border-radius: 10px;
            padding: 0.6rem 1.2rem;
            border: none;
        }

        .stButton>button:hover {
            background-color: #009acd;
            transform: scale(1.03);
        }

    </style>
    """,
    unsafe_allow_html=True
)

# ==========================================================
# HEADER
# ==========================================================
st.markdown(
    """
    <h1 style='text-align:center; font-size: 3rem; margin-bottom: 0;'>
    💼 Salary Prediction App
    </h1>
    <p style='text-align:center; font-size: 1.2rem;'>
        Powered by D05 Batch ML Team
    </p>
    """,
    unsafe_allow_html=True
)

# ==========================================================
# LOAD DATA
# ==========================================================
@st.cache_data
def load_data():
    df = pd.read_csv("salaries.csv")
    return df

try:
    df = load_data()
except:
    st.error("❌ salaries.csv not found. Place it next to app.py and restart.")
    st.stop()

# ==========================================================
# TRAIN MODEL (FROM .ipynb LOGIC)
# ==========================================================
def train_model(df):
    X = df.drop(columns=['salary_in_usd'])
    y = df['salary_in_usd']

    X = pd.get_dummies(X)

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.20, random_state=42
    )

    scaler = StandardScaler()
    X_train_scaled = scaler.fit_transform(X_train)
    X_test_scaled = scaler.transform(X_test)

    model = LinearRegression()
    model.fit(X_train_scaled, y_train)

    return model, scaler, X

model, scaler, X_matrix = train_model(df)

# ==========================================================
# SIDEBAR
# ==========================================================
st.sidebar.title("⚙ Controls")
st.sidebar.info("Adjust inputs and press *Predict Salary*")

# ==========================================================
# FEATURE INPUT UI
# ==========================================================
st.markdown("<div class='card'>", unsafe_allow_html=True)
st.subheader("🔧 Enter Employee Details")

input_values = {}
original_columns = df.drop(columns=['salary_in_usd']).columns

cols = st.columns(2)

for i, col in enumerate(original_columns):
    with cols[i % 2]:
        if df[col].dtype in [np.float64, np.int64]:
            input_values[col] = st.number_input(
                f"{col}",
                min_value=float(df[col].min()),
                max_value=float(df[col].max()),
                value=float(df[col].median())
            )
        else:
            choices = sorted(df[col].unique().tolist())
            input_values[col] = st.selectbox(f"{col}", choices)

st.markdown("</div>", unsafe_allow_html=True)

# ==========================================================
# PREDICT
# ==========================================================
if st.button("🚀 Predict Salary"):
    input_df = pd.DataFrame([input_values])
    input_df = pd.get_dummies(input_df)

    for col in X_matrix.columns:
        if col not in input_df.columns:
            input_df[col] = 0

    input_df = input_df[X_matrix.columns]
    input_scaled = scaler.transform(input_df)
    prediction = model.predict(input_scaled)[0]

    st.balloons()
    
    st.markdown(
        f"""
        <div class='prediction-box'>
        <strong>Estimated Salary:</strong> ₹ {prediction:,.2f}
        </div>
        """,
        unsafe_allow_html=True
    )

# Footer
st.markdown(
    """
    <hr>
    <p style='text-align:center; font-size: 0.9rem;'>Created with ❤ in Streamlit</p>
    """,
    unsafe_allow_html=True
)