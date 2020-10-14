#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import datetime
import json
from requests_oauthlib import OAuth1Session
from dotenv import load_dotenv
import os
import analyse_sentimental_magnitude_and_score
import schedule
import time

load_dotenv()

now_time = datetime.datetime.now()

CK  = os.environ["CK"]
CS  = os.environ["CS"]
AT  = os.environ["AT"]
ATS = os.environ["ATS"]
twitter = OAuth1Session(CK, CS, AT, ATS)
# Twitter Endpoint(検索結果を取得する)
timeline_url = 'https://api.twitter.com/1.1/search/tweets.json'

# Enedpointへ渡すパラメーター
keyword = ["コロナ min_retweets:1000 " + "since:" + str(now_time.year) + '-' + str(now_time.month) + '-' + str(now_time.day - 1)] #20RT以上されてるツイートを取得
params ={
         'count' : 1000,      # 取得するtweet数
         'q'     :  keyword,# 検索キーワード
         'result_type': 'mixed',#時系列で取得
         'exclude': 'retweets'#RTされて表示されているツイートを除外
         }
def main():
    timeline_req = twitter.get(timeline_url, params = params, stream=True)
    if timeline_req.status_code == 200:
        res = json.loads(timeline_req.text)
        for line in res['statuses']:
            #print(line["created_at"], line["id"], line["text"], line["retweet_count"], line["entities"]["urls"][0]["url"], line["user"]["verified"])
            is_posted_user_verifined = line["user"]["verified"]
            tweet_text = line["text"]
            tweetId = line["id"]
            reliability_point = 70
            if line["entities"]["urls"] :
                print (line["entities"]["urls"][0]["url"])
                reliability_point += 20
            else:
                reliability_point -= 30
            if is_posted_user_verifined:
                reliability_point += 90
            reliability_point += analyse_sentimental_magnitude_and_score.load_sentimental( tweet_text )

            reply = "点数：" +  str( reliability_point )
            reply = ""
            if reliability_point > 70:
                reply =  "botによるツイート内容の信用度分析結果【"+ str( reliability_point ) +"points】\n"+"botによる自動ファクトチェックにより、ツイート内容が比較的 信用度の値が高い結果になりました。SNSでの情報の共有にはデマ・フェイクニュースに騙されないように真偽の程度を確認するようにしてください\n https://iinoten.github.io/tweet-test-bot"
            else:
                reply = "botによるツイート内容の信用度分析結果【"+ str( reliability_point ) + "points】\n " + "botによる自動ファクトチェックにより、ツイート内容の 信用度の値が低い結果になりました。これはあくまでもプログラムによる自動チェックの結果であり、真偽の確実な判断ではありません。情報の出所などを確認し、デマやフェイクニュースに気をつけてください。\n https://iinoten.github.io/tweet-test-bot"
            mention = {"status":reply, "in_reply_to_status_id":tweetId, "auto_populate_reply_metadata":True}
            resPost = twitter.post("https://api.twitter.com/1.1/statuses/update.json", params=mention)

    else: print("Failed: %d" % timeline_req.status_code)

schedule.every().days.at("08:00").do(main); # 毎朝8時にスクリプトを実行
while True:
    schedule.run_pending()
    time.sleep(1)

# コード実行の行をコメントアウト
#if __name__ == '__main__':
#    main()