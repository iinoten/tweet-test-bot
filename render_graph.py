import matplotlib.pyplot as plt
import json
 
json_open = open('./analysed_netnewsdata.json', 'r')
json_load = json.load(json_open)
analysed_news_data_array = json_load['analysed_data']

# 対象データ
x = []
y = []

for index, analysed_result in enumerate(analysed_news_data_array):
  x.append(analysed_result["documentSentiment"]["magnitude"])
  y.append(analysed_result["documentSentiment"]["score"])
 
# figureを生成する
fig = plt.figure()
 
# axをfigureに設定する
ax = fig.add_subplot(1, 1, 1)
 
# axesに散布図を設定する
ax.scatter(x, y, c='b', s=1)
 
# 表示する
plt.savefig("scalar_plot_graph.jpg")