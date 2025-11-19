#  Sistema de Análise do Mercado de Trabalho Internacional

## Descrição Geral

Este projeto permite realizar análises estatísticas comparando países a
partir de dados econômico-demográficos obtidos automaticamente pela
**API do World Bank**.\
Ele foi desenvolvido para ser simples de usar, mesmo para pessoas sem
experiência em programação.

O sistema é composto por **dois arquivos principais**:

------------------------------------------------------------------------

# 1. `salvarDados.py` --- Coleta de Dados

Este arquivo:

-   Conecta à **API pública do World Bank**
-   Baixa dados reais para vários países
-   Coleta pelo menos **5 variáveis**
-   Garante dados para pelo menos **20 países**
-   Gera automaticamente os arquivos CSV dentro da pasta:

```{=html}
<!-- -->
```
    data/
        countries_data.csv
        population.csv
        gdp_per_capita.csv
        …

### Para executar:

``` bash
python salvarDados.py
```
## (Pode demorar alguns minutinhos)
------------------------------------------------------------------------

# 2. `funcoesDeAnalise.py` --- Análise e Menu Interativo

Este arquivo contém:

### Funções de análise:

-   `apresenta_pais(pais)`
-   `apresenta_dado(variavel)`
-   `calcula_media_dado(variavel)`
-   `calcula_variancia_dado(variavel)`
-   `calcula_media_ponderada(variavel, peso)`
-   `calcula_correlacao(var1, var2)`

### Menu interativo no terminal

Quando você roda:

``` bash
python funcoesDeAnalise.py
```

O programa abre um menu como este:

    =====================================================
    SISTEMA DE ANÁLISE — MERCADO DE TRABALHO INTERNACIONAL
    =====================================================

    1) Listar países disponíveis
    2) Listar variáveis disponíveis
    3) Mostrar todos os dados de um país
    4) Mostrar uma variável para todos os países
    5) Calcular média de uma variável
    6) Calcular variância de uma variável
    7) Calcular média ponderada
    8) Calcular correlação entre duas variáveis
    0) Sair

------------------------------------------------------------------------

# Como Usar o Programa

### 1. Baixe os dados

Execute:

``` bash
python salvarDados.py
```

### 2. Inicie o sistema de análise

Execute:

``` bash
python funcoesDeAnalise.py
```

### 3. Interaja com o menu

Escolha qualquer opção digitando o número desejado.

------------------------------------------------------------------------

# Exemplos de uso (no menu)

### Ver todos os países disponíveis

Opção **1**

### Ver todas as variáveis disponíveis

Opção **2**

### Ver todos os dados de um país

Opção **3**

### Ver uma variável específica

Opção **4**

### Calcular média

Opção **5**

### Calcular correlação entre duas variáveis

Opção **8**

------------------------------------------------------------------------

# Variáveis Disponíveis (preencha aqui depois de rodar o fetch)

    VARIÁVEIS DISPONÍVEIS:

    - population
    - gdp_per_capita
    - labour_force
    - employment_agriculture_pct
    - female_labor_participation
    - (adicione outras aqui)

------------------------------------------------------------------------

# Fontes dos Dados

-   https://data.worldbank.org/
-   https://api.worldbank.org/
  
------------------------------------------------------------------------

| Nome                    | RM     |
| ----------------------- | ------ |
| Kevin Carvalho Venancio | 561459 |
| Guilherme Moura Badia   | 561568 |
