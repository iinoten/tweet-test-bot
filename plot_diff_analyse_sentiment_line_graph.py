import matplotlib.pyplot as plt
import json
 
json_open = open('./analysed_data/analysed_data_sepalate.json', 'r')
json_load = json.load(json_open)
analysed_news_data_array = json_load['analysed_data_sepalate']

""" 
# figureを生成する
fig = plt.figure()
 
# axをfigureに設定する
ax = fig.add_subplot(1, 1, 1)
"""
 
# axesに散布図を設定する
for index, analysed_result in enumerate(analysed_news_data_array):
  sentence_data_X = []
  sentence_data_Y = []
  for sentence_index, target_sentence in enumerate( analysed_result["sentence_return"] ):
    sentence_data_X.append( sentence_index )
    sentence_data_Y.append( target_sentence["sentence_analyse_result"]["score"] )
    print( sentence_index, target_sentence["sentence_analyse_result"]["score"] )
  plt.plot( sentence_data_X, sentence_data_Y, linewidth=0.2 )



# 表示する
plt.savefig("./graphs/sentence_article_line_graph.jpg")