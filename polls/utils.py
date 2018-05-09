import csv
from collections import Counter

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

def getAuthorInfo(inputFile):
	"""
	author.csv: header row, author names with affiliations, countries, emails
	data format:
	paper ID | f name | s name | email | country | affiliation | page | person ID | corresponding?
	"""
	parsedResult = {}
	fileData = inputFile.read().decode("utf-8")
	lines = fileData.split("\n")[1:]
	lines = [ele for ele in lines if ele]
	authorList = []
	for line in lines:
		authorInfo = line.replace("\"", "").split(",")
		print authorInfo
		authorList.append({'name': authorInfo[1] + " " + authorInfo[2], 'country': authorInfo[4], 'affiliation': authorInfo[5]})
	
	# authors = map(lambda ele: ele['name'], authorList)
	# authors = [ele for ele in authors if ele] # in case of empty strings; same applies below
	# topAuthors = []
	# for authorName, paperCounts in Counter(authors).most_common(5):
	# 	topAuthors.append({authorName: paperCounts})
	# parsedResult['topAuthors'] = topAuthors

	# countries = map(lambda ele: ele['country'], authorList)
	# countries = [ele for ele in countries if ele]
	# topCountries = []
	# for countryName, paperCounts in Counter(countries).most_common(5):
	# 	topCountries.append({countryName: paperCounts})
	# parsedResult['topCountries'] = topCountries

	authors = [ele['name'] for ele in authorList if ele] # adding in the if ele in case of empty strings; same applies below
	topAuthors = [{ele[0]:ele[1]} for ele in Counter(authors).most_common(5)]
	parsedResult['topAuthors'] = topAuthors

	countries = [ele['country'] for ele in authorList if ele]
	topCountries = [{ele[0]:ele[1]} for ele in Counter(countries).most_common(5)]
	parsedResult['topCountries'] = topCountries

	affiliations = [ele['affiliation'] for ele in authorList if ele]
	topAffiliations = [{ele[0]:ele[1]} for ele in Counter(affiliations).most_common(5)]
	parsedResult['topAffiliations'] = topAffiliations


	return parsedResult

def parseCSVFileFromDjangoFile(inputFile):
	parsedResult = {}
	fileData = inputFile.read().decode("utf-8")
	lines = fileData.split("\n")
	print lines[0]
	headerRow = lines[0]
	secondRow = lines[1]
			
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
		print row
		if index == 0:
			headerRow = row
		elif index == 5:
			secondRow = row
			break
			
	hasHeader = False
	for index, ele in enumerate(headerRow):
		ele2 = float(secondRow[index]) if isNumber(secondRow[index]) else secondRow[index]
		if type(ele) != type(ele2):
			hasHeader = True
			break

	contentRow = secondRow if hasHeader else headerRow
	# print secondRow
	# contentRow = secondRow
	# Testing with the first row content
	for index, ele in enumerate(contentRow):
		parsedResult["entry" + str(index + 1)] = ele

	# print parsedResult
	return parsedResult

if __name__ == "__main__":
	parseCSVFile("review.csv")