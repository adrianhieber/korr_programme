import os
import shutil

#speichern in abgaben
fromcopy = input("von wo: ")
tocopy = input("wohin: ")

def adder(srcpath, teamname,file):
	personnr=0
	for (dirpath, dirnames, filenames) in os.walk("./"+tocopy+"/"+teamname):
		for names in dirnames:
			print(f"copy {srcpath} to {dirpath}/{names}/{file}")
			shutil.copyfile(srcpath, dirpath+"/"+names+"/"+file)
			personnr=personnr+1
		break #to stop recursive
	return personnr

def searcher():
	teamnr=0
	personnr=0
	for (dirpath, dirnames, filenames) in os.walk("./"+fromcopy):
		for teamname in dirnames:
			for (dirpath, dirnames, filenames) in os.walk("./"+fromcopy+"/"+teamname):
				for file in filenames:
					personnr=personnr+adder(os.path.join(dirpath,file),teamname,file)
					print(f"{teamname} done")
					teamnr=teamnr+1
					print()
	print(f"succesfull with {teamnr} Teams and {personnr} people")
	
searcher()

		

	
