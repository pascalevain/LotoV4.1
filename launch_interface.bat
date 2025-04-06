@echo off
cd /d "%~dp0"
python -m streamlit run interface_mixtral/chat_mistral_mixtral.py
pause
