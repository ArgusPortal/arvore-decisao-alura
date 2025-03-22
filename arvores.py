import pandas as pd


dados = pd.read_csv("creditcard.csv")
##print(dados.head())

n_transacoes = dados['Class'].count()
n_fraudes = dados['Class'].sum()
n_normais = n_transacoes - n_fraudes
fraudes_porc = n_fraudes / n_transacoes
normais_porc = n_normais / n_transacoes

print("Número de transações: ", n_transacoes)
print("Número de fraudes: ", n_fraudes, "%.2f" %(fraudes_porc*100))
print("Número de transações normais: ", n_normais, "%.2f" %(normais_porc*100))