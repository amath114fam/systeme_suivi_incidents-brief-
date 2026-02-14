from getpass import getpass
import bcrypt
from db import get_connexion
import re

pattern = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"

salt = bcrypt.gensalt()  

#########################################gère la connexion#############################
def logine():
    connection = get_connexion()
    cursor = connection.cursor()
    email = input("Entrer votre email : ").strip()
    while email == "" or email.isnumeric() or not re.match(pattern, email):
        print("Format incorrect")
        email = input("Entrer votre email : ").strip()
    mot_de_passe = getpass("Entrer votre mot de passe : ").strip().encode("utf-8")
    while mot_de_passe == "" :
        print("Veiller saisir au moins 4 caractères")
        mot_de_passe = input("Entrer votre mot de passe : ").strip().encode("utf-8")
    try:
        query = "select id_utilisateur, email, mot_de_passe, role from users where email = %s"
        cursor.execute(query, (email, ))
        session = cursor.fetchone()
        if not session:
            print("-" * 30)
            print("L'utilisateur n'existe pas")
            return None
        ids, email, mot_de_passe_hash, role = session
        hashe = mot_de_passe_hash.encode("utf-8")
        if bcrypt.checkpw(mot_de_passe, hashe):
            return {"role" : role, "id" : ids}
        else:
            print("-" * 30)
            print("Mot de passe incorrect")
    except Exception as e:
        print("Probleme : ", e)
    finally:
        cursor.close() 
        connection.close()


    
