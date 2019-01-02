from bs4 import BeautifulSoup as Bs
import PyPDF4
import os
import textract
import pandas as pd
# from tabula import convert_into
from tabula import read_pdf

home = os.environ.get("HOME")  # fixo
folder = r"/documents/jobs/grp_prazo/2018-12-27 Grupo Prazo/1 - Dados Originais/"
flname = 'CFB_1988.pdf'

flpath = home + folder + flname

# title = "CONSTITUIÇÃO DA REPÚBLICA FEDERATIVA DO BRASIL"


def read_pdf():
	pass
	

pdfFileObj = open(flpath, 'rb')

pdfReader = PyPDF4.PdfFileReader(pdfFileObj)

num_pages = pdfReader.numPages
count = 1
page = ""

while count < num_pages:
	pageObj = pdfReader.getPage(count)
	page += pageObj.extractText()

	if page != "":
		page = page
	else:
		page = textract.process(flpath, method='tesseract', language='pt')

	if page == "TÍTULO" or "CAPÍTULO" or "Art. " or "SUB":
		break
	if page.endswith("SEÇÃO"):
		break

	count += 1

	print(page)


def organization():

	# arq = open(flpath, 'rb')
	
	data = {
		"TÍTULO": [""],
		"CAPÍTULO": [""],
		"Art. ": [""],
		"SUB": [""],
		"SEÇÂO": [""]
	}

	# df = pd.DataFrame(data, columns=["TÍTULO", "CAPÍTULO", "Art. ", "SUB", "SEÇÂO"])
	df = read_pdf(flpath)
	
	print(df)
	
	return organization()
#
#
# def convertio():
#
# 	f = wrapper.localize_file(folder)
# 	co = f.wrapper.convert_into(folder, folder, output_format="csv", java_options=None, **kwargs)
#
# 	if co is True:
# 		print("Done")
# 	else:
# 		print("Not done")
#
# 	return
#
#
# print(organization())
# print(convertio())

