import json

data = {
    "a": "Olzhas",
    "z": "I live in Almaty",
    "d": ['1.png', '2.wav'],
    'v': 'direct',
    'b': None,
}

class MyEncoder(json.JSONEncoder):
    def default(self, o):
        if isinstance(o, set):
            return list(o)
        return o
json_str = json.dumps({1, 2, 3, 4, 5}, cls = MyEncoder)
print(type(json_str))

json_str = json.dumps('привет', ensure_ascii=False)
print(json_str)


py_obj = json.loads(json_str)
print(py_obj)


json_str = json.dumps(data, indent = 4)
print(json_str)

json_str = json.dumps(data, sort_keys = True, indent = 3)
print(json_str)


json_string = '''
    {
        "students": [
            {
                "id": 1,
                "name":"Rozi",
                "age": 21,
                "full-time":true
            },
            {
                "id": 2,
                "name":"Olzhas",
                "age": 20,
                "full-time":false
            }
        ]
    }
'''
data = json.loads(json_string)
# data['test'] = True

new_json = json.dumps(data)
new_json1 = json.dumps(data, indent = 4)

print(new_json)


data = {
    "firstName": "Jane",
    "lastName": "Doe",
    "hobbies": ["running", "sky diving", "singing"],
    "age": 35,
    "children": [
        {
            "firstName": "Alice",
            "age": 6
        },
        {
            "firstName": "Bob",
            "age": 8
        }
    ]
}


