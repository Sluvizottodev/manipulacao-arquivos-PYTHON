import pdfplumber

path_pdf = r"C:\Users\User\Downloads\EXTRATO DE DÉBITOS COMPLETO.pdf"

with pdfplumber.open(path_pdf) as pdf:
    for page in pdf.pages:
        tables = page.extract_tables()
        for table in tables:
            for row in table:
                print(row)