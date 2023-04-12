# Simple Projet Python : Découverte Data Engineering

## Description

Ce projet a pour but de découvrir le Data Engineering. Il s'agit de mettre en place un pipeline de traitement de donées.

Nous chargeons un fichier .csv qui contient des utilisateurs et leurs informations. Nous allons ensuite le traiter pour en extraire des informations, puis les stocker dans une base de données.

## Prérequis

- Python 3.7
- Docker
- Docker-compose
- Git

## Installation

- Clonez le projet
- Créez un environnement virtuel

    ```bash
    # Linux
    python -m venv venv
    # Windows
    py -m venv venv
    ```

- Activez l'environnement virtuel

    ```bash
    # Linux
    source venv/bin/activate
    # Windows batch/cmd.exe
    venv\Scripts\activate.bat

    #windows powershell
    venv\Scripts\Activate.ps1
    ```

- Installez les dépendances

```bash
pip install -r requirements.txt
```
