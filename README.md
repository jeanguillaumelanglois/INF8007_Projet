# INF8007_Projet

Ce programme permet d'extraire tous les liens contenus dans un site web et les classer selon leut validité, produisant donc une liste de liens valides et une liste de liens invalides pour un site web donné.

## Prérequis

```
Git pull
Gut stash
```


## Architecture

Le projet contient 3 modules:

* my_parser
* web_scraper
* web_crawler

## Étapes du crawler

Pour crawler un site, on met son url dans la variable starting_url du fichier main.py, puis le script appelera la fonction crawl_site(starting_url) du module web_crawler.

Une fois le crawling terminé, le programme appelera la fonction print_report() qui imprimera la liste des liens valides, puis la liste des liens invalides.

## Auteurs

* **Marc Hounto - 1769769**
* **Jean-Guillaume Langlois - 1741803**

