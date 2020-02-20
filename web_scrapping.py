from html.parser import HTMLParser
from tldextract import extract

links = []
links_text = []

import requests
import re


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


def get_links_on_page(url, starting_domain):
    all_links = []
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'}
    page = requests.get(url, headers=headers)
    data = page.text
    parser = MyHTMLParser()
    text_parser = MyHTMLTextParser()
    text_parser.links_text = []
    text_parser.feed(data)
    parser.links = []
    parser.feed(data)
    pattern = re.compile("((http|ftp)s?://.*?)")

    for l in links:
        for value in list(l.values()):
            if pattern.match(str(value)):
                print(value)
                if check_domain(value, starting_domain):
                    if value not in all_links:
                        all_links.append(value)
                    else:
                        print("link already in all_links")
                else:
                    print("link not in domain")
                    if value not in external_links:
                        external_links.append(value)

    for l in links_text:
        for value in list(l.values()):
            if pattern.match(str(value)):
                print(value)
                if check_domain(str(value), starting_domain):
                    if str(value) not in all_links:
                        all_links.append(value)
                    else:
                        print("link already in all_links")
                else:
                    print("link not in domain")
                    if str(value) not in external_links:
                        external_links.append(value)
    return all_links


def check_links(all_links):
    for link in all_links:
        code = requests.head(link).status_code
        if code in [400, 403, 404, 405]:
            invalid_links.append((link, requests.head(link).status_code))
        else:
            valid_links.append((link, requests.head(link).status_code))


def extract_domain(url):
    tsd, td, tsu = extract(url)  # prints abc, hostname, com
    domain = td + '.' + tsu  # will prints as hostname.com
    return domain


def check_domain(url, domain):
    new_domain = extract_domain(url)
    if domain == new_domain:
        return True
    else:
        return False


starting_url = "https://www.polymtl.ca"
starting_domain = extract_domain(starting_url)

valid_links = []
invalid_links = []

visited_links = []
external_links = []
# scraping main page

all_links = get_links_on_page(starting_url, starting_domain)
#
# check_links(all_links)


# print("List of valid links: ")
# print(valid_links)
# print("list of invalid links: ")
# print(invalid_links)
print("list of internal links")
print(all_links)
print("external links:")
print(external_links)

# Schema.org donne un 301

# TODO Rajouter les liens relatifs dans les hrefs
# TODO filtrer les faux positifs et les faux negatifs (?)
# Image --> vérifier si elles existent, regarder contenttype
# TODO Balises scripts json (?)
# TODO comment utiliser les liens relatifs(?)
# TODO pour le web cralling il faut utiliser les listes des urls issues du web scrapping(?)
# TODO verifier si elles font partie du meme site (?)
# TODO recommencer recursivement pour les adresses du meme site(?)
# TODO rapport en JSON

for link in all_links:
    get_links_on_page(link, starting_domain)

print(all_links)