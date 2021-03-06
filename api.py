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
	
	df = pd.DataFrame(data, index="L1 L2 L3 L4", columns="TÍTULO CAPÍTULO Art. SUB SEÇÂO".split())
	# df2 = read_pdf(flpath)
	
	for text in df:
		return df.to_csv("CFB_1988.csv")
	
	print(list(map(data)))
	# print(df)
	
	return pd.read_csv("CFB_1988.csv")
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

