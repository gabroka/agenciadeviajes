from tabulate import tabulate
rios1 = [['Almanzora', 105],
         ['Guadiaro', 79],
         ['Guadalhorce', 154],
         ['Guadalmedina', 51.5]]
print(tabulate(rios1, headers=['Río', 'Long. (Km.)']))

data = [
    {"Nombre": "Juan", "Edad": 30, "Ciudad": "Madrid"},
    {"Nombre": "Ana", "Edad": 25, "Ciudad": "Barcelona"},
    {"Nombre": "Luis", "Edad": 35, "Ciudad": "Valencia"}
]

print(tabulate(data, headers="keys"))