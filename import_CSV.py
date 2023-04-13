import pandas as pd  
# connecteur/driver pour se connecter à la base de données (traducteur)
import pymysql

df = pd.read_csv('clients.csv')
"""
    Args:
        nom_CSV (str): nom du fichier CSV à lire "clients.csv"
"""

def lire_csv(nom_CSV : str) -> pd.DataFrame : # fonction qui permet de lire le fichier CSV et de le convertir en dataframe 
    df = pd.read_csv(nom_CSV)
    return df 

def se_connecter_db(host, user, password, database): 
    conn = pymysql.connect(host=host, user=user, password=password, database=database) # permet de se connecter à la base de données
    return conn

if __name__ == "__main__": # permet de vérifier si le fichier est exécuté directement en tant que premier fichier. Si c'est le cas on execute le code si dessus. Si le fichier est importé, le code ne sera pas exécuté
    db_host ="localhost" # si vous êtes sur votre machine, ip si c'est sur une autre machine
    db_user ="root" # login de la base de données
    db_password ="example" # mot de passe de la base de données
    db_database ="exercice" # nom de la base de données
    conn = se_connecter_db(db_host, db_user, db_password, db_database)


def inserer_donnees(conn, utilisateurs): # fonction qui permet d'insérer les données dans la base de données
    cursor = conn.cursor() # permet de créer un curseur qui va se placer sur la table et de parcourir les enregistrements. Permet d'interagir avec la base de données
    for index, row in df.iterrows(): # boucle qui permet de parcourir le dataframe et de récupérer les données
        sql ="INSERT INTO clients (id, prenom, nom, email, profession, pays, ville) VALUES (%s, %s, %s, %s, %s, %s, %s)" # requête SQL qui permet d'insérer les données dans la base de données, créer un schéma de la table
        cursor.execute(sql,(row['id'], row['firstname'], row['lastname'], row['email'], row['profession'], row['country'], row['city'])) # exécute la requête SQL avec les données du dataframe
        conn.commit() # permet de valider les modifications dans la base de données

inserer_donnees(conn, df) # appel de la fonction qui permet d'insérer les données dans la base de données

