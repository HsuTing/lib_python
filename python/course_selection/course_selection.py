import csv
import json

def Course_selection(csvFile, jsonFile, key_name, key_num, answer):
	fcsv = open(csvFile, "r")
	fjson = open(jsonFile, "r")
	filterArray = []

	csvContent = csv.reader(fcsv)
	for row in csvContent:
		for i in range(0, len(key_num)):
			if(row[ key_num[i] ] == key_name[i]):
				filterArray.append(row)

	print filterArray
	print "---------------------------------"
	jsonContent = json.load(fjson)
	for i in range(0, len(jsonContent["children"])):
		for j in range(0, len(jsonContent["children"][i]["children"])):
			print jsonContent["children"][i]["children"][j]["name"]

	fcsv.close()
	fjson.close()
