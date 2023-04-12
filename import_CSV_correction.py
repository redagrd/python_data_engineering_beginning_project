import pandas as p
import pymysql as maria
from pymysql.connections import Connection


def lire_csv(nom_fichier: str) -> p.DataFrame:
    """_summary_ : permet de lire un fichier csv et de le convertir en DataFrame
    Args:
        nom_fichier (str): nom du fichier csv à lire "nom_fichier.csv"
    Returns:
        p.DataFrame: DataFrame contenant les données du fichier csv
    """
    table = p.read_csv(nom_fichier)
    return table


# table = lire_csv("clients.csv")


def se_connecter_db(host: str, user: str, password: str, database: str) -> maria.connections.Connection:
    """_summary_ : permet de se connecter à une base de données
    Args:
        host (str): machine sur laquelle se trouve la base de données
            - localhost : si c'est sur la même machine
            - ip : si c'est sur une autre machine exemple: 10.125.22.53
        user (str): login de la base de données
        password (str): password de la base de données
        database (str): nom de la base de données
    Returns:
        maria.connections.Connection: appel vers la base de données
    """
    connexion = maria.connect(host=host, user=user, password=password, database=database)
    return connexion


def ajouter_client(cnx: Connection , data: p.DataFrame):
    """_summary_ : permet d'ajouter un client dans la base de données
    Args:
        cnx (maria.connections.Connection): appel vers la base de données
        data (p.DataFrame): DataFrame contenant les données du client à ajouter
    """
    # on crée un curseur. Un curseur permet de parcourir les enregistrements d'un résultat
    curseur = cnx.cursor()
    # on crée une requête sql pour ajouter les clients
    sql = "INSERT INTO clients (id, nom, prenom, email, profession, pays, ville) \
        VALUES (%s, %s, %s, %s, %s, %s, %s)"
    
    for index, row in data.iterrows():
        # on exécute la requête sql
        curseur.execute(sql, \
            (row["id"], row["firstname"], row["lastname"], row["email"], row["profession"], row["country"], row["city"]))
        
    # on commit les changements. Commiter permet de valider les changements
    cnx.commit()
    # on ferme la connexion (c'est raccrocher le téléphone)
    cnx.close()

# vérification que le fichier est bien exécuté en tant que premier fichier
# si c'est le cas, on exécute le code ci-dessous
# exemple: py app.py
if __name__ == "__main__":
    db_host = "localhost"
    db_user = "root"
    db_password = "example"
    db_database = "exercice"
    
    # on lit le fichier csv
    table_clients = lire_csv("clients.csv")
    
    # on se connecte à la base de données. C'est comme lancer un appel téléphonique
    cnx = se_connecter_db(db_host, db_user, db_password, db_database)
    
    # on ajoute un client
    ajouter_client(cnx, table_clients)