import os
import glob

extension=['*.txt','*.xls','*.xlsx','*.jpeg','*.png','*.jpg','*.html','*.htm','*.docx','*.pdf','*.ppt','*.rar']

Desktop=os.getcwd()

os.mkdir("Backup")
Backup = os.getcwd() + '\\Backup\\'
newFile=Backup
os.chdir(Backup)
#Creating Directory for respective file extension
for file in ([ext for ext in extension]):
	os.mkdir(file[2:])
os.chdir(Desktop)

#Writing file to perticular destination
for file in ([ext for ext in extension]):
	for ext in glob.glob(file):
		fileToMove = newFile +file[2:]+"\\"+ ext
		os.rename(ext,fileToMove)

