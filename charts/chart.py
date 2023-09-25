# usamos la li matplotlib para graficar un chart

import matplotlib.pyplot as plt

def generate_pie_chart():
    labels = ['Python', 'Java', 'Dart', 'Go']
    values = [45, 30, 15, 10]

    fig, ax = plt.subplots()
    ax.pie(values, labels=labels)
    plt.savefig('pie.png')
    plt.close()
    

if __name__ == '__main__':
    generate_pie_chart()

