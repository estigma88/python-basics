import json

userJSON = '{"first":"asfasf"}'

user = json.loads(userJSON)

print(user)
print(user['first'])

userj=json.dumps(user)

print(userj)
