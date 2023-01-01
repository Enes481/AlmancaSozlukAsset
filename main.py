import requests
from bs4 import BeautifulSoup
import pandas as pd
import json
import lxml


"""headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36'}
url = "https://almancakonulari.com/a1-seviye-almanca-kelimeler/#gsc.tab=0"

result = requests.get(url)
soup = BeautifulSoup(result.text, 'html.parser')
div = soup.find('div', class_='entry-content clearfix')


list = []

words = div.find_all('table', class_='table table-bordered')"""


"""for word in div.find_all('table', class_='table table-bordered'):"""
"""for word1 in words[0].find_all('tbody'):
    rows = word1.find_all('tr')
    for row in rows:
        each_word = row.find_all('td')
        case = {
            "index": float(each_word[0].string),
            "word": each_word[1].string,
            "meaning": each_word[2].string
        }
        list.append(case)



with open('almancaKelimeler2.json', 'w', encoding='utf-8') as f:
    json.dump(list, f, ensure_ascii=False, indent=4)"""

import pandas as pd
from bs4 import BeautifulSoup
import requests

url = 'https://almancakonulari.com/a1-seviye-almanca-kelimeler/#gsc.tab=0'
page = requests.get(url)
soup = BeautifulSoup(page.content, 'html.parser')

# restrict search to div with class entry-content clearfix
div = soup.find('div', attrs={'class': 'entry-content clearfix'})

# get all h3
h3 = div.find_all('h3')
h3 = [' '.join(i.get_text().strip().split()) for i in h3] # clean text

# get all tables with pandas
df = pd.read_html(page.content)
df = df[-len(h3):] # only keep relevant tables, i.e. the last n tables where n == len(h3)

# rename all columns of the tables
for i in df:
    i.columns = ['index', 'word', 'meaning']

# create output dict
output_dict = {h3[n]: i.to_dict(orient='records') for n, i in enumerate(df)}

with open('almancaKelimeler1.json', 'w', encoding='utf-8') as f:
    json.dump(output_dict, f, ensure_ascii=False, indent=4)