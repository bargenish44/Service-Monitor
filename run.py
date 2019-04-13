import os
import platform
import time
import subprocess
def dif(a,b):
	txt1=a
	txt2=b
	with open(txt1) as infile:
	    f1 = infile.readlines()
	with open(txt2) as infile:
	    f2 = infile.readlines()
	only_in_f1 = [i for i in f1 if i not in f2]
	only_in_f2 = [i for i in f2 if i not in f1]
	with open('different.txt', 'w') as outfile:
	    if only_in_f1:
		outfile.write('Process stop working:\n')
		for line in only_in_f1:
		    outfile.write(line)

	    if only_in_f2:
		outfile.write('Process start working:\n')
		for line in only_in_f2:
		    outfile.write(line)
def difmanual(a,b):
    ans=True
    work1 = ""
    work2 = ""
    stop1 = ""
    stop2 = ""
    for line in open(a).readlines():
        if 'Process stop working:' in line:
            ans=False
        elif not 'Process start working:' in line and not ans:
             stop1 += line+"\n"
        elif 'Process start working:' in line:
            ans=True
        elif ans:
            work1 += line+"\n"
	ans = True
    for line in open(b).readlines():
        if 'Process stop working:' in line:
            ans = False
        elif not 'Process start working:' in line and not ans:
            stop2 += line + "\n"
        elif 'Process start working:' in line:
            ans=True
        elif ans:
            work2 += line + "\n"
    only_in_f1 = [line for line in work1 if line not in work2]
    only_in_f2 = [line for line in stop1 if line not in stop2]
    with open('different.txt', 'w') as outfile:
        if only_in_f1:
            outfile.write('Process stop working:\n')
            for line in only_in_f1:
                outfile.write(line)
        if only_in_f2:
            outfile.write('Process start working:\n')
            for line in only_in_f2:
                outfile.write(line)
def findlast():
	lines = []
	with open('3', 'w') as outfile:
		for line in reversed(open("serviceList").readlines()):
	    		if 'The date and time is:' in line:
				    break
	    		else:
				    lines.append(line)
		for line in reversed(lines):
	    		outfile.write(line)
def delete():
	infile = "linuxservice.txt"
	outfile = "linuxservices.txt"
	delete_list = [" [ + ]  "]
	fin = open(infile,"r")
	fout = open(outfile, "w+")
	for line in fin:
	    print(line)
	    line=line.lstrip(delete_list)
	    fout.write(line.lstrip(delete_list))
	fin.close()
	fout.close()
def remove_spaces():
	with open("different.txt", "r") as f:
		for line in f:
			cleanedLine = line.strip()
			if cleanedLine: # is not empty
				print(cleanedLine)
def findpos(date1,date2) :
	lines = []
	flag=True
	fout = open("one", "w+")
	for line in open("Status_Log.txt").readlines():
	    if 'The date and time is: ' in line:
	    	if flag:
		        if date1 in line:
			        flag=False
		else:
		   break
	    elif not flag:
		    fout.write(line)
	for line in lines:
	    fout.write(line)
	fout = open("two", "w+")
	lines = []
	flag=True
	for line in open("Status_Log.txt").readlines():
	    if 'The date and time is: ' in line:
	    	if flag:
		        if date2 in line:
			        flag=False
		else:
		   break
	    elif not flag:
		    fout.write(line)
	for line in lines:
	    fout.write(line)
def check_files():
	global duc1
	global duc2
	with open("serviceList", "r") as onetmp:
		duc1tmp = onetmp.readlines()
	with open("Status_Log.txt", "r") as twotmp:
		duc2tmp = twotmp.readlines()
	if(duc1tmp!=duc1 or duc2tmp != duc2):
		print("Someone touched ur files")
		exit(0)
	else:
		duc1=onetmp
		duc2=twotmp
def update_files():
	global duc1
	global duc2
	with open("serviceList", "r") as one:
		duc1 = one.readlines()
	with open("Status_Log.txt", "r") as two:
		duc2 = two.readlines()
duc1=""
duc2=""
print('Hey welcome to my Service Monitor program.')
System=platform.system()
mode=raw_input("Please enter your Mode:(Monitor,Manual,quit).")
mode=mode.lower()
while(mode!="monitor" and mode != "manual" and mode != "quit"):
	mode = raw_input("invalid input , Please enter your Mode:(Monitor,Manual,quit).")
if (mode=="manual") :
	date1=raw_input('Please enter the first date(The recent date) to compare(at: %d/%m/%Y %H:%M:%S format): ')
	date2=raw_input('Please enter the second date(The old date) to compare(at: %d/%m/%Y %H:%M:%S format): ')
	findpos(date1,date2)
	#check_files()
	difmanual("one","two")
	os.system("rm one")
	os.system("rm two")
	os.system("cat different.txt")
	os.system("rm different.txt")
	#check_files()
elif (mode == "monitor"):
	if(System=="Windows"):
		times=raw_input('Please enter frequency check in seconds: ')
		while True:
			p = subprocess.Popen(['powershell.exe', 'Get-Service | where-object {$_.Status -eq "Running"} | select Name >windowsservice.txt'])
			time.sleep(1)
			p = subprocess.Popen(['powershell.exe', 'Get-Content windowsservice.txt | Select-Object -Skip 3 | Out-File windowsservices.txt'])
			time.sleep(0.5)
			os.system("rm windowsservice.txt")
			if(os.stat("serviceList").st_size != 0):
				findlast()
				dif("3","windowsservices.txt")
				exit(0)
				os.system("rm 3")
				#check_files()
				time.sleep(0.5)
				os.system("echo The date and time is: $(date '+%d/%m/%Y %H:%M:%S') >> serviceList")
				remove_spaces()
				os.system("cat windowsservices.txt >> serviceList")
				os.system("rm windowsservices.txt")
				if(os.stat("different.txt")!=0):
					os.system("echo 'The date and time is: $(date '+%d/%m/%Y %H:%M:%S')' >> Status_Log.txt")
					os.system("cat different.txt >> Status_Log.txt")
				#update_files()
				remove_spaces()
				os.system("cat different.txt")
				os.system("rm different.txt")
				#check_files()
			else:
				os.system("echo 'The date and time is: $(date '+%d/%m/%Y %H:%M:%S')' >> serviceList")
				os.system("cat windowsservices.txt >> serviceList")
				os.system("rm windowsservices.txt")
			time.sleep(float(times))
	elif (System == "Linux"):
		#while True:
			
			os.system("bash dontrun.sh")
			#p = subprocess.Popen(['Terminal.exe',"service --status-all | grep '+' | tee 'linuxservice.txt' &>/dev/null "])
			#command = "service --status-all | grep '+' | tee 'linuxservice.txt' &>/dev/null "
			#p = subprocess.Popen(
			#	command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
			#time.sleep(1)
			#delete()
			#exit(0)
			#os.system("rm linuxservice.txt")
			#if(os.stat("serviceList").st_size != 0):
				#check_files()
				#findlast()
				#dif("3","linuxservices.txt")
				#os.system("rm 3")
				#os.system("echo The date and time is: $(date '+%d/%m/%Y %H:%M:%S') >> serviceList")
				#os.system("cat linuxservices.txt >> serviceList")
				#os.system("rm linuxservices.txt")
				#if(os.stat("different.txt")!=0):
				#	os.system("echo 'The date and time is: $(date '+%d/%m/%Y %H:%M:%S')' >> Status_Log.txt")
					#os.system("cat different.txt >> Status_Log.txt")
				#update_files()
				#os.system("cat different.txt")
				#os.system("rm different.txt")
			#else:
				#os.system("echo 'The date and time is: $(date '+%d/%m/%Y %H:%M:%S')' >> serviceList")
				#os.system("cat linuxservices.txt >> serviceList")
				#update_files()
				#os.system("rm linuxservices.txt")
			#time.sleep(float(times))
elif (mode=="quit"):
	exit(0)
