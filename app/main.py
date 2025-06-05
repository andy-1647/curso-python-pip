#Inportando el modulo que cree en main
import utils
import read_csv
import charts


#Esto la verdad no me funciono
def run():
  data = read_csv.read_csv('data.csv')
  data = list(filter(lambda item : item['Continent'] == 'South America',data))

  countries = list(map(lambda x : x['Country'], data))
  percentages = list(map(lambda x : x['World Population Percentage'], data))
  charts.generate_pie_chart(countries, percentages)

  country = input('Type Country => ')

  result = utils.population_by_country(data, country)

  if len(result) > 0:
    country = result[0]
    labels, values = utils.get_population(country)
    charts.generate_bar_chart(labels, values)

   

#Haciendolo de forma dinamica, para que se ejecute como script, desde la terminal
if __name__ == '__main__':
    run()















































'''
#Inportando el modulo que cree en main
import utils

data = [

        {
          'Country': 'Colombia',
          'Populatin': 500
        },
        {
           'Country': 'Bolivia',
           'Population': 300
        }
    ]

def run():
    keys, values = utils.get_population()
    print(keys, values)
    country = input('Type Country => ')

    result = utils.population_by_country(data, country)
    print(result)
#Haciendolo de forma dinamica, para que se ejecute como script, desde la terminal
if __name__ == '__main__':
    run()
'''