#Course Selection

##Environment

```
	ubuntu 14.04.2 LTS
```

##Language

```
	python
```

##File

> courseselection.py

```
- courseselection(csvFile, jsonFile, key, answer):

	csvFile is data file, and json is structure file.
	key is filter key, which decides that which data is used.
	answer is the number of csvFile`s column which is people`s result.
	jsonFile is also the name of output file.

	example:

		key = [
			{
				"number": 2,
				"name": "一類"
			}
	  	]
		courseselection("input", "1", key, 3)
```
