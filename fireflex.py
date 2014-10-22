#!/usr/bin/python
# python script to look for new tar.gz files ,extract them and append .log to its filename
import os 
import tarfile
import shutil

#open existing file containing list of previously existed files,read contents line by line and add each line to a list
if os.path.isfile("prev_files"):
	f = open("prev_files","r")
	prev_file_list = f.read().splitlines()
else:
	print "First run, No files containing list of previously existed files found!"
	open("prev_files",'w')
	prev_file_list = os.listdir(os.getcwd())
	print "Prev_files created and added list of existing files"
#add list of existing files to current_file_list
current_file_list = os.listdir(os.getcwd())
print "existing file list added to current_file_list" 
#create a directory for extracted files#
if os.path.isdir('extracted_files'):
	pass
else:
	os.mkdir('extracted_files')
#create a directory for log files#
if os.path.isdir('logfiles'):
	pass
else:
	os.mkdir('logfiles')
flag = 0
#check for added files , if found any extract to extracted_files directory,append .log to filename and copy to log directory
if current_file_list != prev_file_list:
	print "New files added or .log file of previous extraction process found!"
	for item in current_file_list:
		if item.endswith('tar.gz'):  
			targz = tarfile.open(item,'r:gz')
			targz.extractall('extracted_files') 
			print ("Found a new file with name %s and extracted successfully")%item
		elif item.endswith('.log'):
			os.rename(item,item+'.log')
			shutil.move(item,os.getcwd()+'/logfiles')
			print ("file %s and moved to logfiles directory")%item
		else:	
			flag = 1
else:
	print "No files added since last update"
if flag == 1:
		print "No tar.gz or .log files found"
#write list of existing files to file prev_files 
with open ('prev_files','w') as f:
	for line in current_file_list:
		f.write("%s\n"% line)

