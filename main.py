# coding=utf-8
from web_crawler import WebCrawler

# starting_url = "https://www.villedefermont.qc.ca/"
starting_url = "https://www.polymtl.ca/"
crawler = WebCrawler()
crawler.crawl_site(starting_url)
crawler.print_report()


