import streamlit as st

def afficher_module_generation_grilles():
    st.markdown("## 🎯 Génération automatique de grilles optimisées")

    # Sélection du mode
    mode = st.radio("Mode de génération :", ["🌿 Manuel", "🚀 Automatique (sans confirmation)"], key="mode_generation_unique")

    st.session_state["mode_generation"] = mode

    # Choix du nombre de grilles
    nb_grilles = st.number_input("🔢 Nombre de grilles à générer :", min_value=1, max_value=100, value=5, step=1)

    # Bouton de génération
    if st.button("⚙️ Lancer la génération des grilles"):
        st.success(f"✅ Génération de {nb_grilles} grille(s) en mode : {mode}")
        if mode == "🚀 Automatique (sans confirmation)":
            st.info("📁 Enregistrement, traitement IA et export automatique à venir…")
        else:
            st.info("👀 Affichage des grilles en cours, sélection manuelle possible…")
