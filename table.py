from tinydb import TinyDB
db=TinyDB('db.json')
smartphone={'user_id':1,'username':'Samsung'}
smartphone2={'user_id':2,'username':'Apple'}
smartphone3={'user_id':3,'username':'Huwaei'}
smartphone4={'user_id':4,'username':'oppo'}
db.insert(smartphone)
db.insert(smartphone2)
db.insert(smartphone3)
db.insert(smartphone4)