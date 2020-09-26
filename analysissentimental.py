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


#基本情報の設定 JAをENにすれば英語のテキストを解析可能
header = {'Content-Type': 'application/json'}
body = {
    "document": {
        "type": "PLAIN_TEXT",
        "language": "JA",
        "content": "おはようございみゃす☁左ひざを痛めみゃした…曲げると痛い…。特別に何かした記憶もなく、風呂上がりに感じる痛み…。ぴえん訴えかける顔さて、今日は月末最後の金曜日「プレミアム文房具デー！」お気に入りの文房具を見つけに、あのお店に行こう！"
    },
    "encodingType": "UTF8"
}
#json形式で結果を受け取る。
response = requests.post(url, headers=header, json=body).json()
#分析の結果をコンソール画面で見やすく表示
print(response)
