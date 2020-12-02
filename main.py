from selenium import webdriver
from bs4 import BeautifulSoup
import  csv
driver = webdriver.Chrome("C:\scraping\chromedriver.exe")
titles = []
tags = []
descriptions = []
dates = []
i = 1
j = i

while i<3:
        url = 'https://www.infrastructureinvestor.com/news-analysis/deals/page/' + str(i) + '/'
        print(url)
        driver.get(url)
        content = driver.page_source
        soup = BeautifulSoup(content, "html.parser")
        for a in soup.findAll('div', attrs={'class': 'item-header'}):
            title = a.find('a', attrs={'rel': 'bookmark'})
            title = title.text
            title = title + "\n"
            titles.append(title)
        for b in soup.findAll('time', attrs={'class': 'entry-date updated td-module-date'})[1:]:
            time=b.text
            time = time + "\n"
            dates.append(time)
        for c in soup.findAll('div', attrs={'class': 'td-tags td-post-small-box clearfix'}):
           tag = c.text
           tag = tag +"\n"
           tags.append(tag)
        for d in soup.findAll('div', attrs={'class': 'td-excerpt'}):
            d=d.text
            d=d.strip()
            d = d + "\n"
            descriptions.append(d)
        i += 1
         #driver.close()


print(titles, "\n", dates, "\n", tags, "\n", descriptions)
driver.close()
entetes = [
     u'titles',
     u'tags',
     u'descriptions',
     u'dates'
]

valeurs1 = [
     titles
]
valeurs2 = [
     tags
]
valeurs3 = [
     descriptions
]
valeurs4 = [

    dates
]


f = open('Data.csv', 'w')
ligneEntete = ";".join(entetes)+ "\n"
f.write(ligneEntete)
for valeur in valeurs1:
     ligne = "".join(valeur)
     f.write(ligne)
for valeur in valeurs2:
     ligne = ";".join(valeur)
     f.write(ligne)
for valeur in valeurs3:
     ligne = ";".join(valeur)
     f.write(ligne)
for valeur in valeurs4:
     ligne = ";".join(valeur)
     f.write(ligne)
f.close()