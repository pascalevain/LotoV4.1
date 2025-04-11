
import streamlit as st

def activer_mode_autonome_si_demande():
    st.subheader("🤖 Mode autonome")
    if st.checkbox("Activer le mode déconnecté automatique"):
        st.info("🧠 Mode autonome lancé : génération et export automatique enclenchés.")
