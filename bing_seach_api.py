# Import required modules.
from azure.cognitiveservices.search.websearch import WebSearchAPI
from azure.cognitiveservices.search.websearch.models import SafeSearch
from msrest.authentication import CognitiveServicesCredentials

import csv

topic_list = ['topic1','topic2','topic3','topic4','topic5','topic6']
#
# Replace with your subscription key.
subscription_key = "YOUR_KEY"

# Instantiate the client and replace with your endpoint.
client = WebSearchAPI(CognitiveServicesCredentials(subscription_key), base_url = "https://api.cognitive.microsoft.com/bing/v7.0")
count = 0

for topic in topic_list:
    url_list = list()


    web_data = client.web.search(query=topic,count=50)   #looks for the topic into microsoft bing search and gives upto top 50 search results from bing.


    print("\r\nSearched for Query# \" %s \"" %topic)
#number of topics searched so far
    count+=1
    print('num of topics searched - %i' % count)

    if hasattr(web_data.web_pages, 'value'):

        for i in range(len(web_data.web_pages.value)):

            with open('/home/chaitanya/Documents/bing_jsons/new_search2.csv', 'a') as fp:
                filewriter = csv.writer(fp)
                url = web_data.web_pages.value[i].url
                name = web_data.web_pages.value[i].name
                snippet = web_data.web_pages.value[i].snippet
                filewriter.writerow([topic,name,url,snippet]) #create a csv having the topic, name, url and snippet

    else:
        print("Didn't find any web pages...for "+topic) #if there are no search results
