# hw3

# from pattern.web import *
# from pattern.en import *
import urllib2
import operator
from bs4 import BeautifulSoup as soup

#from timeline.timeline import timeline

# tell python to look into the CDC website
search = raw_input('Enter search word: ')
page = 0
x = dict()

while page < 200:

    # download the html for this url and parse it with beautiful soup so we can find tags in the future
    cdc = soup(urllib2.urlopen("http://www.cdc.gov/search.do?q=" + search + "&ie=utf8&oe=UTF-8&ulang=&sort=date:D:L:d1&entqrm=0&wc=200&wc_mc=1&ud=1&start=" + str(page)).read())

    # create a list to save all the links we find
    links = []

    # loop through all the ul tags with the class: "results"
    for tag in cdc.find_all("ul", "results"):
        links.extend(tag.find_all("li")[0].find_all("li")[2].text.replace("(", "").replace(",", "").replace("-", "").replace(".", "").replace(")", ""). replace(":", "").encode("utf-8").split()) # add the list of links we find for each a tag to the list: links

    # look at the frequencies of each word
    for word in links:
        x[word] = x.get(word, 0) + 1
 
    page += 10

# putting frequencies in order from highest to lowest
sorted_x = sorted(x.items(), key=operator.itemgetter(1))[::-1]

print sorted_x
