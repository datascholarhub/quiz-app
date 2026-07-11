from domaines_quiz import *
from classe_quiz import *

def main():
    identifiant = demander_identifiant()
    domaine_index = choisir_domaine(identifiant, domaines_quiz)
    questions_reponses=donnees_domaines[domaine_index][0]
    correction=donnees_domaines[domaine_index][1]
    quiz = Quiz(questions_reponses, correction, identifiant)
    quiz.lancer_Quiz()
    quiz.recapitulatif()
    quiz.score_quiz()
    quiz.afficher_correction()


if __name__ == "__main__":
    main()