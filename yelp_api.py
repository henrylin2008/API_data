import requests
from requests_oauthlib import OAuth1

consumer_key = ''
consumer_secret = ''
token = ''
token_secret = ''

auth = OAuth1(consumer_key, consumer_secret,
              token, token_secret)

url = "https//api.yelp.com/v2/search"

params = {
    "term": "food",
    "location": "San Francisco",

}


r = requests.get(url, auth=auth)

print(r.text)
