# INF8007_Projet

Ce programme permet d'extraire tous les liens contenus dans un site web et les classer selon leut validité, produisant donc une liste de liens valides et une liste de liens invalides pour un site web donné.

## Prérequis

```
Ouvrir avec PyCharm

pip install requirements.txt
```

## Fonctionnement du crawler

Pour crawler un site, on met son url dans la variable STARTING_URL du fichier main.py, puis le script appelera la fonction crawl_site(STARTING_URL) du module web_crawler.

Une fois le crawling terminé, le programme appelera la fonction print_report() qui imprimera la liste des liens valides, puis la liste des liens invalides.

## Auteurs

* **Marc Hounto - 1769769**
* **Jean-Guillaume Langlois - 1741803**

