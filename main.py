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
timeline_url = 'https://api.twitter.com/1.1/search/tweets.json'

#Twitter フォロワー数を取得する エンドポイント
follower_url = 'https://api.twitter.com/1.1/followers/ids.json'

# Enedpointへ渡すパラメーター
keyword = ["い min_retweets:50"]#20RT以上されてるツイートを取得

params ={
         'count' : 1000,      # 取得するtweet数
         'q'     :  keyword,# 検索キーワード
         'result_type': 'mixed',#時系列で取得
         'exclude': 'retweets'#RTされて表示されているツイートを除外
         }

timeline_req = twitter.get(timeline_url, params = params)
followers_req = twitter.get(follower_url, params = {'screen_name': '@iinoten'})

if timeline_req.status_code == 200:
    res = json.loads(timeline_req.text)
    for line in res['statuses']:
        if ( line["user"]["followers_count"] <= 500 ): #フォロワー数が500以下のツイートを表示 
            print( line["text"] )
            print( "https://twitter.com/" + line['user']['screen_name'] + "/status/" + line['id_str'] ) #ツイートのURLを表示
            print('*******************************************')
else:
    print("Failed: %d" % timeline_req.status_code)