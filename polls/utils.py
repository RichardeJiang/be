import csv

def isNumber(inputStr):
	try:
		float(inputStr)
		return True
	except ValueError:
		return False

def parseCSVFile(inputFile):
	parsedResult = {}
	with open(inputFile, 'rU') as fp:
		readerCSV = csv.reader(fp, delimiter = ",")
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

	print parsedResult
	return parsedResult

if __name__ == "__main__":
	parseCSVFile("test.csv")