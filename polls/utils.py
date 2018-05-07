import csv

def isNumber(inputStr):
	try:
		float(inputStr)
		return True
	except ValueError:
		return False

def parseCSVFileFromDjangoFile(inputFile):
	parsedResult = {}
	fileData = inputFile.read().decode("utf-8")
	lines = fileData.split("\n")
	print lines[0]
	headerRow = lines[0]
	secondRow = lines[1]

	# for index, row in enumerate(fileData):
	# 	if index == 0:
	# 		headerRow = row
	# 	elif index == 1:
	# 		secondRow = row
	# 		break
			
	hasHeader = False
	for index, ele in enumerate(headerRow):
		ele2 = float(secondRow[index]) if isNumber(secondRow[index]) else secondRow[index]
		if type(ele) != type(ele2):
			hasHeader = True
			break

	contentRow = secondRow if hasHeader else headerRow
	# contentRow = secondRow
	# Testing with the first row content
	for index, ele in enumerate(contentRow):
		parsedResult["entry" + str(index + 1)] = ele

	return parsedResult

def parseCSVFile(inputFile):
	parsedResult = {}
	readerCSV = csv.reader(inputFile, delimiter = ",")
	headerRow = None
	secondRow = None
	for index, row in enumerate(readerCSV):
		if index == 0:
			headerRow = row
		elif index == 1:
			secondRow = row
			break
			
	hasHeader = False
	for index, ele in enumerate(headerRow):
		ele2 = float(secondRow[index]) if isNumber(secondRow[index]) else secondRow[index]
		if type(ele) != type(ele2):
			hasHeader = True
			break

	contentRow = secondRow if hasHeader else headerRow
	# contentRow = secondRow
	# Testing with the first row content
	for index, ele in enumerate(contentRow):
		parsedResult["entry" + str(index + 1)] = ele

	return parsedResult

if __name__ == "__main__":
	parseCSVFile("test.csv")