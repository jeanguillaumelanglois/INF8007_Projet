"""on importe notre module web crawler qu'on a créé
   """
from web_crawler import WebCrawler
import sys
# Options du script:
# Arguments
# 1- Type de données (1- URL, 2- Fichier local, 3- Données en stdin)
# 2- Activation du crawling (1/0)
# 3- Données (Pour les types de données 1 et 2)
data_type = sys.argv[1]
crawling_activated = True if sys.argv[2] == '1' else False

# On prend en entrée un URL
if data_type == '1':
    print("Starting crawler on URL")
    if not crawling_activated:
        print("(Crawling deactivated)")
    STARTING_URL = sys.argv[3]
    CRAWLER = WebCrawler()
    CRAWLER.crawl_site(STARTING_URL, crawling_activated)
    CRAWLER.print_report()

# On prend en entrée un fichier local (crawling désactivé)
elif data_type == '2':
    print("Starting crawler on local file")
    print("(Crawling deactivated)")
    crawling_activated = False
    LOCAL_FILE = sys.argv[3]
    CRAWLER = WebCrawler()
    CRAWLER.crawl_local_file(LOCAL_FILE)
    CRAWLER.print_report()

# On prend en entrée des données en stdin
elif data_type == '3':
    print("What type of std:in do you want to use (1- HTML page, 2- List of web sites, 3- List of files)")
    stdin_type = input()

    # On prend une page HTML en entrée
    if (stdin_type == '1'):
        print("Please enter the path of your HTML page")
        HTML_page = input()
    # On prend une liste de sites web en entrée
    elif (stdin_type == '2'):
        print("Please enter the path of your web site list")
        CRAWLER = WebCrawler()
        website_list = input()
        for url in website_list:
            print("Processing for {}".format(url))
            CRAWLER.crawl_site(url)
    # On prend une liste de fichiers en entrée
    elif (stdin_type == '3'):
        print("Please enter the path of your list of files")
        files_list = input()
    # print("Starting crawler on stdin data")
    # if not crawling_activated:
    #     print("(Crawling deactivated)")
    # CRAWLER = WebCrawler()
    # CRAWLER.crawl_site(data, crawling_activated)
    # CRAWLER.print_report()


