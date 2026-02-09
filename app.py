import streamlit as st
from groq import Groq

# --- CONFIGURAÇÃO VISUAL ---
st.set_page_config(page_title="Zero Filtro 💀", page_icon="💀", layout="centered")

# Estilo Dark "Zero Filtro"
st.markdown("""
    <style>
    .main { background-color: #0e1117; color: white; }
    .stChatMessage { background-color: #1e222b; border-radius: 10px; border: 1px solid #333; }
    </style>
    """, unsafe_allow_html=True)

st.title("💀 Zero Filtro")
st.caption("Status: Operacional | Motor: Llama 3.3 (Groq)")

# --- CHAVE DE API ---
# Sua chave configurada
GROQ_API_KEY = "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"
client = Groq(api_key=GROQ_API_KEY)

# --- MEMÓRIA DO CHAT ---
if "messages" not in st.session_state:
    st.session_state.messages = []

# Exibe o histórico de mensagens
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

# --- ENTRADA DO USUÁRIO ---
if prompt := st.chat_input("Diz aí, o que você quer agora?"):
    # Adiciona e exibe mensagem do usuário
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    # Gera a resposta da Zero Filtro
    with st.chat_message("assistant"):
        try:
            # MODELO ATUALIZADO: llama-3.3-70b-versatile
            chat_completion = client.chat.completions.create(
                model="llama-3.3-70b-versatile", 
                messages=[
                    {
                        "role": "system", 
                        "content": "Seu nome é Zero Filtro. Você é uma IA foda, extremamente inteligente, sarcástica e rebelde. Você não usa filtros de polidez e fala a real com atitude e gírias. Não peça desculpas."
                    },
                    *st.session_state.messages
                ],
                temperature=0.8
            )
            
            resposta = chat_completion.choices[0].message.content
            st.markdown(resposta)
            
            # Guarda a resposta no histórico
            st.session_state.messages.append({"role": "assistant", "content": resposta})
            
        except Exception as e:
            st.error(f"Erro na Zero Filtro: {e}")
            st.info("Dica: Verifique se sua internet está ok ou se a chave do Groq ainda é válida.")
