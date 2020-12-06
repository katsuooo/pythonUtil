'''
mongodb some interface

'''
from pymongo import MongoClient
import json
print('mongo-if start')

#
# shushu/ attend_202011 read
#
myClient = MongoClient('mongodb://localhost:27017')
myDb = myClient['shushu']
myCol = myDb['attend_202011']
x = myCol.find({})
xx = []
for i in x:
    del i['_id']
    xx.append(i)
    print(i)
    print('-'*10)
#print(xx)
with open('x.json', 'w', encoding='utf-8') as f:
    json.dump(xx, f, ensure_ascii=False, sort_keys=True, indent=4)
#
# shushu/ attend_202011 read
#
myClient = MongoClient('mongodb://localhost:27017')
myDb = myClient['shushu']
myCol = myDb['attend_edit_202011']
x = myCol.find({})
xx = []
for i in x:
    del i['_id']
    xx.append(i)
    print(i)
    print('-'*10)
#print(xx)
with open('xEdit.json', 'w', encoding='utf-8') as f:
    json.dump(xx, f, ensure_ascii=False, sort_keys=True, indent=4)
#--------------------
print('end')