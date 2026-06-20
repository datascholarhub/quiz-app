domaines_quiz = ["Culture générale", "Mathématiques", "Statistiques", "Programmation"]

questions_domaine_culture_geneale = { "En quelle année Christophe Colombe a découvert l'Amérique":
                                       ([1975, 1907, 2000, 1492], 4),
                                      "Qui a proposé la théorie de la relativité":
                                        (["Isaac Newton", "Albert Einstein", "Blaise Pascal", "Bill Gattes"], 2),
                                      "Quel est le nom de l'entreprise qui a dévloppé ChatGPT":
                                        (["google.com", "microsoft.com", "meta.com", "openai.com"], 4),
                                      "Quel est le nom proposé par Alain Turing pour évaluer l'intellignece d'une machine":
                                      (["Test de Shannon","Test IM", "Test de Turing", "Test de Pascal"], 3),
                                   }
questions_domaine_maths = {  "Si deux entiers naturels a et b sont premiers ente eux alors":
                           (["pgcd(a,b)=1", "pgcd(a,b)*ppcm(a,b)=a*b", "ppcm(a,b) = a*b"], 1),
                             "Le calcul du déterminant d'une matrice":
                               (["Est toujours possible", "n'est possible lorque la matriceest une matrice carrée", "Est toujours non nul lorque la matrice existe"], 1),
                             "Une matrice est inverssible lorsque:" :
                               (["lorsqu'elle est une matrice carrée", "lorsque son déterminant est nul", "lorsque son déterminant est non nul"], 3),
                             "L'intégrale de Riemann en 0 est convergente si et seulement si":
                             (["alpha =1", "alpha > 1", "alpha < 1"], 3),
                          }


def demande_identifiant():
    return input('Veuillez saisir votre identifiant: ')

def affichage_personnaliser(texte):
    print()
    print(texte)
    print()

def choix_domaine_quiz():
    affichage_personnaliser(f"Bienvenue Mr/Mlle {demande_identifiant()} dans notre application quiz.Veuillez sélectionner un domaine pour commencer une partie.")
    for i, domaine_quiz in enumerate(domaines_quiz,1):
        print(f"{i}-{domaine_quiz}")
    domaine_quiz = int(input("\n==> "))
    return domaine_quiz
 

def affichage_des_questions(domaines):
    affichage_personnaliser("La partie à commencer.")
    affichage_personnaliser("Veuillez choisir la (les) bonne(s) réponse(s).")
    score_general = 0
    for question in domaines:
        affichage_personnaliser(f"{question}")
        for id, choix in enumerate(domaines[question][0], 1): 
            print(f"{id}) {choix}")
        affichage_personnaliser("Veuillez choisir une réponse.")
        reponse = int(input(f"==> "))
        if reponse == domaines[question][1]:
            score_general = score_general + 1 
    affichage_personnaliser(f"La partie est terminée. Votre score général est : {score_general}/{len(domaines)}, soit {score_general*25}%")

def main():
    choix = choix_domaine_quiz()
    if choix  == 1:
        affichage_des_questions(questions_domaine_culture_geneale)
    elif choix == 2:
        affichage_des_questions(questions_domaine_maths)


if __name__ == "__main__" :
    main()
