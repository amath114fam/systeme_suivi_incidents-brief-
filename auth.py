from db import get_connexion
import bcrypt
import re

pattern = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
# génération du sel
salt = bcrypt.gensalt()  # s

"""Authentification"""
###############################################Create utilisateurs###############################################""
def create_user():
    connection = get_connexion()
    cursor = connection.cursor()
    print("#" * 80)
    print("Créer compte".center(80))
    print("#" * 80)
    email = input("Entrer votre email : ").strip()
    while email == "" or email.isnumeric() or not re.match(pattern, email):
        print("Format incorrect")
        email = input("Entrer votre email : ").strip()
    query = "SELECT id_utilisateur FROM users WHERE email = %s"
    cursor.execute(query, (email,))
    if cursor.fetchone():  
        print("Cet email est déjà utilisé. Veuillez en choisir un autre.")
        return  
    mot_de_passe = input("Entrer votre mot de passe : ").strip().encode("utf-8")
    while mot_de_passe == "" or len(mot_de_passe) < 4:
        print("Veiller saisir au moins 4 caractères")
        mot_de_passe = input("Entrer votre mot de passe : ").strip().encode("utf-8")
    role = "user"
    query = "insert into users(email, mot_de_passe, role) values (%s, %s, %s)"
    cursor.execute(query, (email, bcrypt.hashpw(mot_de_passe, salt), role ))
    connection.commit()
    cursor.close()
    print("#" * 10)
    print("Utilisateur crée avec succès")
    print("#" * 10)
"""Menu connexion"""
