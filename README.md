# INF8007_Projet

Ce programme permet d'extraire tous les liens contenus dans un site web et les classer selon leut validité, produisant donc une liste de liens valides et une liste de liens invalides pour un site web donné.

## Prérequis

```
Ouvrir avec PyCharm

pip install requirements.txt
```

## Fonctionnement du main.py

Le script main.py prend 3 éléments en arguments:
* 1- Type de données (1, 2 ou 3)
    1- URL : le script va trouver tous les liens valides et invalides pour le site contenu à cet url
    2- Fichier local : le script va trouver tous les liens valides et invalides pour la page HTML contenue dans ce fichier local
    3- Données en stdin : le script va demander le type de données en stdin
        a- Page HTML : le script va demander le path d'une page HTML, puis trouver tous les liens valides et invalides sur cette page
        b- Liste d'URLs : le script va demander le path d'un fichier .txt contenant une liste d'URLs, puis trouvera tous les liens valides et invalides pour chacun de ces URLs
        c- Liste de fichiers : le script va demander le path d'un fichier .txt contenant une liste de fichiers, puis trouvera tous les liens valides et invalides pour la page HTML contenue dans chacun de ces fichiers
* 2- Activation du crawling (1 ou 0) : spécifie au script si on doit crawler les pages HTML, c'est-à-dire plus d'un niveau de profondeur
* 3- Données : Si on a choisi 1 (URL) comme type de données, on spécifie ici l'URL, sinon si on a choisi 2 (Fichier local) comme type de données, on spécifie ici le path de ce fichier

## Fonctionnement du verifyURL.sh (script bash)

Le script verifyURL.sh prend 2 éléments en arguments:
* 1- URL : URL d'un repository git contenant le code d'un site web duquel on veut vérifier les liens
* 2- Port : Port sur lequel on va "runner" le site web contenu sur le lien git sur notre localhost

Le script bash partira un serveur en localhost sur le port spécifié sur lequel on ébergera le site web contenu dans le lien git. Ensuite, on va appeler le fichier main.py en spécifiant 1 comme type de données, 1 pour crawling_activated et localhost:{port} comme url

## Auteurs

* **Marc Hounto - 1769769**
* **Jean-Guillaume Langlois - 1741803**

