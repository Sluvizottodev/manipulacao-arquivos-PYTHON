import csv

# só funciona caso o arquivo já tenha sido criado ou dará erro
with open("filmes.csv", "r", newline='', encoding="utf8") as arquivo:
    leitor = csv.reader(arquivo)
    for linha in leitor:
        print(f"Linha CSV: {linha}")
