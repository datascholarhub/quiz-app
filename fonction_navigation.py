import time

listes_navigateur = ["Taper 2 pour aller à la question suivante",
          "Taper 1 pour aller aller a la question précédente",
          "Taper 0 pour aller à une question spécifique donnée"]

def print_texte(text):
    for char in text:
        print(char, end="", flush=True)
        time.sleep(0.05)
    print("\n")

def demander_et_controler(prompt, a, b):
    while True:
        print(prompt)
        reponse = input(">>>  ").strip()
        if reponse.isdigit():
            reponse_vrai = int(reponse)
            if a <= reponse_vrai <= b:
                return reponse_vrai
            else:
                print("Le nombre entrez ne se situe pas dans le bon intervalle.")
        else:
            print("Vous n'avez pas entrer un nombre")

def demander_identifiant():
    print("Bonjour, saisissez votre identifiant.")
    return input('>>> ')

def choisir_domaine(identifiant, domaines):
    print(f"Mr/Mlle {identifiant}.Bienvenue dans notre jeu de quizz.\nVeuillez sélectioner un domaine de quiz")
    print("  ")
    for i, domaine_quiz in enumerate(domaines, 1):
        print_texte(f"{i}-{domaine_quiz}")
    choix_domaine_quiz = demander_et_controler("", a=1, b=len(domaines))
    return choix_domaine_quiz

def demander_si_reponse_terminer():
    while True:
        print("Vous voulez entrer encore une autre réponse ? (oui ou non )")
        reponse = input(">>>  ")
        if not reponse.isdigit():
            reponse = reponse.lower().strip()
            if reponse in ["oui", "non"]:
                return reponse
            else:
                print("Vous devez entrer oui ou soit non")
        else:
            print("Vous avez entrez un nombre")


def index_autre_question(listes, compteur, questions, dictionnaire_user):
    for c in listes:
        print(c)
    choix = demander_et_controler(prompt='', a=0, b=2)
    if choix ==0:
        num_question = demander_et_controler('Entrer le numéro de la question',1, len(questions))
        compteur = num_question - 1
        dictionnaire_user[f'question{compteur+1}'].clear()
    elif choix == 1 and compteur > 0:
        compteur -=1
        dictionnaire_user[f'question{compteur+1}'].clear()
    elif choix == 2:
        compteur +=1
    else:
        print("Option mal choisie ou l'action ne peut pas être exécuté.")
        compteur +=1
    return compteur




def navigateur_choix_user(liste_reponse, index_question, dictionnaire_user):
    reponse_user_one = demander_et_controler(prompt="Entrer votre réponse:", a=1, b=len(liste_reponse))
    dictionnaire_user[f"question{index_question+1}"].append(reponse_user_one)
    choix_multiple = demander_si_reponse_terminer()
    while choix_multiple == "oui":
        reponse = demander_et_controler("Entrer votre réponse", 1, len(liste_reponse))
        dictionnaire_user[f"question{index_question+1}"].append(reponse)
        choix_multiple = demander_si_reponse_terminer()

    
def appreciation(notes, identifiant):
    nb_repondu = notes/5
    pourcentage = nb_repondu*25
    if notes < 5:
        print(f"{identifiant} vous avez répondu correctement à {nb_repondu} sur 4 questions soit {notes}/20 et {pourcentage}%.Mention Médiocre")
    elif 5<= notes <=10:
        print(f"{identifiant}  vous avez répondu correctement à {nb_repondu} sur 4 questions soit {notes}/20 et {pourcentage}%.Mention Passale")
    elif 10<= notes <=15:
        print(f"{identifiant} avez répondu correctement à {nb_repondu} sur 4 questions soit {notes}/20 et {pourcentage}%.Mention Bien")
    else:
        print(f"{identifiant} vous avez répondu correctement à {nb_repondu} sur 4 questions soit {notes}/20 et {pourcentage}%.Mention Très bien")