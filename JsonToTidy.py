import json

json_open = open('./netnewsdata.json', 'r')
json_load = json.load(json_open)
news_data_array = json_load['data']

form_news_data_array = []
for index, news_item in enumerate(news_data_array):
  replaced_news_text = news_item.replace("\u3000", "")
  replaced_news_text = news_item.replace("None", "")
  if not(replaced_news_text==''): form_news_data_array.append(replaced_news_text)

with open('./replaced_netnewsdata.json', 'w') as f:
    json.dump({"data":form_news_data_array}, f, ensure_ascii=False, indent=4)