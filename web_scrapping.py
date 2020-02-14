# import requests
# # import re
# # url = "http://polymtl.ca/"
# #
# # page = requests.get(url)
# # data = page.text
# # links = re.findall('"((http|ftp)s?://.*?)"', data)
# # valid_links = []
# # invalid_links = []
# # for link in links:
# #     if (requests.head(link[0]).status_code in [400, 403, 404, 405]):
# #       invalid_links.append((link,requests.head(link[0]).status_code))
# #     else:
# #       valid_links.append((link,requests.head(link[0]).status_code))
# #
# # print(links)
# # print(valid_links)
# # print("list of invalid links ; ")
# # print(invalid_links)

from html.parser import HTMLParser

links = []
links_text = []
all_links = []

import requests
import re

url = "http://polymtl.ca/"

class MyHTMLParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        if tag != 'a':
            return
        attr = dict(attrs)
        links.append(attr)

class MyHTMLTextParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        if tag != 'a':
            attr = dict(attrs)
            links_text.append(attr)


headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'}
page = requests.get(url, headers=headers)
data = page.text
parser = MyHTMLParser()
text_parser = MyHTMLTextParser()
text_parser.links_text =[]
text_parser.feed(data)
parser.links = []
parser.feed(data)
pattern = re.compile("((http|ftp)s?://.*?)")
#TODO Rajouter les liens relatifs dans les hrefs
#TODO filtrer les faux positifs et les faux negatifs (?)
#TODO Balises scripts json (?)
#TODO comment utiliser les liens relatifs(?)
#TODO pour le web cralling il faut utiliser les listes des urls issues du web scrapping(?)
#TODO verifier si elles font partie du meme site (?)
#TODO recommencer recursivement pour les adresses du meme site(?)

for l in links :
    for value in list(l.values()):
        if pattern.match(value):
            all_links.append(value)

for l in links_text:
    for value in list(l.values()):
        if pattern.match(str(value)):
            all_links.append(value)

print(all_links)
