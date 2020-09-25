import json
import math
 
json_open = open('./analysed_data/analysed_data_sepalate.json', 'r')
json_load = json.load(json_open)
analysed_news_data_array = json_load['analysed_data_sepalate']

for analysed_news_data in analysed_news_data_array:
  variable_sepalate_sentimental = 0
  hold_senti_score = 0
  for sepalate_list in analysed_news_data["sentence_return"]:
    sepalate_score_point = sepalate_list["sentence_analyse_result"]["score"]
    variable_sepalate_sentimental += math.fabs( hold_senti_score - sepalate_score_point )
    hold_senti_score = sepalate_score_point
  print(variable_sepalate_sentimental)