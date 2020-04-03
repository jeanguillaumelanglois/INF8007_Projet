"""on importe notre module web crawler qu'on a créé
   """
import sys
from web_crawler import WebCrawler

# Options du script:
# Arguments
# 1- Type de données (1- URL, 2- Fichier local, 3- Données en stdin)
# 2- Activation du crawling (1/0)
# 3- Données (Pour les types de données 1 et 2)
DATA_TYPE = sys.argv[1]
CRAWLING_ACTIVATED = True if sys.argv[2] == '1' else False

# On prend en entrée un URL
if DATA_TYPE == '1':
    print("Starting crawler on URL")
    if not CRAWLING_ACTIVATED:
        print("(Crawling deactivated)")
    STARTING_URL = sys.argv[3]
    CRAWLER = WebCrawler()
    CRAWLER.crawl_site(STARTING_URL, CRAWLING_ACTIVATED)
    CRAWLER.print_report()

# On prend en entrée un fichier local (crawling désactivé)
elif DATA_TYPE == '2':
    print("Starting crawler on local file")
    print("(Crawling deactivated)")
    CRAWLING_ACTIVATED = False
    LOCAL_FILE = sys.argv[3]
    CRAWLER = WebCrawler()
    CRAWLER.crawl_local_file(LOCAL_FILE)
    CRAWLER.print_report()

# On prend en entrée des données en stdin
elif DATA_TYPE == '3':
    print("What type of std:in do you want to use \
    (1- HTML page, 2- List of web sites, 3- List of files)")
    STDIN_TYPE = input()

    # On prend une page HTML en entrée
    if STDIN_TYPE == '1':
        print("Please enter the path of your HTML page")
        HTML_PAGE = input()
        print("Starting crawler on HTML page")
        print("(Crawling deactivated)")
        CRAWLING_ACTIVATED = False
        CRAWLER = WebCrawler()
        CRAWLER.crawl_local_file(HTML_PAGE)
        CRAWLER.print_report()
    # On prend une liste de sites web en entrée
    elif STDIN_TYPE == '2':
        print("Please enter the path of your web site list")
        WEBSITE_LIST = input()
        CRAWLER = WebCrawler()
        print("Starting crawler on web site list")
        if not CRAWLING_ACTIVATED:
            print("(Crawling deactivated)")
        with open(WEBSITE_LIST, 'r') as list:
            URLS = list.readlines()
        for url in URLS:
            url = url.rstrip('\n')
            print("Crawling on", url)
            CRAWLER.crawl_site(url, CRAWLING_ACTIVATED)
            CRAWLER.print_report()
    # On prend une liste de path de fichiers en entrée
    elif STDIN_TYPE == '3':
        print("Please enter the path of your list of files")
        FILES_LIST = input()
        print("Starting crawler on list of files")
        print("(Crawling deactivated)")
        CRAWLER = WebCrawler()
        with open(FILES_LIST, 'r') as list:
            FILES = list.readlines()
        for file in FILES:
            file = file.rstrip('\n')
            print("Crawling on", file)
            CRAWLER.crawl_local_file(file)
            CRAWLER.print_report()
