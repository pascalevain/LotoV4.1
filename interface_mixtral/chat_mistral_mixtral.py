import streamlit as st
import requests

st.set_page_config(page_title="Chat Loto IA - Mistral / Mixtral")
st.title("💬 Assistant IA Loto V4.1")

model = st.selectbox("Choisir le modèle :", ["mistral", "mixtral"])
message = st.text_area("Votre message :")
uploaded_file = st.file_uploader("Ou charge un fichier à analyser (TXT, CSV, PY, etc.)")

if uploaded_file is not None:
    try:
        file_text = uploaded_file.read().decode("utf-8")
        st.text_area("Contenu du fichier :", file_text, height=200)
    except Exception as e:
        st.error(f"Erreur lors de la lecture du fichier : {e}")

if st.button("Envoyer à l'IA"):
    if not message and not uploaded_file:
        st.warning("Veuillez entrer un message ou fournir un fichier.")
    else:
        prompt = message + "\n" + file_text if uploaded_file else message
        with st.spinner("L'IA réfléchit..."):
            try:
                response = requests.post(
                    f"http://localhost:11434/api/generate",
                    json={"model": model, "prompt": prompt, "stream": False})
                if response.status_code == 200:
                    result = response.json()
                    st.success("Réponse de l'IA :")
                    st.markdown(result["response"])
                else:
                    st.error("Erreur lors de l'appel à l'IA.")
            except Exception as e:
                st.error(f"Erreur de connexion à Ollama : {e}")