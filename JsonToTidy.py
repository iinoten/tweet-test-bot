import json

json_open = open('./netnewsdata.json', 'r')
json_load = json.load(json_open)

print(json_load['data'][0])