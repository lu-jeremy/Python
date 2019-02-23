import requests
from bs4 import BeautifulSoup

data = requests.get('http://world.bymap.org/Population.html')

data_content = BeautifulSoup(data.content, 'html.parser')

# table = data_content.find_all(class_ = 'data')
table = data_content.find_all('table')

tbody = table[0].find_all('tbody')

td = tbody[0].find_all('td')

thead = data_content.find_all('thead')

countries = []
population = []
for var in td:
    try:
        countries.append(var['data-html'])
    except:
        pass

for i in range(len(td)):
    try:
       
        td[i]['data-html']           # don't delete this line because 
                                     #it's trying to print 
                                     #if it is not a country, it will go to the exception
        population.append(td[i+1].text)
    except:
        pass

for var in range(242):
    print(countries[var], population[var])
# put on graph

# th = table_headers[0].find_all('th')

# tbody = data_content.find_all('tbody')

# td = data_content.find_all('td')

# for var in th:
#     print(var['data-coltype'])

# coltype = td[0].find_all('data-wiki')

# for var in coltype:
#     print(var)

##table_headers = data_content.find_all('th', attrs = {'data-coltype': 'name'})
##
##for v in table_headers:
##    print(v)
    

##column_headers = [th.getText() for th in 
##                  data_content.findAll('tr', limit=2)[1].findAll('th')]
##
##print(column_headers)
