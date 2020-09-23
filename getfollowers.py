import requests
from bs4 import BeautifulSoup
import re

urlName = "https://bunshun.jp/articles/-/1"
url = requests.get(urlName)
soup = BeautifulSoup(url.content, "html.parser")

elems = soup.find_all("p")

return_string = ""
for elem in elems: 
  if ( not (elem.get("class")) and not(elem.string == "SCOOP!") and not(elem.string == "NEW") and not(elem.string == "ABJマークは、この電子書店・電子書籍配信サービスが、著作権者からコンテンツ使用許諾を得た正規版配信サービスであることを示す登録商標（登録番号6091713号）です。" )): 
    p_parent_class_name = elem.find_parent('div').get("class")#親要素のクラス名を取得
    if ( p_parent_class_name == ["article-body"] ):#親要素のクラス名がarticle-bodyの場合内容を出力
      elem_text = elem.string
      return_string = return_string + elem_text
print("結果：" + return_string) 