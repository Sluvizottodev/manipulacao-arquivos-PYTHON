import pdfplumber

path_pdf = r"C:\Users\User\Downloads\EXTRATO DE DÉBITOS COMPLETO.pdf"

text = ''
with pdfplumber.open(path_pdf) as pdf:
    for page in pdf.pages:
        text += page.extract_text()

print(text)