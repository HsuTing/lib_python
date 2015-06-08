#coding:utf-8
import csv
import json

def Course_selection(csvFile, jsonFile, key_name, key_num, answer):
	fcsv = open(csvFile + ".csv", "r")
	fjson = open(jsonFile + ".json", "r")
	filterArray = []
	filterNum = []
	nameArray = []

	"""input data"""
	csvContent = csv.reader(fcsv)
	for row in csvContent:
		for i in range(0, len(key_num)):
			if row[ key_num[i] ] == key_name[i]:
				filterArray.append(row)
	for i in range(0, len(filterArray)):
		for j in range(0, len(filterArray[i][answer])):
			filterArray[i].append("")

	"""input structure"""
	jsonContent = json.load(fjson)
	i = 0
	while(i < len(jsonContent["children"])):
		print jsonContent["children"][i]["name"] + "(total is " + str(len(filterArray)) + "):"

		temp = []
		tempCount = 0
		for j in range(0, len(jsonContent["children"][i]["children"])):
			tempNum = raw_input(">> num of " + jsonContent["children"][i]["children"][j]["name"].encode("utf-8").strip() + " : ")
			temp.append(tempNum)
			tempCount = tempCount + int(tempNum)

		if tempCount != len(filterArray):
			print "The num of this part is not equal to total num, please input again"
			print "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"
			continue

		for j in range(0, len(temp)):
			filterNum.append(int(temp[j]))
		for j in range(0, len(jsonContent["children"][i]["children"])):
			nameArray.append(jsonContent["children"][i]["children"][j]["name"].encode("utf-8").strip())
		i = i + 1
		print "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"

	"""choice"""
	count = 1
	while(check(filterNum) == False):
		for i in range(0, len(filterArray)):
			for j in range(0, len(filterArray[i][answer])):
				if int(filterArray[i][answer][j]) == count and filterNum[j] != 0:
					filterArray[i][ answer + 1 + j ] = nameArray[j]
					filterNum[j] = filterNum[j] - 1
		count = count + 1

	for i in range(0, len(filterArray)):
		print filterArray[i][0] + ": "
		for j in range(0, len(filterArray[i][answer])):
			print str(j) + ": " + filterArray[i][ answer + 1 + j ]

	fcsv.close()
	fjson.close()

def check(filterNum):
	count = 0
	for i in range(0, len(filterNum)):
		if filterNum[i] == 0:
			count = count + 1

	if count == len(filterNum):
		return True
	else:
		return False
