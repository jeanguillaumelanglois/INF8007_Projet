"""on importe notre module web crawler qu'on a créé
   """
from web_crawler import WebCrawler
import sys

print("starting crawler")
STARTING_URL = sys.argv[1]
CRAWLER = WebCrawler()
CRAWLER.crawl_site(STARTING_URL)
CRAWLER.print_report()
