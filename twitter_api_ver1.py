import json, config
from requests_oauthlib import OAuth1Session


CK = CONSUMER_KEY
CS = CONSUMER_SECRET
AT = ACCESS_TOKEN
ATS = ACCESS_TOKEN_SECRET
twitter = OAuth1Session(CK, CS, AT, ATS)    


# -*- coding: utf-8 -*-
from flask import Flask, jsonify, abort, make_response, request

# import json

api = Flask(__name__)

@api.route('/get_tweets', methods=['GET'])
def get_tweets():
    account_id = request.args.get('account_id')
    tweets_count = request.args.get('tweets_count')
    url = "https://api.twitter.com/1.1/statuses/user_timeline.json?user_id={}&count={}".format(account_id, tweets_count)
    req = twitter.get(url)
    if req.status_code == 200:
        timeline = json.loads(req.text)
        data = []
        
        for tweet in timeline:
            data.append({'created_at':tweet['created_at'], 'text':tweet['text'],'favorite_count':tweet['favorite_count'], 'retweet_count':tweet['retweet_count']})
        return str(data)
    else:
        print("ERROR: %d" % req.status_code)

if __name__ == '__main__':
    api.run(debug=True)