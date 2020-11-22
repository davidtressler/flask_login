
import json
from tinydb import TinyDB, Query
db = TinyDB('db/db.json', indent=4)

table = db.table('userdata')


User = Query()

user_input = "bob@bob.com"

user_output = db.search(User.email == user_input)

print("user_output",user_output[0]['password'])

# try:
#     if user_output[0] != None:
#         print("User already exists")
#     else:
#         pass
# except:
#         db.insert({'name': user_input})
#         print("New User Added ", user_input)
#
# # el = db.get(User.name == 'John')

def get_password():
    print()


#print(el.doc_id)

#
# with open('db/db.json') as json_file:
#     data = json.load(json_file)
#
# print(data['_default']['1']['name'])
