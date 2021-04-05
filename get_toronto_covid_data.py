import requests

url = "https://ckan0.cf.opendata.inter.prod-toronto.ca/api/3/action/package_show"
params = { "id": "64b54586-6180-4485-83eb-81e8fae3b8fe"}
package = requests.get(url, params = params).json()
#print(package["result"])

f = open("output_toronto_covid_api.txt", "w")

for idx, resource in enumerate(package["result"]["resources"]):
    if resource["datastore_active"]:
        url = "https://ckan0.cf.opendata.inter.prod-toronto.ca/api/3/action/datastore_search"
        p = { "id": resource["id"] }
        data = requests.get(url, params = p).json()
        #print(data['license_title'])
        # for key in data.keys():
        #     print(key)
        
        # for key2 in data['result'].keys():
        #     print(key2)

        records_data = data['result']['records']

        # We will now need to deal with pagination here to get all of the records
        while True:
            records_data = data['result']['records']
            for individual_records in records_data:
                f.write(str(individual_records)+'\n')
                print(individual_records)
            if 'next' in data['result']['_links'].keys():
                # print("Yes, there's another page")
                next_page_url = 'https://ckan0.cf.opendata.inter.prod-toronto.ca'+ data['result']['_links']['next']
                #print(next_page_url)
                data = requests.get(next_page_url).json()
            else:
                f.close()
                break