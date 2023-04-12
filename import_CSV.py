import pandas as pd  
import pymysql

df = pd.read_csv('clients.csv')
"""
    Args:
        nom_CSV (str): nom du fichier CSV à lire "clients.csv"
"""
  
def lire_csv(nom_CSV : str) -> pd.DataFrame : 
    df = pd.read_csv(nom_CSV)
    print(df)
    return df

def se_connecter_db(host, user, password, database): 
    # Connexion à la base de données
    conn = pymysql.connect(host=host, user=user, password=password, database=database)
    return conn

db_host ="localhost"
db_user ="root"
db_password ="example"
db_database ="exercice"
conn = se_connecter_db(db_host, db_user, db_password, db_database)

def inserer_donnees(conn, utilisateurs):    
    cursor = conn.cursor() 
    for index, row in df.iterrows():        
        sql ="INSERT INTO clients (id, prenom, nom, email, profession, pays, ville) VALUES (%s, %s, %s, %s, %s, %s, %s)" 
        cursor.execute(sql,(row['id'], row['firstname'], row['lastname'], row['email'], row['profession'], row['country'], row['city']))
        conn.commit()

inserer_donnees(conn, df)