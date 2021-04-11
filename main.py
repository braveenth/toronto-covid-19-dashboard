#!/usr/bin/python3
# The goal of this program is to parse the JSON file provided by the City of Toronto - COVID Cases so that the data can be shipped to ElasticSearch for further analysis
import json
#from datetime import datetime


file_name = './output_curl.txt'
json_file = open(file_name, "r")

json_data = json.loads(json_file.read())

# Write the JSON line by line
cases_file = open("./output.txt", "w")

for item in json_data:
	# We need to format the JSON objects properly so that Filebeat and Elastic can parse it properly
	# We need to convert '_id' to 'message_id' since the '_id' field is reserved for use in Elasticsearch
	# Reason provided by Filebeat: "Field [_id] is a metadata field and cannot be added inside a document
	item['message_id'] = item.pop('_id')

	# We are going to convert the dates to an ISO8601 format for ElasticSearch
	# We can use isoformat() or append the required string
	item['reported_date'] = item['Reported Date'] + 'T00:00:00-04:00'
	item['@timestamp'] = item.pop('Reported Date') + 'T16:44:50.000Z'
	item['episode_date'] = item.pop('Episode Date') + 'T00:00:00-04:00'

	cases_file.write(str(json.dumps(item))+'\n')
	#print(item)
	print("Wrote item")

json_file.close()
cases_file.close()

# if __name__ == "__main__":
# 	print("Running main.py")