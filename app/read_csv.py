import csv

def read_csv(path):
  with open(path, 'r') as csvfile:
    reader = csv.reader(csvfile, delimiter=',')
    header = next(reader)
    data = []
    for row in reader:
      iterable = zip(header, row)
      contry_dict = {key: value for key, value in iterable}
      data.append(contry_dict)
    return data
    
if __name__ == '__main__':
  data =   read_csv('./app/data.csv')
  print(data[0])


























  #Reto de la clase 38
  #Lee un CSV para calcular el total de gastos
  '''
  #Guia
  Para resolver este desafío, debes utilizar el archivo data.csv que contiene los datos de los gastos de una empresa. El archivo tiene dos columnas: el nombre del área y el total de gastos del año.

Tu reto es implementar la función read_csv que lee el archivo CSV y calcula el total de gastos de la empresa. Para leer el archivo CSV, puedes utilizar la función open y el módulo csv de Python. Una vez que hayas leído los datos, puedes calcular el total de gastos implementando la lógica que consideres necesaria.

Ejemplo

Input: data.csv
Administration,10
Marketing,20
Purchasing,10
Human Resources,20

Output:
60
'''
'''
#Mi solucion
import csv

def read_csv(path):
   # Tu código aquí 👇
   with open(path, 'r') as csvfile:
      reader = csv.reader(csvfile)
      lector_dict = dict(reader)
      total = sum(int(i) for i in lector_dict.values())
   return total

response = read_csv('./data.csv')
print(response)
'''