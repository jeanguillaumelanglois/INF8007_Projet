"""re est un module pour les expressions regex,
requests pour executer des requetes https sur des url
et html parser un module qu'on a cree pour parser le html recu
   """
import re
import requests
from my_parser import HTMLTagParser


def get_links_on_page_url(url, all_links):
    """retourne tous les liens contenus dans la page associée au lien passé en parametres
        On charge le HTML de la page puis on le parse pour recuperer les attributs via les tags
        Ensuite on fait matcher les valeurs avec notre regex cree pour filtrer les liens parmi
        d'autres attributs. On vérifie qu'elle n'existe pas deja dans
        notre liste de liens en parametres avant de l'ajouter
    """
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 \
        (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'}
    page = requests.get(url, headers=headers)
    data = page.text
    parser = HTMLTagParser()
    parser.feed(data)

    pattern1 = re.compile("((http|ftp)s?://.*?)")
    pattern2 = re.compile("\/+(.*)")
    links_from_text = re.findall('http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|\
                                                (?:%[0-9a-fA-F][0-9a-fA-F]))\+', data)
    for link in parser.links:
        for value in list(link.values()):
            if pattern1.match(str(value)) or pattern2.match(str(value)):
                if value not in all_links:
                    all_links.append(value)
    for link in parser.links_text:
        for value in list(link.values()):
            if pattern1.match(str(value)) or pattern2.match(str(value)):
                if value not in all_links:
                    all_links.append(value)
    for link in links_from_text:
        if link not in all_links:
            all_links.append(link)

    return all_links


def get_links_local_file(local_file_path, all_links):
    """retourne tous les liens contenus dans la page associée au lien passé en parametres
        On charge le HTML de la page puis on le parse pour recuperer les attributs via les tags
        Ensuite on fait matcher les valeurs avec notre regex cree pour filtrer les liens parmi
        d'autres attributs. On vérifie qu'elle n'existe pas deja dans
        notre liste de liens en parametres avant de l'ajouter
    """
    with open(local_file_path, 'r') as file:
        data = file.read()
    parser = HTMLTagParser()
    parser.feed(data)

    pattern1 = re.compile("((http|ftp)s?://.*?)")
    pattern2 = re.compile("\/+(.*)")
    for link in parser.links:
        for value in list(link.values()):
            if pattern1.match(str(value)) or pattern2.match(str(value)):
                if value not in all_links:
                    all_links.append(value)
    for link in parser.links_text:
        for value in list(link.values()):
            if pattern1.match(str(value)) or pattern2.match(str(value)):
                if value not in all_links:
                    all_links.append(value)

    return all_links
