
import streamlit as st

def afficher_bouton_pdf():
    st.subheader("📄 Export PDF")
    if st.button("📥 Télécharger les grilles en PDF"):
        st.success("PDF généré (simulation).")
