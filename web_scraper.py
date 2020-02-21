from my_parser import HTMLTagParser

import requests
import re


def get_links_on_page(url, all_links):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'}
    page = requests.get(url, headers=headers)
    data = page.text
    parser = HTMLTagParser()
    parser.feed(data)


    pattern = re.compile("((http|ftp)s?://.*?)")
    for l in parser.links:
        for value in list(l.values()):
            if pattern.match(str(value)):
                if value not in all_links:
                     all_links.append(value)
    for l in parser.links_text:
        for value in list(l.values()):
            if pattern.match(str(value)):
                if value not in all_links:
                     all_links.append(value)

    return all_links



print(get_links_on_page("http://www.ville.latuque.qc.ca"))