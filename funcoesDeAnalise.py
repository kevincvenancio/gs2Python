import pandas as pd
import numpy as np
import os

# carregamento dataset
def load_master(path="data/countries_data.csv"):
    if not os.path.exists(path):
        print("\n ERRO: O arquivo data/countries_data.csv não existe.")
        print("➡ Rode primeiro: salvarDados.py\n")
        exit()

    return pd.read_csv(path).set_index("country")

# funcoes para exibir

def lista_paises(df=None):
    if df is None:
        df = load_master()
    return list(df.index)

def lista_dados(df=None):
    if df is None:
        df = load_master()
    return list(df.columns)

def apresenta_dado(nome_dado, df=None):
    if df is None:
        df = load_master()
    return df[nome_dado]

def apresenta_pais(nome_pais, df=None):
    if df is None:
        df = load_master()
    return df.loc[nome_pais].to_dict()

# estatiticas 

def calcula_media_dado(nome_dado, df=None):
    return apresenta_dado(nome_dado, df).mean()

def calcula_variancia_dado(nome_dado, df=None):
    return apresenta_dado(nome_dado, df).var(ddof=0)

def calcula_media_ponderada(nome_dado, peso, df=None):
    if df is None:
        df = load_master()
    valores = apresenta_dado(nome_dado, df)
    pesos = apresenta_dado(peso, df)
    return (valores * pesos).sum() / pesos.sum()

def calcula_correlacao(var_x, var_y, df=None):
    if df is None:
        df = load_master()
    return df[var_x].corr(df[var_y])

#MENU

def mostrar_menu():
    print("""
=====================================================
SISTEMA DE ANÁLISE — MERCADO DE TRABALHO INTERNACIONAL
=====================================================

Escolha uma opção:

1) Listar países disponíveis
2) Listar variáveis disponíveis
3) Mostrar todos os dados de um país
4) Mostrar uma variável para todos os países
5) Calcular média de uma variável
6) Calcular variância de uma variável
7) Calcular média ponderada
8) Calcular correlação entre duas variáveis
0) Sair
""")


def executar_menu():
    df = load_master()

    while True:
        mostrar_menu()
        opc = input("Digite a opção desejada: ").strip()

        #sair
        if opc == "0":
            print("\nEncerrando... Obrigado!\n")
            break

        #listar paises
        elif opc == "1":
            print("\n Países disponíveis:\n")
            for p in lista_paises(df):
                print("-", p)

        #listar
        elif opc == "2":
            print("\n Variáveis disponíveis:\n")
            for v in lista_dados(df):
                print("-", v)

        #mostrar dados de um pais
        elif opc == "3":
            nome = input("\nDigite o nome do país exatamente como aparece na lista: ")
            try:
                print("\nDados do país:\n", apresenta_pais(nome, df), "\n")
            except:
                print("\n País inválido.\n")

        #mostrar uma variavel
        elif opc == "4":
            var = input("\nDigite o nome da variável: ")
            try:
                print("\nValores:\n", apresenta_dado(var, df), "\n")
            except:
                print("\n Variável inválida.\n")

        #media
        elif opc == "5":
            var = input("\nVariável: ")
            try:
                print("\nMédia =", calcula_media_dado(var, df), "\n")
            except:
                print("\n Variável inválida.\n")

        #variancia
        elif opc == "6":
            var = input("\nVariável: ")
            try:
                print("\nVariância =", calcula_variancia_dado(var, df), "\n")
            except:
                print("\n Variável inválida.\n")

        #media ponderada
        elif opc == "7":
            var = input("\nVariável: ")
            peso = input("Peso (ex.: population): ")
            try:
                print("\nMédia ponderada =", calcula_media_ponderada(var, peso, df), "\n")
            except:
                print("\n Variável ou peso inválido.\n")

        #correlação
        elif opc == "8":
            x = input("\nPrimeira variável: ")
            y = input("Segunda variável: ")
            try:
                print("\nCorrelação =", calcula_correlacao(x, y, df), "\n")
            except:
                print("\n Variáveis inválidas.\n")

        else:
            print("\n Opção inválida.\n")


# execuçao automatica

if __name__ == "__main__":
    executar_menu()