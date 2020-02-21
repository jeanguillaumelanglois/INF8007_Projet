"""on importe notre module web crawler qu'on a créé
   """
from web_crawler import WebCrawler

STARTING_URL = "https://www.villedefermont.qc.ca/"
CRAWLER = WebCrawler()
CRAWLER.crawl_site(STARTING_URL)
CRAWLER.print_report()
