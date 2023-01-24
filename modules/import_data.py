import json


def get_data():

    ruta_data = "../data/productos.json"
    with open(ruta_data) as data:
        data = json.load(data)

    return data 