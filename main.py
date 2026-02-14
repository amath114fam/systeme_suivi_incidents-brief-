from db import get_connexion
import bcrypt
from auth import create_user
from login import logine
from tickets import add_ticket, voir_demande, voir_demande_admin, update_ticket, update_ticket_user, del_demande


# génération du sel
salt = bcrypt.gensalt()  # s

"""Authentification"""

# def create_admin():
#     # print("#" * 80)
#     # print("Bienvenu dans la boutique".center(80))
#     # print("#" * 80)
#     email = input("Entrer votre email : ").strip()
#     mot_de_passe = input("Entrer votre mot de passe : ").strip().encode("utf-8")
#     cursor = connection.cursor()
#     try:
#         query = "insert into users(email, mot_de_passe, role) values (%s, %s, 'admin')"
#         cursor.execute(query, (email, bcrypt.hashpw(mot_de_passe, salt)))
#         connection.commit()
#         cursor.close()
#         print("Admin crée avec succès")
#     except Exception as e:
#         print("Problème : ", e)

   
############################################ Menu users #############################################
def menu_users(user):
    continuer = True
    while continuer:
        print("#" * 80)
        print("1. Faire une demande")
        print("2. Voir mes demande")
        print("3. Modifier une demande")
        print("4. Supprimer une demande")
        print("0. Déconnecter")
        choix = input("Choisie : ")
        match choix:
            case "1":
                add_ticket(user["id"])
            case "2":
                voir_demande(user["id"])
            case "3":
                voir_demande()
                update_ticket_user()
            case "4":
                voir_demande(user["id"])
                del_demande()
            case "0":
                print("Au revoir")
                continuer = False
            case _:
                print("Mauvaise saisie")
                exit()
############################################ Menu admin #############################################
def menu_admin():
    continuer = True
    while continuer:
        print("#" * 80)
        print("1. La liste des demandes")
        print("2. Modifier l'état d'une demande")
        print("3. Déconnexion")
        print("0. Quitter")
        choix = input("Choisie : ")
        match choix:
            case "1":
                voir_demande_admin()
            case "2":
                voir_demande_admin()
                update_ticket()
            case "3":
                print("Au revoir")
                continuer = False
            case _:
                print("Mauvaise saisie")
                exit()
def main():
    print("#" * 80)
    print("Bienvenue dans Simplon".center(80))
    print("#" * 80)
    continuer = True
    while continuer:
        print("1. S'inscrire")
        print("2. Se connecter")
        print("0. Quitter")
        choix = input("Choisie : ")
        match choix:
            case "1":
                create_user()
            case "2":
                user = logine()
                if user:
                    if user["role"].lower() == "admin" :
                        menu_admin()
                    else:
                        menu_users(user)
            case "0":
                print("Au revoir")
                continuer = False
            case _:
                print("Erreur de saisie")
                exit()
main()