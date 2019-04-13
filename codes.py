import sys
op=sys.argv[1]
if op == "dif" :
	txt1=sys.argv[2]
	txt2=sys.argv[3]
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
elif op == "findlast" :
	lines = []
	with open('3', 'w') as outfile:
		for line in reversed(open("serviceList").readlines()):
	    		if 'The date and time is:' in line:
				break
	    		else:
				lines.append(line)
		for line in reversed(lines):
	    		outfile.write(line)
elif op == "delate" :
	infile = "linuxservice.txt"
	outfile = "linuxservices.txt"
	delete_list = [" [ + ]  "]
	fin = open(infile)
	fout = open(outfile, "w+")
	for line in fin:
	    for word in delete_list:
		line = line.replace(word, "")
	    fout.write(line)
	fin.close()
	fout.close()
elif op == "findpos" :
	date1=sys.argv[2]
	date2=sys.argv[3]
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
elif op == "difmanual":
    a=sys.argv[2]
    b=sys.argv[3]
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
    ans=True
    for line in open(b).readlines():
        if 'Process stop working:' in line:
            ans = False
        elif not 'Process start working:' in line and not ans:
            stop2 += line + "\n"
        elif 'Process start working:' in line:
            ans=True
        elif ans:
            work2 += line + "\n"
    only_in_f1 = [i for i in work1 if i not in work2]
    only_in_f2 = [i for i in stop1 if i not in stop2]
    with open('different.txt', 'w') as outfile:
        if only_in_f1:
            outfile.write('Process stop working:\n')
            for line in only_in_f1:
                outfile.write(line)
        if only_in_f2:
            outfile.write('Process start working:\n')
            for line in only_in_f2:
                outfile.write(line)
