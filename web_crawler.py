"""requests pour executer des requetes https sur des url,
    tdlextract est un module de parsage d'url pour extraire un domaine
    et html parser un module qu'on a cree pour parser le html recu
   """
import requests
from tldextract import extract
from web_scraper import get_links_on_page


class WebCrawler():
    """La classe utilisee pour le web crawler elle a les attributs suivants :
        valid_links = liste de liens valides
        invalid_Links = liste de liens invalides
        all_links = liste de tous les liens dans le site
        mis a jour reguliererment au fur et a mesure
        qu'on parcours des liens
       """

    def __init__(self):
        self.valid_links = []
        self.invalid_links = []
        self.all_links = []

    def check_link_validity(self, link_to_check):
        """params: link_to check (un lien)
                verifie si le lien retourne un code d'erreur
                 si oui il le place dans les liens invalides
                    sinon il le place dans les liens valides.
               """
        headers = {
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 \
            (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'}
        try:
            code = requests.head(link_to_check, headers=headers).status_code
            if code in [400, 403, 404, 405]:
                self.invalid_links.append((link_to_check, code))
            else:
                self.valid_links.append((link_to_check, code))
        except:
            self.invalid_links.append((link_to_check, "invalid"))

    def extract_domain(self, url):
        """ params: notre url
                   permet d'extraire le domaine lie a notre url passee en parametre
               """
        tsd, td, tsu = extract(url)  # prints abc, hostname, com
        domain = td + '.' + tsu  # will prints as hostname.com
        return domain

    def check_domain(self, url, domain):
        """params = url(notre url), domaine=(notre domaine de reference)
                   verifie si le domaine de notre url est le meme que le domaine de reference
              """
        domain_to_check = self.extract_domain(url)
        return domain == domain_to_check

    def crawl_site(self, starting_url):
        """re est un module pour les expressions regest,
                requests pour executer des requetes https sur des url
                et html parser un module qu'on a cree pour parser le html recu
               """
        starting_domain = self.extract_domain(starting_url)
        self.all_links = get_links_on_page(starting_url, self.all_links)
        for link in self.all_links:
            self.check_link_validity(link)
            if self.check_domain(link, starting_domain):
                self.all_links = get_links_on_page(link, self.all_links)
            self.all_links.remove(link)
            print(self.valid_links)
            print(self.invalid_links)

    def print_report(self):
        """imprime lorsque le crawling est fini les liens valides et les liens invalides
               """
        print("list of valid links")
        print(self.valid_links)
        print("list of invalid links")
        print(self.invalid_links)
