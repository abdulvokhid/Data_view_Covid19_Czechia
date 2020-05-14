import requests             #used for http request
from bs4 import BeautifulSoup  #extracts data from html

page = requests.get('https://www.worldometers.info/coronavirus/country/czech-republic/')

soup = BeautifulSoup(page.text, 'html.parser')

total_czech = soup.find(class_='col-md-8')
total_czech_cases = total_czech.find_all(class_='content-inner')

for total_czech in total_czech_cases:
    print(total_czech.text)   