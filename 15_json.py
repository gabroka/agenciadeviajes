import json

menu = {
    "desayuno": {
        "beber": "Café",
        "comer": "Tostadas"
    },
    "almuerzo": {
        "beber": "agua",
        "comer": "sorrentinos"
    },
    "merienda": {
        "beber" : "mate",
        "comer" : "galletitas"
    },
    "cena": {
        "beber" : "cerveza",
        "comer" : "pizza"
    }
}

print("menú:", menu)

dump_json = json.dumps(menu)
print("dump_json:", dump_json)

menu2 = json.loads(dump_json)
print("menú2:", menu2)
