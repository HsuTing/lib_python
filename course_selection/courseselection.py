#coding:utf-8
import csv
import json

def courseselection(csvFile, jsonFile, key, answer):
	"""csv is data, json is structure"""
	"""key is filter key"""
	"""answer is poeple`s choice"""

	fcsv = open(csvFile + ".csv", "r")
	fjson = open(jsonFile + ".json", "r")
	foutput = open(jsonFile + ".csv", "w")
	filterArray = []
	maxSize = 0

	"""input data"""
	csvContent = csv.reader(fcsv)
	for row in csvContent:
		keyCheck = True
		for i in range(0, len(key)):
			if row[ key[i]["number"] ] != key[i]["name"]:
				keyCheck = False
		if keyCheck == True:
			filterArray.append(row)

	"""input structure"""
	jsonContent = json.load(fjson)
	i = 0
	while i < len(jsonContent["children"]):
		print jsonContent["children"][i]["name"] + "(total is " + str(len(filterArray)) + "):"

		tempNumber = []
		tempCount = 0
		for j in range(0, len(jsonContent["children"][i]["children"])):
			tempNum = raw_input(">> num of " + jsonContent["children"][i]["children"][j]["name"].encode("utf-8").strip() + " : ")
			tempNumber.append(tempNum)
			tempCount = tempCount + int(tempNum)

		"""if totoal number does not enough"""
		if tempCount < len(filterArray):
			print "The num of this part is not enough, please input again"
			print "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"
			continue

		if len(jsonContent["children"][i]["children"]) > maxSize:
			maxSize = len(jsonContent["children"][i]["children"])
		for j in range(0, len(jsonContent["children"][i]["children"])):
			"""add number to every data"""
			jsonContent["children"][i]["children"][j]["number"] = tempNumber[j]

		for k in range(0, len(filterArray)):
			filterArray[k].append("")
		i = i + 1
		print "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"

	"""chocie"""
	count = 1
	while(check(jsonContent) == False):
		for i in range(0, len(filterArray)):
			position = 0
			for j in range(0, len(jsonContent["children"])):
				for k in range(0, len(jsonContent["children"][j]["children"])):
					if int(filterArray[i][answer][position]) == count and jsonContent["children"][j]["children"][k]["number"] != 0 and filterArray[i][answer + 1 + j] == "" and jsonContent["children"][j]["children"][k]["name"] != filterArray[i][answer + 1 + j - 1]:
						filterArray[i][answer + 1 + j] = jsonContent["children"][j]["children"][k]["name"]
						jsonContent["children"][j]["children"][k]["number"] = int(jsonContent["children"][j]["children"][k]["number"]) - 1
					position = position + 1
		count = count + 1
		if count > maxSize:
			break

	"""show final result"""
	for i in range(0, len(jsonContent["children"])):
		for j in range(0, len(jsonContent["children"][i]["children"])):
			print jsonContent["children"][i]["children"][j]["name"] + ": " + str(jsonContent["children"][i]["children"][j]["number"])


	"""write output file"""
	for i in range(0, len(filterArray)):
		for j in range(0, len(filterArray[i])):
			if j > answer:
				foutput.write(filterArray[i][j].encode("utf8") + ",")
			else:
				foutput.write(filterArray[i][j] + ",")
		foutput.write("\n")

	fcsv.close()
	fjson.close()
	foutput.close()

def check(jsonContent):
	for i in range(0, len(jsonContent["children"])):
		for j in range(0, len(jsonContent["children"][i]["children"])):
			if jsonContent["children"][i]["children"][j]["number"] != 0:
				return False

	return True
