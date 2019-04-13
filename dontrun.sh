#!/bin/bash
echo 'Please enter frequency check in seconds: '
read varname
while true; do  
	myvar="$PWD"
	service --status-all 2>&1 | grep "+" | tee "$myvar/linuxservice.txt" &>/dev/null	
	python codes.py delate
	rm linuxservice.txt
	if [[ -s serviceList ]]; 
		then
		python codes.py findlast 
		python codes.py dif 3 linuxservices.txt
		rm 3
		echo "The date and time is: $(date '+%d/%m/%Y %H:%M:%S')" >> serviceList	
		cat linuxservices.txt >> serviceList
		rm linuxservices.txt
		if [[ -s different.txt ]];
			then
				echo "The date and time is: $(date '+%d/%m/%Y %H:%M:%S')" >> Status_Log.txt
				cat different.txt >> Status_Log.txt
		fi
		cat different.txt
		rm different.txt	
	fi;
sleep $varname; done
