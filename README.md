# Softdesk
Issue tracking system - API RESTful

Version : Python 3.10.1

## Paramétrage
- Cloner ce dépôt de code avec la commande
```$ git clone https://github.com/tom1ke/softdesk.git```
- Se positionner à la racine du projet via le terminal
- Créer un environnement virtuel avec la commande

  - MacOS / Linux ```$ python3 -m venv env```

  - Windows ```$ python -m venv env```
- Activer l'environnement virtuel avec la commande

  - MacOS / Linux ```$ source env/bin/activate```

  - Windows ```$ env\Scripts\activate```
- Installer les dépendances du projet avec la commande ```$ pip install -r requirements.txt```
- Se positionner au niveau de projet Django via le terminal avec la commande ```$ cd src```
- Démarrer le serveur local avec la commande ```$ python manage.py runserver```
- Accéder à l'API via un navigateur ou un outil de type Postman à cette url : http://127.0.0.1:8000/

Cela vaut uniquement pour l'installation initiale. Pour les lancements ultérieurs, il suffira d'activer l'environnement
virtuel et de démarrer le serveur pour accéder à l'API.

## Documentation Postman
La documentation de l'API et de tous les points de terminaison est disponible sur Postman :

https://documenter.getpostman.com/view/19593831/UzJQqEcf


## Inscription et authentification
L'authentification fonctionne avec un système de *bearer token* (JWT). Il est nécessaire de s'incrire, puis de s'authentifier pour pouvoir utiliser l'API.

Vous trouverez les points de terminaison liés à l'inscription et l'authentification, ainsi que la marche à suivre sur la documentation Postman.

## Administration
Afin d'accéder à l'interface d'administration de l'application il est nécessaire de créer un profil de *superuser*.

Pour ce faire, se positionner au niveau du projet Django via le terminal et utiliser la commande ```$ python manage.py createsuperuser```

Suivre les instructions données dans le terminal (le nom d'utilisateur et le mot de passe sont indispensables, mais il 
n'est pas nécessaire de renseigner une adresse email).

Il est maintenant possible de se connecter avec les indentifiants nouvellement créés à l'interface d'admninistration de
l'API à cette url : http://127.0.0.1:8000/admin/