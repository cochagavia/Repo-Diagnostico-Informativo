import json

with open('json1.json') as file:
    data = json.load(file)

def funcion1: 
    lista = []
    sorted_json_data = json.dumps(data["retweetCount"], sort_keys=True)
    for i in range(10):
        lista.append(sorted_json_data.pop)
    return lista
