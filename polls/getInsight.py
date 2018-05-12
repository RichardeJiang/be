import csv
import codecs
from collections import Counter

from utils import parseCSVFile, testCSVFileFormatMatching, isNumber

def parseAuthorCSVFile(inputFile):

	csvFile = inputFile
	dialect = csv.Sniffer().sniff(codecs.EncodedFile(csvFile, "utf-8").read(1024))
	csvFile.open()
	# reader = csv.reader(codecs.EncodedFile(csvFile, "utf-8"), delimiter=',', dialect=dialect)
	reader = csv.reader(codecs.EncodedFile(csvFile, "utf-8"), delimiter=',', dialect='excel')

	rowResults = []
	for index, row in enumerate(reader):
		rowResults.append(row)
		print row
		print type(row)
		if index == 5:
			break

	parsedResult = {}

	return parsedResult

def getAuthorInfo(inputFile):
	"""
	author.csv: header row, author names with affiliations, countries, emails
	data format:
	submission ID | f name | s name | email | country | affiliation | page | person ID | corresponding?
	"""
	parsedResult = {}

	lines = parseCSVFile(inputFile)[1:]
	lines = [ele for ele in lines if ele]

	authorList = []
	for authorInfo in lines:
		# authorInfo = line.replace("\"", "").split(",")
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

def getReviewScoreInfo(inputFile):
	"""
	review_score.csv
	data format:
	review ID | field ID | score
	File has header

	e.g. 1,1,3 - score (can be negative)
	     1,2,5 - confidence
	     1,3,no - recommended
	"""
	parsedResult = {}
	lines = parseCSVFile(inputFile)[1:]
	lines = [ele for ele in lines if ele]
	scores = []
	confidences = []
	isRecommended = []

	scores = [int(line[2]) for line in lines if int(line[1]) == 1]
	confidences = [int(line[2]) for line in lines if int(line[1]) == 2]
	isRecommended = [str(line[2]).replace("\r", "") for line in lines if int(line[1]) == 3]

	parsedResult['yesPercentage'] = float(isRecommended.count('yes')) / len(isRecommended)
	parsedResult['meanScore'] = sum(scores) / float(len(scores))
	parsedResult['meanConfidence'] = sum(confidences) / float(len(confidences))
	parsedResult['totalReview'] = len(confidences)

	return {'infoType': 'review', 'infoData': parsedResult}

if __name__ == "__main__":
	parseCSVFile(fileName)