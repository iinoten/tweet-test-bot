import requests 
import os
from dotenv import load_dotenv
import math

def load_sentimental(text):
  load_dotenv()
  GOOGLE_LANG_API_KEY  = os.environ['GOOGLE_LANG_API_KEY']
  #APIキーを入力
  key = GOOGLE_LANG_API_KEY

  #APIのURL
  url = 'https://language.googleapis.com/v1/documents:analyzeSentiment?key=' + key


  #基本情報の設定 JAをENにすれば英語のテキストを解析可能
  header = {'Content-Type': 'application/json'}
  body = {
      "document": {
          "type": "PLAIN_TEXT",
          "language": "JA",
          "content": text
      },
      "encodingType": "UTF8"
  }
  #json形式で結果を受け取る。
  response = requests.post(url, headers=header, json=body).json()
  #感情スコアの変動のための変数を初期化
  variable_sepalate_sentimental = 0
  #前回に処理しておいた感情スコアを保持しておくための変数を初期化
  hold_senti_score = 0
  for sentence_result in response["sentences"]:
    sepalate_score_point = sentence_result["sentiment"]["score"]
    variable_sepalate_sentimental += math.fabs( hold_senti_score - sepalate_score_point )
    #保持するためのスコアに今回のスコアを保存
    hold_senti_score = sepalate_score_point
  importance_of_magnitude_point = -20
  importance_of_diff_sentimental_score_point = -30
  analyse_sentimental_result = response["documentSentiment"]["magnitude"] * importance_of_magnitude_point + variable_sepalate_sentimental * importance_of_diff_sentimental_score_point
  return( analyse_sentimental_result )