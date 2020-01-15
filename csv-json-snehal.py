import csv
import json

csvFilePath = "File.csv"
jsonFilePath = "JFile.json"

data = {}
with open(csvFilePath) as csvFile:
    csvReader = csv.DictReader(csvFile)
    for csvRow in csvReader:
        animals=csvRow['Animals']
        data[animals]=csvRow

with open('jsonFilePath','w')as JSonFile:
    JSonFile.write(json.dumps(data, indent=4))

