import csv
## write rescreve, apaga se já tiver algo, recria do 0
#writerow
with open("filmes.csv", "w", newline = '', encoding = "utf-8") as arquivo:
    escritor = csv.write(arquivo)
    escritor.writerow(["Missão impossível 7", 2025, "Ação"])
    escritor.wtriterow(["Matrix", 1999, "Ficação científica"])

#writerows

dados = [
    ['Ana', 30, 'São Paulo'],
    ['Bruno', 25, 'Rio de Janeiro'],
    ['Clara', 28, 'Belo Horizonte']
]

with open('exemplo.csv', 'w', newline='') as arquivo:
    escritor = csv.writer(arquivo)
    escritor.writerow(['Nome', 'Idade', 'Cidade'])  # cabeçalho
    escritor.writerows(dados)  # várias linhas
