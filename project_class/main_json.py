
import json

from my_own_codes.project_class.main import data

with open("json", "r") as f:
    data = json.load(f)

print(data.items())

with open("json", "w") as f:
    json.dump(data, f)
print(data.items())