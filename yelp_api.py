import requests
from requests_oauthlib import OAuth1

consumer_key = ''
consumer_secret = ''
token = ''
token_secret = ''
# test 

auth = OAuth1(consumer_key, consumer_secret,
              token, token_secret)
#
# url = "https//api.yelp.com/v2/search"
#
# params = {
#     "term": "food",
#     "location": "San Francisco",
#
# }
#
#
# r = requests.get(url, auth=auth, params=params)
#
# print(r.text)

def do_search(term='Food', location='San Francisco'):
    base_url = 'https://api.yelp.com/v2/search'
    term = term.replace(" ", "+")
    location = location.replace(" ", "+")
    url = "{base_url}?term={term}&location={location}".format(
            base_url=base_url,
            term=term,
            location = location)
    )

    params ={
        "term": term,
        "location": location
    }
    auth = OAuth1(consumer_key, consumer_secret,
              token, token_secret)

    r = requests.get(url, auth=auth, params=params)
    return r.json()

search1 = do_search()

for i in search1["businesses"]:
    print(i["name"])
    print(i["phone"])
    print(i["location"]["display_address"])
    print(i["location"]["city"])
    print(i.get('location').get('area'))
    print('\n')
