import requests 
import os
from dotenv import load_dotenv

load_dotenv()

GOOGLE_LANG_API_KEY  = os.environ['GOOGLE_LANG_API_KEY']

#APIキーを入力
key = GOOGLE_LANG_API_KEY

#感情分析したいテキスト
text = "ありえんよさみ!w 無限に泣きをしまつ。○○が尊すぎて鉄板ネタに大声でゲラゲラ笑ってる(真顔) そして一瞬で鬱になった"

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

#分析の結果をコンソール画面で見やすく表示
print(response["documentSentiment"])