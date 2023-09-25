import matplotlib.pyplot as plt

def generate_bar_chart(name, labels, values):
    fig, ax = plt.subplots()
    ax.bar(labels, values)
    plt.show()

def generate_pie_chart(labels, values):
    fig, ax = plt.subplots()
    ax.pie(values, labels=labels, autopct='%1.1f%%')
    plt.show()
    # guardo la imagen con el name.png
    fig.savefig(f'./app/{name}.png')
    plt.close()

def generate_line_chart(labels, values):
    fig, ax = plt.subplots()
    ax.plot(labels, values)
    plt.show()

if __name__ == '__main__':
    labels = ['A', 'B', 'C']
    values = [1, 4, 2]
    generate_bar_chart(name, labels, values)
    generate_pie_chart(labels, values)
    generate_line_chart(labels, values)