import json
with open("pessoas.json", "r", encoding="utf-8") as arquivo:
    conteudo = json.load(arquivo)
    print(f"Dados do JSON: {conteudo}")