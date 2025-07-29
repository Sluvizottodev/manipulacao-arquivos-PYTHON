import json

pessoa = {
    "nome": "Mauricio",
    "idade": 25,
    "cidade": "Manaus"
}

with open("pessoas.json", "w", encoding="utf-8") as arquivo:
    json.dump(pessoa, arquivo, ensure_ascii=False, indent=4)