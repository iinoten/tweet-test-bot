import matplotlib.pyplot as plt
import json
 
json_open = open('./analysed_netnewsdata.json', 'r')
json_load = json.load(json_open)
analysed_news_data_array = json_load['analysed_data']
 
# figureを生成する
fig = plt.figure()
 
# axをfigureに設定する
ax = fig.add_subplot(1, 1, 1)
 
# axesに散布図を設定する
for index, analysed_result in enumerate(analysed_news_data_array):
  ax.scatter(x=len(analysed_result["text"]), y=analysed_result["documentSentiment"]["magnitude"], c='b', s=1)
 
# 表示する
plt.savefig("textlength_magnitude_graph.jpg")