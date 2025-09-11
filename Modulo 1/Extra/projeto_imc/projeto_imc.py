import streamlit as st

# -------------------------------------------------- Sidebar

st.sidebar.image("logo.png")
st.sidebar.title("IMC(Ìdice de Massa Corporal) ")
st.sidebar.image("qualidade.png")












# ---------------------------------------------------- Principal




st.title("IMC (ídice de Massa Corporal) ")
usu =st.text_input("Nome do Usuário: ")
peso = st.text_input("Digite seu peso: ")
altura = st.text_input("Digite sua altura: ")
if st.button("calcular"):
    peso = float(peso)
    altura = float(altura)
    imc = peso / (altura ** 2)
    st.warning(F"Seu IMC é:{imc:.2f}")



    if imc <18.5 :
        st.text("Abaixo do peso,Foco em se alimentar de forma saudável,Você é mais do que seu peso!")

    elif imc <= 24.9 :
        st.text("Peso normal,Você está fazendo um ótimo trabalho em manter um peso saudável!")

    elif imc <= 29.9 :
        st.text("Sobrepeso,Você pode fazer mudanças saudáveis para melhorar sua saúde!")

    elif imc <= 34.9 :
        st.text("Obesidade Grau I,Você não está sozinho nessa jornada!Busque apoio de profissionais")

    elif imc <= 39.9 :
        st.text("Obesidade Grau II,Você é forte e capaz de superar desafios!Busque apoio de profissionais")

    else:
        st.text("Obesidade Grau III,Você merece cuidado e apoio!Busque ajuda de profissionais")





