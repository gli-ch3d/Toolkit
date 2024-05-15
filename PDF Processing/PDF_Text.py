import PyPDF2

pdf_file = open('file_name.pdf','rb')

read = PyPDF2.PdfFileReader(pdf_file)

pg_no = read.numPages

get_pg = pdfreader.getPage(pg_no+1)

text = pageobj.extractText()

with open('file_loc/sample.txt', mode = 'w') as f:
    f.writelines(text)