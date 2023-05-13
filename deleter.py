import os
import shutil

#speichern in abgaben
actdir = input("Ordner zum machen:")
os.chdir(actdir)
i=0

mykorr=["Team 184344", "Team 184347", "Team 184402", "Team 184518", "Team 184529", "Team 184645", "Team 184762", "Team 184976", "Team 185081", "Team 185085", "Team 185094", "Team 185185", "Team 185236", "Team 185245", "Team 185322", "Team 185328", "Team 185372", "Team 185400"]

for (dirpath, dirnames, filenames) in os.walk("."):
	for name in dirnames:
		if name not in mykorr:
			shutil.rmtree(os.path.join(os.getcwd(),name))
		else:
			print(name)
			i=i+1
	print(f"Insgesamt {i} Abgaben fuer dich :)")
	break #to stop recursive
