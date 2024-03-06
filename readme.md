# Projet 10 Développeur d'application Python : Créez une API sécurisée RESTful en utilisant Django REST

## Informations générales

Ce projet constitue un examen dans le cadre du parcours Développeur d'application Python d'OpenClassrooms, il est codé avec le langage Python.
Concrètement, il consiste à créer une application permettant de remonter et suivre des problèmes techniques en passant par la création d'une API avec Django REST.

## Auteur

Fabien ROYER

## Contributions

Le projet est achevé depuis février 2024.

## Cloner le repository

- `cd /path/to/put/project/in`
- `git clone https://github.com/royerfab/OC_P10_API_RESTful_avec_Django_REST.git`

## Installation

Création de l'environnement :
```bash
python -m venv env
```

Lancement de l'environnement :
```bash
env\Scripts\activate
```

Utilisez le _package installer_ [pip](https://pypi.org/project/pip/) pour installer les packages inclus dans le fichier 
requirements.txt, pour cela utilisez dans le terminal la commande :

```bash
pip install -r requirements.txt
```

## Utilisation

Pour exécuter le code, il faut entrer la commande suivante dans le terminal :

```bash
python manage.py runserver
```

Ce programme permet de créer des utilisateurs, des contributeurs, des projets, des problèmes et des commentaires, ainsi que de les associer entre eux. Un système de permissions donne pour chaque utilisateur un accès restreint aux données qu'il pourra consulter et aux actions qu'il pourra entreprendre sur Postman.

## Accéder à l'exemple de l'API par Postman

- url de Postman : `https://documenter.getpostman.com/view/31593605/2sA2xcZZsF`