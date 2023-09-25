def get_population(population):
    # keys = ['col', 'bol', 'arg']
    # values = [100, 200, 300]
    # ----------------------------------------------------------------
    # guardo el index a trabajar
    dataIndex = population
    # itero por el diccionaro dataIndex y todos los elementos que en su key tengan la palabra 'Population' los guardo en un diccionario
    population = {key: value for key, value in dataIndex.items() if 'Population' in key}
    #modifico el nombre de la key borrando 'Population'
    population = {key.replace('Population', ''): value for key, value in population.items()}


    labels = population.keys()
    values = population.values()
    return labels, values

# A = 'Hola'

# en el item Country/Territory busco el pais que ingrese por teclado
def population_by_country(data, country):
    # busco en la data el elemento que tenga la key country y el value que ingrese por teclado
    result = [element for element in data if element['Country/Territory'] == country]
    return result

