import matplotlib.pyplot as plt
import json
 
json_open = open('./analysed_data/analysed_data_sepalate.json', 'r')
json_load = json.load(json_open)
analysed_news_data_array = json_load['analysed_data_sepalate']
 
# figureを生成する
fig = plt.figure()
 
# axをfigureに設定する
ax = fig.add_subplot(1, 1, 1)
 
# axesに散布図を設定する
for index, analysed_result in enumerate(analysed_news_data_array):
  for target_sentence in analysed_result["sentence_return"]:
    ax.scatter(x=len(target_sentence["sentence_txt"]), y=target_sentence["sentence_analyse_result"]["score"], c='b', s=0.3)
 
# 表示する
plt.savefig("./graphs/sentence_analyse_plot.jpg")