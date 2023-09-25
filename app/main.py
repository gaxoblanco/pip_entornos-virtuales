import utils
import read_csv
import charts
import matplotlib.pyplot as plt

#creo la lista de diccionarios 
# data = [
#     {'country': 'Colombia', 'population': 100},
#     {'country': 'Bolivia', 'population': 200},
#     {'country': 'Argentina', 'population': 300},
#     {'country': 'Argentina', 'population': 500},
# ]

def run():
    data = read_csv.read_csv('./app/data.csv')
    data = list(filter(lambda x: x['Country/Territory'] != 'South America', data))
    # ingreso que pais quiero graficar
    country = input("Type Country => ")
    # guardo el input del usuario en name
    name = country
    # le paso a la funcion population_by_country data y el input del usuario
    result = utils.population_by_country(data, country)
    print(result)
    # si el resultado tiene algun elemeneto 

    if len(result) > 0:
        country = result[0]
        labels, values = utils.get_population(country)
        charts.generate_bar_chart(name, labels, values)
    else:
        print('Country not found')

    # # uso la funcion get_world_population con generate_pie_chart
    # # tomo la columna 'Country' de data y la uso como key del diccionario
    # countries = list(map(lambda x: x['Country/Territory'], data))
    # # tomo la columna 'World Population Percentage' de data y la uso como value del diccionario
    # percentages = list(map(lambda x: x['World Population Percentage'], data))
    # creo el diccionario
    # charts.generate_pie_chart(countries, countries, percentages)


if __name__ == '__main__':
    run()