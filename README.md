# Système de Suivi des Incidents

## Description du projet
Ce projet est un système simple de suivi des demandes/tickets pour gérer les incidents ou demandes utilisateurs.  
Il est développé en Python avec MySQL pour la gestion des données.

---

## Geste professionnel réalisé

Dans ce projet, plusieurs **bonnes pratiques professionnelles** ont été appliquées pour assurer la **fiabilité, la sécurité et la maintenabilité** du code :

1. **Gestion propre des ressources :**
   - Chaque fonction ouvre une connexion et un curseur au début.
   - Les curseurs et connexions sont fermés dans un bloc `finally`, garantissant que les ressources sont toujours libérées même en cas d'erreur.
   - Utilisation de `buffered=True` pour éviter les erreurs `Unread result found`.

2. **Validation des données utilisateur :**
   - Les entrées utilisateur sont systématiquement vérifiées (ex: email, titre, description, niveau d'urgence, ID de ticket).
   - Les données numériques et textuelles sont filtrées pour éviter les erreurs ou saisies invalides.
   - Vérification de l’existence d’un email avant création pour éviter les doublons.

3. **Gestion des statuts avec sensibilité à la casse :**
   - Les statuts comme `Disponible` ou `disponible` sont normalisés lors des comparaisons.
   - L’utilisation de `LOWER(statut)` dans SQL permet d’éviter les erreurs liées à la casse.

4. **Sécurité des mots de passe :**
   - Les mots de passe sont stockés sous forme hashée avec `bcrypt`.
   - Vérification sécurisée lors de la connexion.

5. **Gestion des erreurs :**
   - Chaque opération critique (INSERT, UPDATE, DELETE) est entourée d’un `try/except` pour capturer et afficher les erreurs.
   - Les messages d’erreur sont clairs pour l’utilisateur et facilitent le debug pour le développeur.

6. **Structure du code et lisibilité :**
   - Chaque opération CRUD est encapsulée dans sa propre fonction.
   - Messages clairs pour l’utilisateur.
   - Code commenté et structuré pour faciliter la maintenance future.

---

## Résultat attendu

- Les tickets peuvent être créés, consultés, modifiés et supprimés de manière sécurisée.
- Les tickets avec le statut “Disponible” ne peuvent pas être modifiés ou supprimés.
- Les données utilisateur sont protégées et validées.
- La base de données reste propre et aucune ressource n’est laissée ouverte inutilement.

---

## Conclusion

Le geste professionnel réalisé dans ce projet consiste à **appliquer des bonnes pratiques de développement backend** : gestion des ressources, validation des entrées, sécurité des mots de passe, et robustesse face aux erreurs.  
Ces pratiques permettent de créer un code fiable, maintenable et sécurisé, prêt à évoluer vers un projet plus complexe ou une application en production.
