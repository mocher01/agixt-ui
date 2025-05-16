import streamlit as st
from agixtsdk import AGiXTSDK
import os

backend_uri = os.getenv("BACKEND_URI", "http://localhost:7437")
client = AGiXTSDK(base_uri=backend_uri, api_key="")

st.title("AGiXT Interface")

query = st.text_input("Message à envoyer à l’agent")
agent = st.text_input("Nom de l’agent", value="default")

if st.button("Envoyer"):
    try:
        response = client.agent.prompt(agent_name=agent, prompt_name="Chat", user_input=query)
        st.success(response)
    except Exception as e:
        st.error(f"Erreur AGiXT : {e}")
