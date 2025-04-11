
import streamlit as st

def afficher_module_strategies():
    st.subheader("📊 Stratégies de génération")
    strategie = st.selectbox("Choisir une stratégie :", ["Fréquence", "Retards", "Paires/Triplets", "Mixte"])
    if st.button("🎯 Appliquer la stratégie"):
        st.success(f"Stratégie '{strategie}' appliquée (simulation).")
