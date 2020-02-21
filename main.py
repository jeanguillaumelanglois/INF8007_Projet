from tldextract import extract




import requests
import re





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


starting_url = "https://www.villedefermont.qc.ca/"
starting_domain = extract_domain(starting_url)

valid_links = []
invalid_links = []

visited_links = []
external_links = []
# scraping main page

all_links = get_links_on_page(starting_url, starting_domain)

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


