Description

- 4 domaines de quiz sera disponible(Mathématiques, Statistiques, Programmation, Culture générale), l'utilisateur sélectionne un domaine
- 4 quuestions selon le domaine choisir

Chaque question  présente au moins 3 réponses possibles et l'utilisateur devra choisir au plus une seule réponse  (il n'a besoin de choisir forcément une réponse).
une réponse juste donne droit à un nombre de points défini, une mauvaise réponse ou une réponse nom proposée ou non choisir donne droit à zéro points
donner la possibilité au joeur de passer et de revenir à des questions 

il faudrait afficher à la fin le récaptulatif , le nombre de bonnes réponses et le score ou point total accumulé

présenter maintenant la correction, toute la correction

Types de données

-liste des domaines disponibles: Domainnes_quiz = ["Mathématiques", "Statistiques", "Programmation", "Culture générale"]
-identifiant de l'utilisateur : Joueur(pseudo)
-questions pour chaque domaine choisir : representer par des dictionnaires.

Déroulement

-demander l'identifiant du joueur
-afficher les dommaines de quiz
-demander le domaine que le joueur veut choisir
-présenter les questions selon le domaine
-le joueur saisir son choix pour chacune des questions
-metre à jour le score à chaque question
-afficher à chaque question , aller à la question précedente ou suivante
-afficher les résultats puis la correction

- Analyse

PP --> identifiant_joueur --> str
PP --> domaine_quiz 
PP --> Partie

Partie --> les_questions du domaine choisis

PP --> resultat_quiz
PP --> correction_quiz



