# from util import wait_element
import selenium

import re
#
#
# test_string = '44.5M\n12k\n6.5G\n12p\n10'
#
# result = re.findall(r'(\d+(?:\.\d+)?)\s*([kmgtp]?)?', test_string, re.IGNORECASE)
#
# print(result)

# for value, unit in regex.findall(test_string):
#     print(int(float(value) * (1024**order.index(unit.lower()))))

from collections import defaultdict
from selenium import webdriver
driver = webdriver.Firefox()

url = 'https://github.com/python'
driver.get(url)
lista_li = driver.find_elements_by_xpath('//ol/li')
resultados = []
mapeamento = defaultdict(lambda: 1)
mapeamento['k'] = 1000
mapeamento['m'] = 1000000
mapeamento['g'] = 1000000000
mapeamento['t'] = 1000000000000

for l in lista_li:
    url = l.find_element_by_xpath('.//a').get_attribute('href')
    nome = l.find_element_by_xpath('.//span/span[2]').text
    lista_pinned = l.find_elements_by_xpath(".//a[contains(@class,'pinned-item-meta')]")
    estrelas = lista_pinned[0].text
    estrelas_n, estrelas_e = re.findall(r'(\d+(?:\.\d+)?)\s*([kmgtp]?)?', estrelas, re.IGNORECASE)[0]
    estrelas = float(estrelas_n)*mapeamento[estrelas_e]
    forks = lista_pinned[1].text
    forks_n, forks_e = re.findall(r'(\d+(?:\.\d+)?)\s*([kmgtp]?)?', forks, re.IGNORECASE)[0]
    forks = float(forks_n)*mapeamento[forks_e]
    resultados.append({'url': url, 'nome': nome, 'estrelas': estrelas, 'forks': forks})

print(resultados)
# print(lista_li[0])