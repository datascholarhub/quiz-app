from collections import defaultdict
from fonction_navigation import*

class Quiz:
    def __init__(self, questions_reponses=dict, correction=dict, identifiant=str):
        
        self.questions_reponses = list(questions_reponses.items())   # une liste composée des tuples de deux éléments:
                                                                     # une question et une liste des réponses proposées pour la question
        self.index_question = 0
        self.reponses_user_questions = defaultdict(list)             # un dictionnaire prenant pour valeur une liste préparée à 
                                                                     # prendre le numéro de la question et les réponses du joueur
        self.correction = correction                                 # un dictionnaire des questions et de leurs réponses
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
        print_texte(f"Mr/Mlle {self.identifiant} pour chaque question, vous êtes amené à choisir une ou plusieurs réponses correspondantes.")
        while self.index_question < len(self.questions_reponses):
            self.afficher_questions()
            liste_reponse = self.questions_reponses[self.index_question][1]
            reponse_user = demander_et_controler(prompt="Entrer votre réponse:", a=1, b=len(liste_reponse))
            self.reponses_user_questions[f"Question{self.index_question+1}"].append(reponse_user)
            choix_multiple = demander_si_reponse_terminer()
            while choix_multiple == "oui":
                reponse_multiple = demander_et_controler("Entrer votre réponse: ", 1, len(liste_reponse))
                self.reponses_user_questions[f"Question{self.index_question+1}"].append(reponse_multiple)
                choix_multiple = demander_si_reponse_terminer()
            choix_navigateur = demander_et_controler("Vous voulez passer à une autre question ? Taper 1 pour aller à la question suivante, -1 pour aller à la question précédente ou 0 pour aller sur une question spécifique.", -1, 1)
            if choix_navigateur == 1:
                self.index_question += 1
            elif choix_navigateur==-1 and self.index_question>0:
                self.index_question -=1
                cle_question = f"Question{self.index_question}"
                self.reponses_user_questions[cle_question].clear()
            elif choix_navigateur ==0:
                num_question = demander_et_controler("Veuillez entrez le numéro de la question", 1, 4)
                self.index_question = num_question-1
            else:
                print_texte("Option mal choisir ou vous ne pouvez par aller à la question précédente")
                choix_navigateur = demander_et_controler("Vous voulez passer à une autre question ? Taper 1 pour aller à la question suivante, -1 pour aller à la question précédente ou 0 pour aller sur une question spécifique.", -1, 1)
        print_texte("\n Partie Terminée.")

    def recapitulatif(self):
        """
        Faire le recapitulatif des réponses, afficher le numéro de la question et 
        les réponses du joueur
        """
        print("\nRécapitulatif des réponses\n")
        for question, reponses in self.reponses_user_questions.items():
            reponses = ','.join(str(r) for r in reponses)
            Question = question.replace('Question', "Question n°")
            print(f'{Question}: {reponses}')

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
        print_texte("\nCorrection Quiz\n")
        for question, reponses in self.correction.items():
            reponses = ','.join(str(r) for r in reponses)
            Question = question.replace('Question', "Question n°")
            print_texte(f'{Question}: {reponses}')
        if self.score < 20:
            print_texte(f" Mr/Mlle {self.identifiant} Nous vous prions de bien vouloir défiler en haut pour revoir les bonnes réponses que nous avions\
        \ndonné des questions que vous avez ratées.")


        

