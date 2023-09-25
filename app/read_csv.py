import csv

def read_csv(path):
    with open(path, 'r') as csvfile:
        reader = csv.reader(csvfile, delimiter=',')
        # creo paso a paso el diccionario
        header = next(reader)
        # guardo la lista de diccionarios
        data = []
        for row in reader:
            # convino el key = value
            iterable = zip(header, row) # obtengo un array de tuplas
            # print(list(iterable))
            country = {key: value for key, value in iterable}
            data.append(country)
        return data

if __name__ == '__main__':
    data = read_csv('./app/data.csv')
    # print(data[10])

    # guardo el index a trabajar
    dataIndex = data[10]
    # itero por el diccionaro dataIndex y todos los elementos que en su key tengan la palabra 'Population' los guardo en un diccionario
    population = {key: value for key, value in dataIndex.items() if 'Population' in key}
    #modifico el nombre de la key borrando 'Population'
    population = {key.replace('Population', ''): value for key, value in population.items()}
    print(population)