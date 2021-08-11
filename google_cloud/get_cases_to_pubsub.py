import os
import requests
from google.cloud import pubsub_v1

topic_name = 'projects/{project_id}/topics/{topic}'.format(
    project_id=os.getenv('GOOGLE_CLOUD_PROJECT'),
    topic='test_topic',  # Set this to something appropriate.
)

subscription_name = 'projects/{project_id}/subscriptions/{sub}'.format(
    project_id=os.getenv('GOOGLE_CLOUD_PROJECT'),
    sub='woohoo_this_works',  # Set this to something appropriate.
)

def publish_messages(project_id, topic_id, message):
    """Publishes multiple messages to a Pub/Sub topic."""
    # [START pubsub_quickstart_publisher]
    # [START pubsub_publish]
    from google.cloud import pubsub_v1

    # TODO(developer)
    #project_id = "covid-canada-dashboard"
    #topic_id = "test_topic"

    publisher = pubsub_v1.PublisherClient()
    # The `topic_path` method creates a fully qualified identifier
    # in the form `projects/{project_id}/topics/{topic_id}`
    topic_path = publisher.topic_path(project_id, topic_id)
    print(topic_path)

    #data = f"Message number {n}"
    #data = "THIS WORKS! Awesome job Braveenth!"
    data = message
    # Data must be a bytestring
    data = data.encode("utf-8")
    # When you publish a message, the client returns a future.
    future = publisher.publish(topic_path, data)
    print(future.result())

    print(f"Published messages to {topic_path}.")
    # [END pubsub_quickstart_publisher]
    # [END pubsub_publish]

url = "https://ckan0.cf.opendata.inter.prod-toronto.ca/api/3/action/package_show"
params = { "id": "64b54586-6180-4485-83eb-81e8fae3b8fe"}
package = requests.get(url, params = params).json()
#print(package["result"])

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
                publish_messages("covid-canada-dashboard","test_topic", str(individual_records))
                #print(individual_records)
            if 'next' in data['result']['_links'].keys():
                # print("Yes, there's another page")
                next_page_url = 'https://ckan0.cf.opendata.inter.prod-toronto.ca'+ data['result']['_links']['next']
                #print(next_page_url)
                data = requests.get(next_page_url).json()
            else:
                break
