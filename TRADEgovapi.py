from six.moves import urllib
import json
import requests
import lxml.etree
import lxml.html
from bs4 import BeautifulSoup
from config import LAST_ACCESS, post_listing

# default image: https://s3images.coroflot.com/user_files/individual_files/193166_af0b5dxkqswezmih86xhrjf_t.jpg
# d4289cd6-563d-4ec6-b1b5-82d49a15ad07

def TRADEGOV_update():
    url = makeParams('electricity')
    results = parse_request(url)['results']
    collect_leads(results)

def collect_leads(lead_data):
    count = 0
    pub_date = ''
    for result in lead_data:
        # print(result)
        print('*************** RESULT # ' + str(count) + " ***************")
        # print('published_at: ', result['publish_date'])
        # print('hosted_url: ', result['url'])
        # print('source: ', result['source'])
        # print('contract_number: ', result['id'])
        # # print('industries: ', result['industries'])
        # print('country: ', result['country_name'])
        # print('description: ', result['description'])
        # print('summary: ', result['description'][:150])
        pub_date = result['publish_date'][0:19] + result['publish_date'][23:]
        if int(pub_date[5:7]) == int(LAST_ACCESS[5:7]) and int(pub_date[8:10]) == int(LAST_ACCESS[8:10]):
            print('update over')
            return

        # print(pub_date[0:5]+pub_date[7:])
        # try:
        #     print('implementing_entity: ', result['funding_source'])
        #     print('reference_number: ', result['reference_number'])
        #     print('click link: ', result['click_url'])
        # except:
        #     pass
        post_listing('keywords', pub_date, pub_date, result['title'], result['description'], result['description'][:150], 'd4289cd6-563d-4ec6-b1b5-82d49a15ad07')
        count += 1

# 2019-10-01T00:00:00+02:00
# 2019-01-24T19:52:27.000+00:00
# result['publish_date'][0:19] + result['publish_date'][23:]

def makeParams(query):
    API_KEY = 'gWSb73PtNBtYufU04rzVl8gK'
    request_url = 'https://api.trade.gov/v1/trade_leads/search?api_key=' + API_KEY + '&q=' + query
    return request_url

def parse_request(url):
    r = requests.get(url)
    data_dict = r.json()
    return data_dict


TRADEGOV_update()
