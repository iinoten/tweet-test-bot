#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import datetime
import json
from requests_oauthlib import OAuth1Session

now_time = datetime.datetime.now()

CK  =
CS  = 
AT  = 
ATS = 
twitter = OAuth1Session(CK, CS, AT, ATS)
# Twitter Endpoint(検索結果を取得する)
timeline_url = 'https://api.twitter.com/1.1/search/tweets.json'

# Enedpointへ渡すパラメーター
keyword = ["竹内 min_retweets:500 " + "since:" + str(now_time.year) + '-' + str(now_time.month) + '-' + str(now_time.day - 1)] #20RT以上されてるツイートを取得
params ={
         'count' : 1,      # 取得するtweet数
         'q'     :  keyword,# 検索キーワード
         'result_type': 'mixed',#時系列で取得
         'exclude': 'retweets'#RTされて表示されているツイートを除外
         }
timeline_req = twitter.get(timeline_url, params = params)
if timeline_req.status_code == 200:
    res = json.loads(timeline_req.text)
    for line in res['statuses']:
        print(line["created_at"], line["id"], line["text"], line["retweet_count"], line["entities"]["urls"][0]["url"], line["user"]["verified"])
        tweetId = line["id"]
        reply = "悲しいです"
        mention = {"status":reply, "in_reply_to_status_id":tweetId, "auto_populate_reply_metadata":True}
        resPost = twitter.post("https://api.twitter.com/1.1/statuses/update.json", params=mention)

else: print("Failed: %d" % timeline_req.status_code)
