
import wikipedia
import sys
from HTMLParser import HTMLParser
import bs4
import operator

wikipedia.set_lang("en")
results=wikipedia.search(sys.argv[1])
page=wikipedia.page(results[0])
text=page.html()
soup = bs4.BeautifulSoup(text, "html.parser")


soup.sup.decompose()

paragraphs = soup.findAll('p')


def get_sentence_from_paragraph(i):
	paragraph = str(paragraphs[i])

	phrases={}

	for line in paragraph.split('. '):
       		phrases[line]=line.count('<a ')


	mysentence = max(phrases.iteritems(), key=operator.itemgetter(1))[0]


	mysoup = bs4.BeautifulSoup(mysentence, "html.parser")

	mysoup.a.replace_with("...")

	return mysoup.get_text()


if (len(sys.argv) != 3):
	print "Usage: python mvp.py <word_to_search_in_wikipedia> <number_of_sentences>"
	sys.exit(-1)

N = int(sys.argv[2])
OFFSET = 1

N = min(N,len(paragraphs) - OFFSET)

sentences = map(get_sentence_from_paragraph, range(OFFSET, N+OFFSET))
print '\n'.join(sentences)
