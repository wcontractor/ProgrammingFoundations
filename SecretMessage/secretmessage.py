#had to switch to python 2.7 to get os.rename to work
import os
saved_dir = raw_input("enter directory name")

def rename_files(saved_dir):
	#Build a list of the files
	file_list = os.listdir(saved_dir)
	os.chdir(saved_dir)
	
	#For each file, rename the file
	for filename in file_list:
		os.rename(filename, filename.translate(None, "0123456789"))
	os.chdir(saved_dir)	

rename_files(saved_dir)
