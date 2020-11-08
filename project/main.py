import streamlit as st
import pandas as pd

class Main:
    def __init__(self): 
        pass

    def main_page(self):
        st.markdown("# Bem vindo")
        
        st.markdown("Abaixo você encontra um dataframe")

        spotify = './datasets/spotifyclassification.csv'
        
        df_1 = pd.read_csv(spotify)
        
        st.dataframe(df_1)

        colunas = df_1.columns.unique()

        coluna_selecionada = st.selectbox(
            "Escolha a coluna",
            colunas
        )

        df_filtrado = df_1[coluna_selecionada]

        st.dataframe(df_filtrado)

        if st.checkbox("Mostrar gráficos"):
            st.bar_chart(df_filtrado)
            



if __name__ == '__main__':
    Main().main_page()