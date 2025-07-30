import pdfplumber
import pandas as pd
import re

## Cógigo iniciante feito com auxilio de IA, para escalar para projeto real
path_pdf = r"C:\Users\User\Downloads\EXTRATO DE DÉBITOS COMPLETO.pdf"

dados = []

def extrair_responsavel(bloco_texto):
    texto = ' '.join(bloco_texto).replace('\n', ' ')
    nome_match = re.search(r"^(.*?) - FONE:", texto)
    cpf_match = re.search(r"CPF:\s*([\d]+)", texto)
    email_match = re.search(r"E-MAIL:\s*([^\s]+)", texto)
    return {
        "nome": nome_match.group(1).title().strip() if nome_match else "",
        "cpf": cpf_match.group(1) if cpf_match else "",
        "email": email_match.group(1) if email_match else ""
    }

with pdfplumber.open(path_pdf) as pdf:
    responsavel = {"nome": "", "cpf": "", "email": ""}
    for page in pdf.pages:
        texto = page.extract_text()
        linhas = texto.split('\n')

        i = 0
        while i < len(linhas):
            linha = linhas[i].strip()

            if linha.startswith("DADOS DO RESPONSÁVEL FINANCEIRO"):
                i += 1
                responsavel_blocos = []
                while i < len(linhas):
                    l = linhas[i].strip()
                    if l == "" or l.startswith("DADOS DO RESPONSÁVEL FINANCEIRO") or l.startswith("DÉBITOS EM ABERTO"):
                        break
                    responsavel_blocos.append(l)
                    i += 1
                novo_responsavel = extrair_responsavel(responsavel_blocos)
                if novo_responsavel["nome"]:
                    responsavel = novo_responsavel
                continue

            if linha.startswith("DÉBITOS EM ABERTO"):
                i += 1
                debitos_blocos = []
                while i < len(linhas):
                    l = linhas[i].strip()
                    if l == "" or l.startswith("DADOS DO RESPONSÁVEL FINANCEIRO") or l.startswith("VALOR TOTAL"):
                        break
                    debitos_blocos.append(l)
                    i += 1

                texto_debitos = "\n".join(debitos_blocos)

                padrao = re.compile(
                    r"(\d{7}) - ([^\n]+)\n" +
                    r"(\d+º Parcela) (\d{2}/\d{2}/\d{4}) (\d+) dia\(s\) R\$ ([\d.,]+) R\$ ([\d.,]+)\n" +
                    r"([^\n]+)?",
                    re.MULTILINE)

                for match in padrao.finditer(texto_debitos):
                    codigo = match.group(1)
                    nome_parcial = match.group(2).strip()
                    parcela = match.group(3)
                    vencimento = match.group(4)
                    dias_atraso = match.group(5)
                    valor_original = match.group(6)
                    valor_atualizado = match.group(7)
                    sobrenome_turma = match.group(8) if match.group(8) else ""

                    # ❌ Remove "MATERIAL", "DIDÁTICO", etc. do nome
                    partes = f"{nome_parcial} {sobrenome_turma}".strip().split()
                    partes_filtradas = [p for p in partes if p.upper() not in ["MATERIAL", "DIDÁTICO"]]
                    nome_completo = " ".join(partes_filtradas)

                    dados.append({
                        "Código do Aluno": codigo,
                        "Nome do Aluno": nome_completo,
                        "Parcela": parcela,
                        "Vencimento": vencimento,
                        "Dias de Atraso": dias_atraso,
                        "Valor Original": valor_original,
                        "Valor Atualizado": valor_atualizado,
                        "Responsável Nome": responsavel.get("nome", ""),
                        "Responsável CPF": responsavel.get("cpf", ""),
                        "Responsável Email": responsavel.get("email", "")
                    })
                continue

            i += 1

# Exportar
df = pd.DataFrame(dados)
df.to_excel("inadimplentes.xlsx", index=False)
print(f"✅ {len(df)} registros exportados para inadimplentes.xlsx com sucesso!")
