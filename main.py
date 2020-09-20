#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import json
import config
from requests_oauthlib import OAuth1Session
import os
from dotenv import load_dotenv

load_dotenv()

CK  = os.environ['CK']
CS  = os.environ['CS']
AT  = os.environ['AT']
ATS = os.environ['ATS']

twitter = OAuth1Session(CK, CS, AT, ATS)

# Twitter Endpoint(検索結果を取得する)
url = 'https://api.twitter.com/1.1/search/tweets.json'

# Enedpointへ渡すパラメーター
keyword = ["コロナ"]

params ={
         'count' : 100,      # 取得するtweet数
         'q'     :  keyword# 検索キーワード
         }

req = twitter.get(url, params = params)

if req.status_code == 200:
    res = json.loads(req.text)
    for line in res['statuses']:
        if line["retweet_count"] >500: #RT数が500以上のツイートを表示 
            print( "https://twitter.com/" + line['user']['screen_name'] + "/status/" + line['id_str'] ) #ツイートのURLを表示
            print('*******************************************')
else:
    print("Failed: %d" % req.status_code)