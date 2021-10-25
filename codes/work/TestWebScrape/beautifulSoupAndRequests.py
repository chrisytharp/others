from bs4 import BeautifulSoup
import requests

with open('file.html') as html_file:  # read is default no nead to add arg
    soup = BeautifulSoup(html_file, 'lxml')  #this is opening html file with lxml parser

print(soup.prettify())               # prettify() makes html code pretty
