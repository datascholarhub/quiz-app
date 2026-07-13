from collections import defaultdict
from fonction_navigation import*

class Quiz:
    def __init__(self, questions_reponses=dict, correction=dict, identifiant=str):
        self.questions_reponses = list(questions_reponses.items())
        self.index_question = 0
        self.reponses_user_questions = defaultdict(list)
        self.correction = correction                       
        self.score = 0
        self.identifiant = identifiant


    def afficher_questions(self):
        """
        Récupère la questionn actuelle du domaine selon l'index, l'affiche à l'écran ainsi
        que ses réponses.
        """
        tuple_questions_reponses = self.questions_reponses[self.index_question]
        question = tuple_questions_reponses[0]
        num_question = self.index_question + 1
        reponses = tuple_questions_reponses[1]
        print(f"{num_question}. {question} \n")
        for id_option, reponse in enumerate(reponses, 1):
            print(f"{id_option}) {reponse} ")


    def lancer_Quiz(self):
        """
        Ici c'est le coeur du code, recupère les réponses du joueur et les stocke dans
        un dictionnaire en faisant toutes les manipulations correctes.
        """
        print(f"Mr/Mlle {self.identifiant} pour chaque question, vous êtes amené à choisir une ou plusieurs réponses correspondantes.")
        while self.index_question < len(self.questions_reponses):
            self.afficher_questions()
            liste_reponse = self.questions_reponses[self.index_question][1]
            navigateur_choix_user(liste_reponse, self.index_question, self.reponses_user_questions)
            self.index_question = index_autre_question(listes_navigateur, self.index_question, self.questions_reponses, self.reponses_user_questions)
        print_texte("\n Partie Terminée.")

    def recapitulatif(self):
        """
        Faire le recapitulatif des réponses, afficher le numéro de la question et 
        les réponses du joueur
        """
        print("\nRécapitulatif des réponses\n")
        for questions, reponses in self.reponses_user_questions.items():
            reponses = ','.join(str(r) for r in reponses)
            question = questions.replace('question', "question n°")
            print(f'{question}: {reponses}')

    def score_quiz(self):
        """
        Faire la comparaison entre les réponses du joueur et la correction proposée puis affucher 
        le score et une appréciation.
        """
        for question in self.reponses_user_questions:
            reponse_user = self.reponses_user_questions[question]
            reponse_question = self.correction[question]
            reponse_question.sort()
            reponse_user.sort()
            if reponse_user == reponse_question:
                self.score +=5
        appreciation(self.score, self.identifiant)

    def afficher_correction(self):
        """
        Afficher la correction de toutes les questions
        """
        print("\nCorrection Quiz\n")
        for questions, reponses in self.correction.items():
            reponses = ','.join(str(r) for r in reponses)
            question = questions.replace('question', "question n°")
            print(f'{question}: {reponses}')
        if self.score < 20:
            print(f" Mr/Mlle {self.identifiant} Nous vous prions de bien vouloir défiler en haut pour revoir les bonnes réponses que nous avions\
        \ndonné des questions que vous avez ratées.")


        

