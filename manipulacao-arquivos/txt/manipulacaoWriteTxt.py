# criar ou sobrescrever um arquivo TXT
with open("exemplo.txt", "w", encoding="utf-8") as arquivo:
    arquivo.write("Olá, mundo!\n")
    arquivo.write("Este é um exemplo de escrita em arquivo TXT.\n")
