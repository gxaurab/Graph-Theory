import requests
from bs4 import BeautifulSoup

url = 'https://www.sharesansar.com/company/RFPL'

res = requests.get(url)
htmlData = res.content
parsedData = BeautifulSoup(htmlData, "html.parser")
desired_part = parsedData.find('table',id='myTableCFloorsheet')

print(desired_part.prettify())
