from html_parser import HTMLTagParser
from html_parser import HTMLTextParser
import requests
import re

def get_links_on_page(url, starting_domain):
    all_links = []
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'}
    page = requests.get(url, headers=headers)
    data = page.text
    parser = HTMLTagParser()
    parser.feed(data)
    text_parser = HTMLTextParser()
    text_parser.feed(data)

    pattern = re.compile("((http|ftp)s?://.*?)")
    for l in parser.links:
        for value in list(l.values()):
            if pattern.match(str(value)):
                if check_domain(value, starting_domain):
                    if value not in all_links:
                        all_links.append(value)
                else:
                    if value not in external_links:
                        external_links.append(value)

    for l in text_parser.links_text:
        for value in list(l.values()):
            if pattern.match(str(value)):
                if check_domain(str(value), starting_domain):
                    if str(value) not in all_links:
                        all_links.append(value)
                else:
                    if str(value) not in external_links:
                        external_links.append(value)
    return all_links