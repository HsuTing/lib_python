#coding:utf-8
import csv
import json

def Course_selection(csvFile, jsonFile, key_name, key_num, answer):
	fcsv = open(csvFile, "r")
	fjson = open(jsonFile, "r")
	filterArray = []
	filterNum = []

	csvContent = csv.reader(fcsv)
	for row in csvContent:
		for i in range(0, len(key_num)):
			if(row[ key_num[i] ] == key_name[i]):
				filterArray.append(row)
				print row
	print "---------------------------------"

	jsonContent = json.load(fjson)
	while(i < len(jsonContent["children"])):
		print jsonContent["children"][i]["name"] + "(total is " + str(len(filterArray)) + "):"

		temp = []
		tempCount = 0
		for j in range(0, len(jsonContent["children"][i]["children"])):
			tempNum = raw_input(">> num of " + jsonContent["children"][i]["children"][j]["name"].encode("utf-8").strip() + " : ")
			temp.append(tempNum)
			tempCount = tempCount + int(tempNum)

		if(tempCount != len(filterArray)):
			print "The num of this part is not equal to total num, please input again"
			print "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"
			continue

		filterNum.append(temp)
		i = i + 1
		print "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"
	print filterNum

	fcsv.close()
	fjson.close()
