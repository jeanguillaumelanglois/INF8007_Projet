# coding=utf-8
from tldextract import extract
import requests

from web_scraper import get_links_on_page


def check_link_validity(link_to_check):
    try:
        code = requests.head(link_to_check).status_code
        if code in [400, 403, 404, 405]:
            invalid_links.append((link_to_check, code))
        else:
            valid_links.append((link_to_check, code))
    except:
        print("Something went wrong with the link")
        invalid_links.append((link_to_check, "invalid"))


def extract_domain(url):
    tsd, td, tsu = extract(url)  # prints abc, hostname, com
    domain = td + '.' + tsu  # will prints as hostname.com
    return domain


def check_domain(url, domain):
    domain_to_check = extract_domain(url)
    if domain == domain_to_check:
        return True
    else:
        return False


starting_url = "https://www.villedefermont.qc.ca/"
starting_domain = extract_domain(starting_url)

valid_links = []
invalid_links = []

# scraping main page
all_links = []
all_links = get_links_on_page(starting_url, all_links)
for link in all_links:
    check_link_validity(link)
    if check_domain(link, starting_domain):
        all_links = get_links_on_page(link, all_links)
    all_links.remove(link)

# all_links = []
# link = 'https://www.villedefermont.qc.ca/conseil-municipal/'
# all_links = get_links_on_page(link, all_links)


print("all_links")
print(all_links)
print("list of valid links")
print(valid_links)
print("list of invalid links")
print(invalid_links)


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


