#Gráficas con matplotlib: Bar Chart y Pie Chart en python
#Primer ejemplo
import matplotlib.pyplot as plt

#Proyecto de un estudiante
def generate_bar_chart(labels, values):
    fig, ax = plt.subplots()
    ax.bar(labels, values)
    plt.savefig('bar.png')
    plt.close()

def generate_pie_chart(labels, values):
    fig, ax = plt.subplots()
    ax.pie(values, labels=labels)
    ax.axis('equal')
    plt.savefig('pie.png')
    plt.close()




if __name__ == '__main__':
    labels = ['a','b','c']
    values = [10, 40, 800]
    #generateBarChart(labels,values)
    generate_pie_chart(labels, values)
