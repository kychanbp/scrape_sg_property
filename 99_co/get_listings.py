import json
import requests

with open("config_99_co.json","r") as json_file:
    config = json.load(json_file)
    API_KEY = config['scraperapi']['api_key']

list_of_urls = [
    "https://www.99.co/api/v2/web/search/listings?query_type=city&property_segments=residential&listing_type=sale&rental_type=unit&page_size=999999999&page_num=1&zoom=11&show_future_mrts=true&show_cluster_preview=true&show_internal_linking=true"
]

proxies = {
  'http': f'http://scraperapi:{API_KEY}@proxy-server.scraperapi.com:8001',
}

NUM_RETRIES = 3

for url in list_of_urls: 

    for _ in range(NUM_RETRIES):
        try:
            response = requests.get(url, proxies=proxies, verify=False)
            if response.status_code in [200, 404]:
                ## escape for loop if the API returns a successful response
                break
        except requests.exceptions.ConnectionError:
            response = ''
    
    ## parse data if 200 status code (successful response)
    if response.status_code == 200:
        
        ## Example: parse data with beautifulsoup
        html_response = response.text
        print(html_response)
        