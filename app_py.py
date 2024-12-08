# -*- coding: utf-8 -*-
"""app.py

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/13g2Zp-RtIG17Y_UDOc7uolztEArNcI0O
"""

!pip install streamlit
!pip install pyngrok

import streamlit as st
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report, confusion_matrix, ConfusionMatrixDisplay
import seaborn as sns
import matplotlib.pyplot as plt
import warnings

# Turn off warnings
warnings.filterwarnings('ignore')

# App Title
st.title("Bankruptcy Prevention Model Deployment")
st.sidebar.header("Settings")

# Sidebar: Upload CSV
uploaded_file = st.sidebar.file_uploader("/content/data.csv", type=["csv"])

if uploaded_file:
    # Load dataset
    df = pd.read_csv(uploaded_file)
    st.write("### Data Preview")
    st.dataframe(df.head())

    # Select Target Variable
    target_column = st.sidebar.selectbox("Select Target Column", df.columns, index=0)
    features = [col for col in df.columns if col != target_column]

    # Data Info
    st.write("### Data Information")
    st.write("Number of rows: ", df.shape[0])
    st.write("Number of columns: ", df.shape[1])

    # Data Description
    st.write("### Dataset Summary")
    st.write(df.describe())

    # Preprocessing: Handle missing values
    if st.sidebar.checkbox("Fill Missing Values"):
        df.fillna(0, inplace=True)
        st.write("Missing values have been filled.")

    # Data Visualization
    st.write("### Feature Distribution")
    selected_column = st.selectbox("Select a Column to Visualize", features)
    fig, ax = plt.subplots()
    sns.histplot(df[selected_column], kde=True, ax=ax)
    st.pyplot(fig)

    # Model Parameters
    st.sidebar.subheader("Model Parameters")
    test_size = st.sidebar.slider("Test Size", 0.1, 0.5, 0.2)
    n_estimators = st.sidebar.slider("Number of Estimators", 10, 200, 100)

    # Model Training
    if st.sidebar.button("Train Model"):
        st.write("### Model Training")
        X = df[features]
        y = df[target_column]

        # Split data
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=test_size, random_state=42)

        # Train Random Forest Classifier
        model = RandomForestClassifier(n_estimators=n_estimators, random_state=42)
        model.fit(X_train, y_train)
        y_pred = model.predict(X_test)

        # Evaluation
        st.write("Classification Report")
        st.text(classification_report(y_test, y_pred))

        # Confusion Matrix
        st.write("Confusion Matrix")
        fig, ax = plt.subplots()
        ConfusionMatrixDisplay.from_estimator(model, X_test, y_test, ax=ax)
        st.pyplot(fig)

        # Feature Importance
        st.write("### Feature Importance")
        feature_importances = pd.Series(model.feature_importances_, index=features).sort_values(ascending=False)
        st.bar_chart(feature_importances)

