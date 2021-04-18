# Toronto COVID-19 Dashboard
Since the province of Ontario is going into another lockdown, I made the decision to create this project to practice cloud computing concepts (AWS, Docker), Infrastructure-as-Code (Terraform), and data ingestion/parsing/analysis (Elastic Stack, Python, RESTful APIs, Filebeat). 

In this project, we are ingesting various City of Toronto COVID-19 data sources into Elasticsearch in order to build a Kibana dashboard.

The goal of main.py is to parse the JSON file provided by the City of Toronto - COVID Cases so that the data can be shipped to Elasticsearch for further analysis.

The docker-compose file sets up various components required so that ElasticSearch, Filebeat, and Kibana can work together to produce our desired results.

You can ssh into the instance after doing a Terraform Plan and Apply by running the following command:

ssh elasticsearch@$(terraform output -raw public_ip) -i ../tf-cloud-init

Before doing this, you need to setup an SSH Key Pair and make sure that the Public Key is specified in the add-toronto-covid-19-dashboard.yaml file (ssh_authorized_keys). The Private Key is held in the 'tf-cloud-init' file.

Here is a link to the City of Toronto's Open Data Portal: https://open.toronto.ca/

Note: Information about COVID-19 cases is gathered through external resources. The information provided may not be accurate. Use at your own risk.
