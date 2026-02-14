from db import get_connexion
from login import logine
def add_ticket(id_utilisateur):
    connection = get_connexion()
    titre = input("Entrer le titre : ").strip()
    while titre == "" or titre.isnumeric():
        print("Veiller entrer des lettres alphabétiques")
        titre = input("Entrer le titre : ").strip()
    description = input("Entrer la descriprtion : ").strip()
    while description == "" or description.isnumeric():
        print("Veiller entrer des lettres alphabétiques")
        description = input("Entrer la descriprtion : ").strip()
    niveau_urgence = input("Entrer le niveau d'urgence : ").strip()
    while niveau_urgence == "" or niveau_urgence.isnumeric():
        print("Veiller entrer des lettres alphabétiques")
        niveau_urgence = input("Entrer le niveau d'urgence : ").strip()
    cursor = connection.cursor()
    statut = "En attente"
    try:
        query = "insert into tickets(titre, description,statut, id_utilisateur, niveau_urgence) values (%s, %s, %s, %s, %s)"
        cursor.execute(query, (titre, description,statut, id_utilisateur, niveau_urgence,))
        connection.commit()
        print("*" * 10)
        print("Demande envoyé avec succès")
    except Exception as e:
        print("Problème : ", e)
    finally: 
        cursor.close()
        connection.close()
############################################### Voir mes demandes #####################################
def voir_demande(id_utilisateur):
    connection = get_connexion()
    cursor = connection.cursor()
    print("La liste de tes demandes")
    try:
        query = "select id_ticket, titre, description, statut from tickets where id_utilisateur = %s"
        cursor.execute(query, (id_utilisateur, ))
        ticket = cursor.fetchall()
        print("*" * 10)
        for row in ticket:
            print(f"{row[0]}. Titre : {row[1]}, Description : {row[2]}, Statut :{row[3]}")
    except Exception as e:
        print("Problème : ", e)
    finally: 
        cursor.close()
        connection.close()
############################################### voir une demande en tant que admin#####################################
def voir_demande_admin():
    connection = get_connexion()
    cursor = connection.cursor()
    print("La liste de tes demandes")
    try:
        query = """select id_ticket, titre, description, statut, users.email from tickets join 
        users on tickets.id_utilisateur = users.id_utilisateur"""
        cursor.execute(query)
        ticket = cursor.fetchall()
        print("*" * 10)
        for row in ticket:
            print(f"{row[0]}. Titre : {row[1]}, Description : {row[2]}, Statut :{row[3]}, {row[4]}")
    except Exception as e:
        print("Problème : ", e)
    finally: 
        cursor.close()
        connection.close()
############################################### Modifier le statut d'une demande #####################################
def update_ticket():
    connection = get_connexion()
    cursor = connection.cursor()
    print("Modifier le statut des demandes")
    id_ticket = input("Entrer l' id du ticket : ").strip()
    while id_ticket == "" or not id_ticket.isnumeric():
        print("Mauvause saisie")
        id_ticket = input("Entrer l' id du ticket : ").strip()
    statut = input("Modifier le statut du ticket (En attente, disponible, En cours) : ").strip()
    while statut == "" or statut.isnumeric():
        print("Erreur de saisie : ")
        statut = input("Modifier le statut du ticket")
    try:
        query = """update tickets set statut = %s where id_ticket = %s"""
        cursor.execute(query, (statut, id_ticket))
        connection.commit()
        print("*" * 10)
        print(f"La demande est : {statut}")
    except Exception as e:
        print("Problème : ", e)
    finally: 
        cursor.close()
        connection.close()
############################################### Modifier le statut d'une demande #####################################
def update_ticket_user():
    connection = get_connexion()
    cursor = connection.cursor()
    print("Modifier mes demandes")
    id_ticket = input("Entrer l' id de la demande : ").strip()
    while id_ticket == "" or not id_ticket.isnumeric():
        print("Mauvause saisie")
        id_ticket = input("Entrer l' id de la demande : ").strip()
    titre = input("Modifier le titre de la demande : ").strip()
    while titre == "" or titre.isnumeric():
        print("Erreur de saisie : ")
        titre = input("Modifier le statut du ticket")
    description = input("Modifier la description de la demande : ").strip()
    while description == "" or description.isnumeric():
        print("Erreur de saisie : ")
        description = input("Modifier la description de la demande")
    niveau_urgence = input("Modifier le niveau d'urgence de la demande : ")
    while niveau_urgence == "" or niveau_urgence.isnumeric():
        print("Erreur de saisie : ")
        niveau_urgence = input("Modifier le niveau d'urgence de la demande")
    try:
        query = "update tickets set titre = %s, description = %s, niveau_urgence = %s  where id_ticket = %s and LOWER(statut) != %s"
        cursor.execute(query, (titre, description, niveau_urgence, id_ticket, "disponible"))
        connection.commit()
        print("*" * 10)
        print(f"La demande est modifié avec succès")
    except Exception:
        print("Imposible de modifier cette demande")
    finally: 
        cursor.close()
        connection.close()
############################################### Supprimer une demande #####################################
def del_demande():
    connection = get_connexion()
    cursor = connection.cursor()
    print("Modifier mes demandes")
    id_ticket = input("Entrer l' id de la demande : ").strip()
    while id_ticket == "" or not id_ticket.isnumeric():
        print("Mauvause saisie")
        id_ticket = input("Entrer l' id de la demande : ").strip()
    query = "SELECT statut FROM tickets WHERE id_ticket = %s"
    cursor.execute(query, (id_ticket,))
    result = cursor.fetchone()
    
    if not result:
        print(f"Le ticket avec l'ID {id_ticket} n'existe pas.")
        return
    
    statut = result[0]
    if statut.lower() == "disponible":
        print("Impossible de supprimer un ticket disponible.")
        return
    try:
        query = "delete from tickets where id_ticket = %s and statut != %s"
        cursor.execute(query, (id_ticket, "disponible"))
        connection.commit()
        print("*" * 10)
        print(f"La demande a été supprimé avec succès")
    except Exception as e:
        print(e)
    finally: 
        cursor.close()
        connection.close()



    


    
    
