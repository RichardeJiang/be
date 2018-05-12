import csv
from collections import Counter

def isNumber(inputStr):
	try:
		float(inputStr)
		return True
	except ValueError:
		return False

def parseCSVFile(inputFile):
	"""
	Parse the uploaded CSV file
	assuming that the uploaded file is of Excel CSV format: allowing multilines in one cell, use double quote to include such cells
	
	Inputs: Django uploaded file 

	Returns: list of lists (inner list represent each row)
	"""

	csvFile = inputFile
	dialect = csv.Sniffer().sniff(codecs.EncodedFile(csvFile, "utf-8").read(1024))
	csvFile.open()
	# reader = csv.reader(codecs.EncodedFile(csvFile, "utf-8"), delimiter=',', dialect=dialect)
	reader = csv.reader(codecs.EncodedFile(csvFile, "utf-8"), delimiter=',', dialect='excel')

	rowResults = [row for row in reader]

	return rowResults

def testCSVFileFormatMatching(inputFile, selectedType):
	"""
	Test whether the upload CSV file matches with the selected type (author, submission, review)
	assuming that the uploaded file sticks to the correct format strictly

	ATTN: for now only testing using the number of columns, but may change to more formal test
	like using the types of each column

	Author CSV file schema (9 columns):
	submission ID | f name | s name | email | country | affiliation | page | person ID | corresponding?

	Submission CSV file schema (13 columns):
	submission ID | track ID | track name | title | authors | submit time | last update time | form fields | keywords | decision | notified | reviews sent | abstract

	Review CSV file schema (15 columns):
	review ID | paper ID? | reviewer ID | reviewer name | unknown | text | scores | overall score | unknown | unknown | unknown | unknown | date | time | recommend?

	Inputs: inputFile: Django uploaded file; selectedType: string (of 'author', 'submission', 'review')

	Returns: true or false
	"""

	firstRow = parseCSVFile(inputFile)[0]
	if selectedType is "author":
		return len(firstRow) == 9
	elif selectedType is "submission":
		return len(firstRow) == 13
	else:
		return len(firstRow) == 15

def returnTestChartData(inputFile):
	"""
	Just return dummy data for testing the Charts construction
	"""
	data = {}
	data["year"] = [1990, 1991, 1992, 1993, 1994, 1995, 1996, 1997, 1998, 1999]
	data["inCitations"] = [12, 18, 34, 45, 23, 99, 65, 45, 55, 90]
	data["outCitations"] = [34, 41, 9, 23, 39, 74, 35, 12, 90, 44]
	return {'infoType': 'dummy', 'infoData': data}

def getReviewInfo(inputFile):
	"""
	review_score.csv
	data format:
	review ID | field ID | score
	e.g. 1,1,3 - score
	     1,2,5 - confidence
	     1,3,no - recommended
	"""
	parsedResult = {}
	fileData = inputFile.read().decode("utf-8")
	lines = fileData.split("\n")[1:]
	lines = [ele for ele in lines if ele]
	scores = []
	confidences = []
	isRecommended = []

	# another way of thinking:
	scores = [int(line.split(",")[2]) for line in lines if int(line.split(",")[1]) == 1]
	confidences = [int(line.split(",")[2]) for line in lines if int(line.split(",")[1]) == 2]
	isRecommended = [str(line.split(",")[2]).replace("\r", "") for line in lines if int(line.split(",")[1]) == 3]

	# print isRecommended
	# print isRecommended.count('yes')
	parsedResult['yesPercentage'] = float(isRecommended.count('yes')) / len(isRecommended)
	parsedResult['meanScore'] = sum(scores) / float(len(scores))
	parsedResult['meanConfidence'] = sum(confidences) / float(len(confidences))
	parsedResult['totalReview'] = len(confidences)

	# for line in lines:
	# 	details = line.split(",")
	# 	if details[1] == 1:
	# 		scores.append(details[2])
	# 	elif details[1] == 2:
	# 		confidences.append(details[2])
	# 	else:
	# 		isRecommended.append(details[2])

	return {'infoType': 'review', 'infoData': parsedResult}

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
		# print authorInfo
		authorList.append({'name': authorInfo[1] + " " + authorInfo[2], 'country': authorInfo[4], 'affiliation': authorInfo[5]})
	

	authors = [ele['name'] for ele in authorList if ele] # adding in the if ele in case of empty strings; same applies below
	topAuthors = Counter(authors).most_common(5)
	parsedResult['topAuthors'] = {'labels': [ele[0] for ele in topAuthors], 'data': [ele[1] for ele in topAuthors]}

	countries = [ele['country'] for ele in authorList if ele]
	topCountries = Counter(countries).most_common(5)
	parsedResult['topCountries'] = {'labels': [ele[0] for ele in topCountries], 'data': [ele[1] for ele in topCountries]}

	affiliations = [ele['affiliation'] for ele in authorList if ele]
	topAffiliations = Counter(affiliations).most_common(5)
	parsedResult['topAffiliations'] = {'labels': [ele[0] for ele in topAffiliations], 'data': [ele[1] for ele in topAffiliations]}


	return {'infoType': 'author', 'infoData': parsedResult}

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

if __name__ == "__main__":
	parseCSVFile("review.csv")