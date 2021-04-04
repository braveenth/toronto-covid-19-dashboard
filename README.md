# toronto-covid-19-dashboard
Ingesting various City of Toronto COVID-19 data sources into Elasticsearch in order to build a Kibana dashboard.

The goal of main.py is to parse the JSON file provided by the City of Toronto - COVID Cases so that the data can be shipped to ElasticSearch for further analysis.

The docker-compose file sets up various components required so that ElasticSearch, Filebeat, and Kibana can work together to produce our desired results.

Here is a link to the City of Toronto's Open Data Portal: https://open.toronto.ca/

Note: Information about COVID-19 cases is gathered through external resources. The information provided may not be accurate. Use at your own risk.
