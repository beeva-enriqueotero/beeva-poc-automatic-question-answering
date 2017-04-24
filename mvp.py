#!/usr/bin/env python

import wikipedia
import sys
from HTMLParser import HTMLParser
import bs4
import operator

wikipedia.set_lang("es")
results=wikipedia.search(sys.argv[1])
page=wikipedia.page(results[0])
text=page.html()
soup = bs4.BeautifulSoup(text, "html.parser")


myhtml = soup.sup.decompose()

soup = bs4.BeautifulSoup(str(soup), "html.parser")
paragraph = str(soup.findAll('p')[1])

phrases={}

for line in paragraph.split('.'):
       phrases[line]=line.count('<a ')


mysentence = max(phrases.iteritems(), key=operator.itemgetter(1))[0]

mysoup = bs4.BeautifulSoup(mysentence, "html.parser")
print mysoup.text
