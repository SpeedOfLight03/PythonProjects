# from PyPDF2 import PdfReader as pdr, PdfWriter as pdw
from PyPDF2 import PdfReader, PdfWriter

## Object for pdf write
out_pdf = PdfWriter()

file_pdf = PdfReader(open('/home/arnab/Learning/Python/Python Projects/PDF_Password_Protection/resume.pdf', 'rb'))
for i in range(len(file_pdf.pages)):
    page_details = file_pdf.pages[i]
    ## Addd to the output page
    out_pdf.add_page(page_details)


password = "arnab@2003"

out_pdf.encrypt(password)

with open("encrypted_resume.pdf", "wb") as filename:
    out_pdf.write(filename)








