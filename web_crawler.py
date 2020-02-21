import requests
from tldextract import extract
from web_scraper import get_links_on_page


class WebCrawler():
    def __init__(self):
        self.valid_links = []
        self.invalid_links = []
        self.all_links = []

    def check_link_validity(self, link_to_check):
        try:
            code = requests.head(link_to_check).status_code
            if code in [400, 403, 404, 405]:
                self.invalid_links.append((link_to_check, code))
            else:
                self.valid_links.append((link_to_check, code))
        except:
            self.invalid_links.append((link_to_check, "invalid"))

    def extract_domain(self, url):
        tsd, td, tsu = extract(url)  # prints abc, hostname, com
        domain = td + '.' + tsu  # will prints as hostname.com
        return domain

    def check_domain(self, url, domain):
        domain_to_check = self.extract_domain(url)
        if domain == domain_to_check:
            return True
        else:
            return False

    def crawl_site(self, starting_url):
        starting_domain = self.extract_domain(starting_url)
        all_links = get_links_on_page(starting_url, self.all_links)
        for link in all_links:
            self.check_link_validity(link)
            if self.check_domain(link, starting_domain):
                all_links = get_links_on_page(link, all_links)
            all_links.remove(link)
            self.print_report()

    def print_report(self):
        print("list of valid links")
        print(self.valid_links)
        print("list of invalid links")
        print(self.invalid_links)
