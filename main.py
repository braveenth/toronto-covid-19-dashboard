#!/usr/bin/python3
# The goal of this program is to parse the JSON file provided by the City of Toronto - COVID Cases so that the data can be shipped to ElasticSearch for further analysis
import json

file_name = 'COVID19_cases.json'
json_file = open(file_name, "r")

json_data = json.loads(json_file.read())

# Write the JSON line by line
cases_file = open("./covid_cases/output.txt", "w")

for item in json_data:
	# We need to format the JSON objects properly so that Filebeat and Elastic can parse it properly
	# We need to convert '_id' to 'message_id' since the '_id' field is reserved for use in Elasticsearch
	# Reason provided by Filebeat: "Field [_id] is a metadata field and cannot be added inside a document
	item['message_id'] = item.pop('_id')
	cases_file.write(str(json.dumps(item))+'\n')
	#print(item)
	print("Wrote item")

json_file.close()
cases_file.close()

# if __name__ == "__main__":
# 	print("Running main.py")