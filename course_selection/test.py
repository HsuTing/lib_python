csvContent = csv.reader(fcsv)
for row in csvContent:
	keyCheck = True
	for i in range(0, len(key)):
		if row[ key[i]["number"] ] != key[i]["name"]:
			keyCheck = False
	if keyCheck == True:
		filterArray.append(row)
