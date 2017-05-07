import os,sys
from lxml import html
import requests

#pull the front page google news results for a company or index
def getArticles(keywords):
    #page with google news results
    url = 'https://www.google.com/search?q=' + keywords + '&tbm=nws'

    #pull the page
    newspage = requests.get(url)
    newspage_tree = html.fromstring(newspage.content)

    titles = newspage_tree.xpath('//h3[@class="r"]/a/text()')
    snippets = newspage_tree.xpath('//div[@class="st"]/text()')
    #print(newspage.content)
    print(titles)
    print(snippets)

getArticles('trump')
