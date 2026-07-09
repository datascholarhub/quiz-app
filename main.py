from domaines_quiz import *
from main_two import *

def main():
    identifiant = demander_identifiant()
    domaine =""
    domaine_index = choisir_domaine(identifiant, domaines_quiz)
    if domaine_index == 1:
        domaine = questions_reponses_domaine_culture_geneale
        correction = correction_culture_generale
    if domaine_index == 2:
        domaine = questions_reponses_domaine_maths
        correction = correction_maths
    if domaine_index == 3:
        domaine = questions_reponses_domaine_statistiques
        correction = correction_stat
    if domaine_index == 4:
        domaine = questions_reponses_domaine_programmation_python
        correction = correction_python
    quiz = Quiz(domaine, correction, identifiant)
    quiz.lancer_Quiz()
    quiz.recapitulatif()
    quiz.score_quiz()


if __name__ == "__main__":
    main()