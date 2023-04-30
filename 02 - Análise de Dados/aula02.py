import pandas as pd;

def display(tabela):
    tb = tabela.__str__();
    arq.write(tb);
    arq.write("\n======================================================================\n\n")

#---------
#  MAIN:
#---------
arq = open("tabela.txt", "w+");

# ----------------------- Passo 01: Importanto a Base de Dados
tabela = pd.read_csv("telecom_users.csv");
display(tabela);

# ----------------------- Passo 02: Visualizar a Base de Dados
# - Entender as informações que você tem disponível
# - Descobrir as cagadas da base de dados

#axis = 0 -> Linha
#axis = 1 -> Coluna
tabela = tabela.drop("Unnamed: 0", axis = 1);
display(tabela);

# ----------------------- Passo 03: Tratamento de Dados
# - Resolver os valores que estão sendo reconhecidos 
# - de forma errada

#Transforma os valores da coluna TotalGasto de Strings para Numeric
#O "errors = " permite especificar o que ocorre quando a conversão
#não der certo. No caso, Coerce vai deletar a linha (?)
tabela["TotalGasto"] = pd.to_numeric(tabela["TotalGasto"], errors="coerce");

#Exclui colunas com TODOS os valores vazios(NaN)
#Uma coluna totalmente vazia é inútil, pois não possui dado algum
# "Dados sem uso sempre atrapalham"
tabela = tabela.dropna(how="all", axis=1); 

#Exclui todas as linhas com algum valor vazio (NaN)
#Essas são inúteis para a análise, pois a falta de um dos dados 
#compromete a capacidade de estabelecer conclusões
tabela = tabela.dropna(how="any", axis=0);
display(tabela);

# ----------------------- Passo 04: Análise Inicial
# tabela["nome_coluna"].mean()          -> media
# tabela["nome_coluna"].sum()           -> soma tudo
# tabela["nome_coluna"].value_counts()  -> soma quais valores de cada tipo

#O normalize faz o resultado ser apresentado em percentual
#No caso, o Churn determina se o cliente cancelou o pacote ou não
#E com esse comando, vamos determinar a divisão percentual de Sim e Não
print(tabela["Churn"].value_counts(normalize=True).map);

# ----------------------- Passo 05: Análise Detalhada

import plotly.express as px;

for coluna in tabela.columns:

    grafico = px.histogram(tabela, x=coluna, color="Churn", text_auto=True);
    grafico.show();