## Description

- 4 domaines de quiz sera disponible(Mathématiques, Statistiques, Programmation_Python, Culture générale), l'utilisateur sélectionne un domaine
- 4 quuestions selon le domaine choisir

Chaque question  présente au moins 3 réponses possibles et l'utilisateur devra choisir au moins une réponse.
une réponse juste donne droit à un nombre de points défini, une mauvaise réponse ou une réponse nom proposée ou non choisir donne droit à zéro points
donner la possibilité au joeur de passer à la question suivante sans chosir une réponse et de revenir à des questions précédente.

il faudrait afficher à la fin le récaptulatif : Toutes les questions et les réponses que la personne à choisir , le nombre de bonnes réponses et le score ou point total accumulé et renvoyer à la personne la correction des questions qu'elles n'a pas réussi uniquement.


## Types de données

-liste des domaines disponibles: Domainnes_quiz = ["Mathématiques", "Statistiques", "Programmation_Python", "Culture générale"]
-identifiant de l'utilisateur : str
-questions pour chaque domaine choisir : representer par des dictionnaires.

## Déroulement

-demande l'identifiant du joueur
-afficher les dommaines de quiz
-demander le domaine que le joueur veut choisir
    -Afficher la première question du domaine X choisi
    -Permettre à l'utilisateur de saisir son choix
    -Demande à l'utilisateur si il veut saisir encore une autre réponse 
       -si oui on lui redonne la main de saisir 
       -si non
    -On affiche à l'écran deux textes
       -aller à la question précédente en tapant 0 
         --on lui donne la main et il tape 0
       -aller à la question suivante en tapant 1
         --on lui donne la main et il tape 1
    --Afficher la question 2 du domaine X maintenant que la personne à taper 1
    -le joueur saisir son choix pour chacune des question
    TANT QUE LES QUESTIONS DU DOMAINE RESTE ON REFAIT LA MEME PROCEDURE
    -On montre le récaputulatif des questions et réponses du joueur
    -Demander si il veut Envoyer ses réponses 
    -Afficher son score avec une mention
    -Afficher la correction des questions qu'il a perdu
    -Aficher Parti terminer
    -Demander si il veut rejouer une aute partie
    -TANT QU'IL DIT OUI ON RECOMMENCE A PARTI DE DOMAINE QUIZ
    -

## Analyse

PP --> demander_identifiant_joeur ---> str
PP --> affiche_domaines_quiz
PP --> demander_domaine_quiz --> Entier

PP --> Partie1

Partie1 (affiche_questions_domaines) --> Partie2
Partie2 --> afficher_la_premiere_question
Partie2 --> demander_sa_reponse
       --> demander_si il y a une autre réponse à chosir
          --> si oui
          --> demander_sa_reponse
          --> si non
      --> afficher_la_deuxière_question
      --> demander_sa_reponse
      --> demander_si il y a une autre réponse à chosir
          --> si oui
          --> demander_sa_reponse
          --> si non
     --> Demander_aller_a_la question précédente (0) où suivante(1)
        --> si oui(1) aller_a_la question suivante
        --> si non aller à la question précédente
     --> ......
     --> afficher_derniere_question
     --> a la fin 
     --> demander_question précédente ou Terminer

PP--> afficher_recapitulatif
PP--> donner_score et mention
PP--> afficher_les_corrections des questions perdues
PP--> demander quitter ou jouer une recommencer une autre partie


