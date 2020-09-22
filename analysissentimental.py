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
  #分析の結果をコンソール画面で見やすく表示
  print(response["documentSentiment"])
  analysed_data_json.append({
    "text": news_text,
    "documentSentiment": response["documentSentiment"]
  })
print (analysed_data_json)
with open('./analysed_netnewsdata.json', 'w') as f:
    json.dump({"analysed_data":analysed_data_json}, f, ensure_ascii=False, indent=4)