import streamlit as st
import random

# Configuração da página
st.set_page_config(page_title="Sorteio Online", page_icon="🎲", layout="centered")

# Ocultar menu e rodapé do Streamlit
hide_streamlit_style = """
    <style>
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    </style>
"""
st.markdown(hide_streamlit_style, unsafe_allow_html=True)

# Estilos personalizados
st.markdown("""
    <style>
    .big-number {
        font-size: 72px;
        color: #ff4b4b;
        font-weight: bold;
        text-align: center;
    }
    .congrats {
        font-size: 36px;
        color: green;
        text-align: center;
        margin-top: 20px;
    }
    .big-text {
        font-size: 24px;
        color: #ff6347;  /* Cor vibrante: Tom de laranja/vermelho */
        font-weight: bold;
        text-align: center;
        margin-top: 20px;
    }
    </style>
""", unsafe_allow_html=True)

# Inicializa a lista de números
if 'numeros_disponiveis' not in st.session_state:
    st.session_state.numeros_disponiveis = [1, 2, 3, 4, 5]

# Interface
st.markdown("<h1 style='text-align: center;'>🎉 Sorteio Online para Inqueridores 🎉</h1>", unsafe_allow_html=True)

# Texto alterado com a classe 'big-text'
st.markdown("<p class='big-text'>Clique no botão abaixo para sortear seu número!</p>", unsafe_allow_html=True)

# Botão de sorteio
if st.button("🎲 Revelar meu número"):
    if st.session_state.numeros_disponiveis:
        numero = random.choice(st.session_state.numeros_disponiveis)
        st.session_state.numeros_disponiveis.remove(numero)
        st.balloons()
        st.markdown(f"<div class='congrats'>Parabéns! Seu número é:</div>", unsafe_allow_html=True)
        st.markdown(f"<div class='big-number'>{numero}</div>", unsafe_allow_html=True)
    else:
        st.error("⚠️ Todos os números já foram sorteados!")
