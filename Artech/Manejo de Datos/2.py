import json

ruta = "JSON/e2.json"
with open(ruta, "r", encoding="utf-8") as f:
    data = json.load(f)

print("---------------------------------------------------------------")
print(data["personas"])
print("---------------------------------------------------------------")
print(data["personas"][0]["Nombre"])
print(data["personas"][0]["Apellido"])
print(data["personas"][0]["Edad"])
print(data["personas"][0]["Hobbies"][0])