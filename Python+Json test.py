import json

a = 30

x = {
  "name": "John",
  "age": (a),
  "city": "New York"
}

y = json.dumps(x)

print(json.loads(y)["age"])
