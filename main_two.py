from collections import defaultdict as df

def demander_identifiant():
    print("Bonjour, saisissez votre identifiant.")
    return input('>>> ')

def choisir_domaine(identifiant, domaines):
    print(f"{identifiant}. Veuillez sélectioner un domaine de quiz")
    for i, domaine_quiz in enumerate(domaines,1):
        print(f"{i}-{domaine_quiz}")
    choix_domaine_quiz = int(input("\n==> "))
    return choix_domaine_quiz

def demander_reponse():
    return int(input("Entrer votre réponse: "))

def demander_si_reponse_terminer():
    print("Vous voulez entrer encore une autre réponse ? (oui ou non )")
    return input(">>> ")

def demander_autre_question():
    print("Vous voulez passer à une autre question ? Taper 1 pour aller à la question suivante, -1 pour aller à la question précédente ou 0 pour aller sur une question spécifique.")
    return int(input(">>> "))
    
def appreciation(notes, identifiant):
    nb_repondu = notes/5
    pourcentage = nb_repondu*25
    if notes < 5:
        print(f"\n Mr\Mlle {identifiant} vous avez répondu correctement à {nb_repondu} sur 4 questions soit {notes}/20 et {pourcentage}%.Mention Médiocre\n")
    elif 5<= notes <=10:
        print(f"\n Mr\Mlle {identifiant}  vous avez répondu correctement à {nb_repondu} sur 4 questions soit {notes}/20 et {pourcentage}%.Mention Passale\n")
    elif 10<= notes <=15:
        print(f"\n Mr\Mlle {identifiant} avez répondu correctement à {nb_repondu} sur 4 questions soit {notes}/20 et {pourcentage}%.Mention Bien \n")
    else:
        print(f"\n Mr\Mlle {identifiant} vous avez répondu correctement à {nb_repondu} sur 4 questions soit {notes}/20 et {pourcentage}%.Mention Très bien \n")



class Quiz:
    def __init__(self, questions_reponses=dict, correction=dict, identifiant=str):
        self.questions_reponses = list(questions_reponses.items())
        self.index_question = 0
        self.reponses_user_questions = df(list)
        self.correction = correction
        self.score = 0
        self.identifiant = identifiant


    def afficher_questions(self):
        tuple_questions_reponses = self.questions_reponses[self.index_question]
        question = tuple_questions_reponses[0]
        num_question = self.index_question + 1
        reponses = tuple_questions_reponses[1]
        print(f"{num_question}. {question} \n")
        for id_option, reponse in enumerate(reponses, 1):
            print(f"{id_option}) {reponse} ")


    def lancer_Quiz(self):
        print("\n Pour chaque question, vous êtes amené à choisir un ou plusieurs réponses correspondant.\n")
        while self.index_question < len(self.questions_reponses):
            self.afficher_questions()
            print("\n ")
            reponse_user = demander_reponse()
            self.reponses_user_questions[f"Question{self.index_question+1}"].append(reponse_user)
            choix_multiple = demander_si_reponse_terminer()
            while choix_multiple == "oui":
                reponse_multiple = demander_reponse()
                self.reponses_user_questions[f"Question{self.index_question}"].append(reponse_multiple)
                choix_multiple = demander_si_reponse_terminer()
            
            choix_navigateur = demander_autre_question()
            if choix_navigateur == 1:
                self.index_question += 1
            elif choix_navigateur==-1 and self.index_question>0:
                self.index_question -=1
                cle_question = f"Question{self.index_question}"
                self.reponses_user_questions[cle_question].clear()
            elif choix_navigateur ==0:
                num_question = int("Entrer l'index de la question:  ")
                self.index_question = num_question
            else:
                print("Option mal choisir ou vous ne pouvez par aller à la question précédente")
                choix_navigateur = demander_autre_question()
        print("\n Partie Terminée.")

    def recapitulatif(self):
        print("\n Récapitulatif des réponses \n")
        for question, reponses in self.reponses_user_questions.items():
            reponses = ','.join(str(r) for r in reponses)
            Question = question.replace('Question', "Question n°")
            print(f'{Question}: {reponses}')

    def score_quiz(self):
        for question in self.reponses_user_questions:
            reponse_user = self.reponses_user_questions[question]
            reponse_question = self.correction[question]
            reponse_question.sort()
            reponse_user.sort()
            if reponse_user == reponse_question:
                self.score +=5
        appreciation(self.score, self.identifiant)

        

