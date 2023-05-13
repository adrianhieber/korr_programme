import os
from PyPDF2 import PdfWriter

toadd = open("eval.pdf", "rb")
org_dir = os.getcwd()
counter = 0

for (dirpath, dirnames, filenames) in os.walk("."):
	for filename in filenames:
		if ".pdf" not in filename or filename=="eval.pdf":
			continue
		print("found "+filename)	
		os.chdir(dirpath)
		
		inputpdf = open(filename, "rb")
		output = PdfWriter()
		
		output.append(toadd)
		output.append(inputpdf)
		
		output.write(filename)
		output.close()
		print("merged")
		print()
		counter = counter + 1
		os.chdir(org_dir)

print(f"merged {counter} pdfs")
