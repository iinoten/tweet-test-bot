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
keyword = ["マスク"]

params ={
         'count' : 5,      # 取得するtweet数
         'q'     :  keyword# 検索キーワード
         }

req = twitter.get(url, params = params)

if req.status_code == 200:
    res = json.loads(req.text)
    for line in res['statuses']:
        test = "honyahonya"
        tweet_degree_point = 100
        if ( not bool( line['user']['verified'] ) ) : tweet_degree_point -= 10      #公認バッジ付きのアカウントでないなら-10ポイント
        if  line['user']['statuses_count'] < 40000  : tweet_degree_point -= 10#総ツイート数が4万以内なら-10ポイント
        if  line['user']['default_profile'] : tweet_degree_point -= 10              #プロフィール文が初期のままなら-10ポイント
        if  line['user']['default_profile_image']  : tweet_degree_point -= 10    #アイコンが初期のままなら-10ポイント
        if  line['entities']['urls']  : tweet_degree_point -= 10                      #参考URLとかがなかったら-10ポイント

        print( "https://twitter.com/" + line['user']['screen_name'] + "/status/" + line['id_str'] ) #ツイートのURLを表示
        print( tweet_degree_point ) #評価の点数を表示
        print('*******************************************')
else:
    print("Failed: %d" % req.status_code)