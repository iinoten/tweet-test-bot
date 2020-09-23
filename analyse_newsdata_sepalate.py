import requests 
import os
import json
from dotenv import load_dotenv

load_dotenv()
GOOGLE_LANG_API_KEY  = os.environ['GOOGLE_LANG_API_KEY']

json_open = open('./replaced_netnewsdata.json', 'r')
json_load = json.load(json_open)
news_data_array = json_load['data']
 
#APIキーを入力
key = GOOGLE_LANG_API_KEY

#APIのURL
url = 'https://language.googleapis.com/v1/documents:analyzeSentiment?key=' + key

analysed_data_json = []

for index, news_text in enumerate(news_data_array):
  #基本情報の設定 JAをENにすれば英語のテキストを解析可能
  header = {'Content-Type': 'application/json'}
  body = {
      "document": {
          "type": "PLAIN_TEXT",
          "language": "JA",
          "content": news_text
      },
      "encodingType": "UTF8"
  }
  #json形式で結果を受け取る。
  response = requests.post(url, headers=header, json=body).json()
  #解析の進行状況を出力
  print( str(index) + "番目の記事を分析中" )

  analysed_sentence_text_array = []
  for sentence_index, sentence_data in enumerate(response["sentences"]):
    analysed_sentence_text_array.append( sentence_data["sentiment"] )
  analysed_data_json.append({
    "text": news_text,
    "documentSentiment": response["documentSentiment"],
    "sentence_return": analysed_sentence_text_array
  })
  print( str(index) + "番目の記事の分析を完了" )

print ("全記事の分析を終了")
with open('./analysed_data/analysed_data_sepalate.json', 'w') as f:
    json.dump({"analysed_data_sepalate":analysed_data_json}, f, ensure_ascii=False, indent=4)