import streamlit as st

def main():
    st.title("Sistema Streamlit")
    st.write("Este é um sistema de exemplo pra demonstrar o streamlit")
    st.write("Simulador de cadastro de Cliente")
    nome = st.text_input("Digite o nome")
    email = st.text_input("Digite o eMail do cliente")
    data = st.date_input("Digite a data de nascimento do cliente")

    endereco = st.text_area("Digite o endereço do cliente")
    estadocivil = st.selectbox("Selecione o estado civil", ["Solteiro",
                                "Casado", "Divorciado", "Viúvo", "União Estável"])
    
    genero = st.radio("Selecione o gênero", ["Masculino", "Feminino", "Outro"])
    if genero == "Outro":
        genero = st.text_input("Digite o gênero do cliente")
    notificacao = st.checkbox("Aceita receber notificações?")

    if st.button("Cadastrar Cliente"):
        st.success("Cliente cadastrado com sucesso!")
        st.write("Nome: ", nome)
        st.write("eMail: ", email) 
        st.write("Data de Nascimento: ", data)
        st.write("Endereço: ", endereco)
        st.write("Estado Civil: ", estadocivil)
        st.write("Gênero: ", genero)
        st.write("Notificação", notificacao)

        dados = (
            f"Nome: {nome}\r\n"
            f"eMail: {email}\r\n"
            f"Data de Nascimento: {data}\r\n"
            f"Endereço: {endereco}\r\n"
            f"Estado Civil: {estadocivil}\r\n"
            f"Gênero: {genero}\r\n"
            f"Notificação: {notificacao}\r\n"
        )

        st.download_button("Baixar Dados", dados, f"{nome}.txt")

if __name__ == "__main__":
    main()