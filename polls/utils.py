import csv

def isNumber(inputStr):
	try:
		float(inputStr)
		return True
	except ValueError:
		return False

def returnTestChartData(inputFile):
	"""
	Just return dummy data for testing the ECharts construction
	"""
	data = {}
	data["year"] = [1990, 1991, 1992, 1993, 1994, 1995, 1996, 1997, 1998, 1999]
	data["inCitations"] = [12, 18, 34, 45, 23, 99, 65, 45, 55, 90]
	data["outCitations"] = [34, 41, 9, 23, 39, 74, 35, 12, 90, 44]
	return data

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