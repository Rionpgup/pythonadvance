from tkinter.scrolledtext import example

from bs4 import BeautifulSoup

element = soup.find(name,attrs,recursive,string,**kwager)
first_Link=soup.find('a')

element = soup.find_all(name,attrs,recursive,string,**kwager)
all_Links = soup.find_all('a')

element = soup.select(selector)

example = soup.select('.example')


text = element.get_text(seperatror,strip)

text = element.get_text()

Attributes =element.attrs

link = soup.find('a')

href = link.attrs['href']


parent = element.parent
parents.element.parents

parent = element.parent
children = element.children
descendants = element.descendants