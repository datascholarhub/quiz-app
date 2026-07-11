"""
ce fichier comporte les fonctionnaire nécessaires pour la navigation de notre quiz.
"""

import time


def print_texte(text):
    for char in text:
        print(char, end="", flush=True)
        time.sleep(0.05)
    print("\n")

def demander_et_controler(prompt, a, b):
    while True:
        print_texte(prompt)
        reponse = input(">>>  ").strip()
        if reponse.isdigit():
            reponse_vrai = int(reponse)
            if a <= reponse_vrai <= b:
                return reponse_vrai
            else:
                print_texte("Le nombre entrez ne se situe pas dans le bon intervalle.")
        else:
            print_texte("Vous n'avez pas entrer un nombre")

def demander_identifiant():
    print_texte("Bonjour, saisissez votre identifiant.")
    return input('>>> ')

def choisir_domaine(identifiant, domaines):
    print_texte(f"Mr/Mlle {identifiant}.Bienvenue dans notre jeu de quizz.\nVeuillez sélectioner un domaine de quiz")
    print_texte("  ")
    for i, domaine_quiz in enumerate(domaines, 1):
        print_texte(f"{i}-{domaine_quiz}")
    choix_domaine_quiz = demander_et_controler("", a=1, b=4)
    return choix_domaine_quiz

def demander_si_reponse_terminer():
    while True:
        print_texte("Vous voulez entrer encore une autre réponse ? (oui ou non )")
        reponse = input(">>>  ")
        if not reponse.isdigit():
            reponse = reponse.lower().strip()
            return reponse
        else:
            print_texte("Vous avez entrez un nombre")

    
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