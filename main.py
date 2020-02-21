"""on importe notre module web craller qu'on a créé
   """
from web_crawler import WebCrawler


# STARTING_URL = "https://www.villedefermont.qc.ca/"
STARTING_URL = "https://www.polymtl.ca/"
CRAWLER = WebCrawler()
CRAWLER.crawl_site(STARTING_URL)
CRAWLER.print_report()
