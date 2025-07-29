> Utilitários simples para ler, escrever e manipular arquivos CSV, JSON e TXT com Python.

## Índice

1. [Visão Geral](#visão-geral)
2. [Funcionalidades](#funcionalidades)
3. [Pré-requisitos](#pré-requisitos)
4. [Instalação](#instalação)
5. [Uso](#uso)

   * [Manipulação de CSV](#manipulação-de-csv)
   * [Manipulação de JSON](#manipulação-de-json)
   * [Manipulação de TXT](#manipulação-de-txt)

---

## Visão Geral

Este repositório reúne scripts e módulos em Python para facilitar a **leitura**, **escrita** e **manipulação** de arquivos de dados comuns, como CSV, JSON e TXT. Ideal para desenvolvedores iniciantes e intermediários que desejam entender padrões de I/O em Python.

## Funcionalidades

* 📄 Leitura e gravação de arquivos CSV (`csv.reader`, `csv.writer`).
* 🗃️ Leitura e gravação de arquivos JSON (`json.load`, `json.dump`).
* 📜 Operações básicas em arquivos de texto (leitura, escrita, anexação).
* 🔄 Funções utilitárias para converter, filtrar e transformar dados entre formatos.
* 👷 Exemplos de tratamento de exceções e verificação de existência de arquivos.

## Pré-requisitos

* Python 3+

## Instalação

1. Clone este repositório:

   ```bash
   git clone https://github.com/sluvizottodev/manipulacao-arquivos-python.git
   cd manipulacao-arquivos-python
   ```

2. (Opcional) Crie e ative um ambiente virtual:

   ```bash
   python3 -m venv venv
   source venv/bin/activate  # Linux/macOS
   venv\Scripts\activate     # Windows
   ```

3. Instale dependências (se houver):

   ```bash
   pip install -r requirements.txt
   ```

> Este projeto não depende de bibliotecas externas além da biblioteca padrão do Python.

## Uso

### Manipulação de CSV

```python
import csv

# Exemplo de escrita de múltiplas linhas
dados = [
    ['Nome', 'Idade', 'Cidade'],
    ['Ana', 30, 'São Paulo'],
    ['Bruno', 25, 'Rio de Janeiro']
]

with open('exemplo.csv', 'w', newline='', encoding='utf-8') as f:
    writer = csv.writer(f)
    writer.writerows(dados)

# Exemplo de leitura
with open('exemplo.csv', 'r', newline='', encoding='utf-8') as f:
    reader = csv.reader(f)
    for linha in reader:
        print(linha)
```

### Manipulação de JSON

```python
import json

# Exemplo de escrita
pessoa = {'nome': 'Mauricio', 'idade': 25, 'cidade': 'Manaus'}
with open('pessoa.json', 'w', encoding='utf-8') as f:
    json.dump(pessoa, f, ensure_ascii=False, indent=4)

# Exemplo de leitura
with open('pessoa.json', 'r', encoding='utf-8') as f:
    dado = json.load(f)
    print(dado['nome'], dado['idade'], dado['cidade'])
```

### Manipulação de TXT

```python
# Escrita de texto simples
texto = ['Linha 1', 'Linha 2', 'Linha 3']
with open('arquivo.txt', 'w', encoding='utf-8') as f:
    f.write("\n".join(texto))

# Leitura
with open('arquivo.txt', 'r', encoding='utf-8') as f:
    for linha in f:
        print(linha.strip())
```


