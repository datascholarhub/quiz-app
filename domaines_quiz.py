"""" 
Ce fichier comporte les données dont nous avons besoins pour notre projet
"""


domaines_quiz =                             ["Culture générale", "Mathématiques", "Statistiques", "Programmation_Pythpn"]

questions_reponses_domaine_culture_geneale = { "En quelle année Christophe Colombe a découvert l'Amérique ?":
                                            [1975, 1907, 2000, 1492],
                                            "Qui a proposé la théorie de la relativité ?":
                                              ["Isaac Newton", "Albert Einstein", "Blaise Pascal", "Bill Gattes"],
                                            "Quel est le nom de l'entreprise qui a dévloppé ChatGPT ?":
                                              ["google.com", "microsoft.com", "meta.com", "openai.com"],
                                            "Quel est le nom exact proposé par Alain Turing pour évaluer l'intellignece d'une machine ?":
                                            ["Intelligence of Machine","Test IM", "Test de Turing", "Test de Pascal"],
                                            }

correction_culture_generale =              {"Question1": [4],
                                            "Question2": [2],
                                            "Question3": [4],
                                            "Question4": [3]
                                            }

questions_reponses_domaine_maths =    {"Si deux entiers naturels a et b sont premiers entre eux alors":
                                      ["pgcd(a,b)=1", "pgcd(a,b)*ppcm(a,b)=a*b", "ppcm(a,b) = a*b"],
                                        "Le calcul du déterminant d'une matrice":
                                          ["Est toujours possible", "n'est possible lorsque la matrice est une matrice carrée", "Est toujours non nul lorque la matrice existe"],
                                        "Une matrice est inverssible lorsque:" :
                                          ["elle est une matrice carrée", "son déterminant est nul", "son déterminant est non nul"],
                                        "L'intégrale de Riemann en 0 est convergente si et seulement si":
                                        ["alpha =1", "alpha > 1", "alpha < 1"],
                                      }

correction_maths                  =    {"Question1": [1],
                                      "Question2": [2],
                                      "Question3": [3],
                                      "Question4": [2]
                                      }

questions_reponses_domaine_statistiques = {
                                        "La statistique est la science de ... : " :
                                        ["collecte", "d'analyse", "de sport", "de prise de décision"],
                                        "Lors de l'analyse univariée d'une variable qualitative nominale, le(s) graphique(s) adaptés est(sont) : " :
                                        ["le nuage de point ou scatter plot", "l'histogramme", "le diagramme en barres ou en bandes", "le diagramme en secteur (camembert)"],
                                        "Lors de l'analyse de deux variables qualitatives, l'indicateur(s) possiles qu'on peut calculer est(sont)":
                                        ["La covariance", "La moyenne", "le coefficient de cramer", "la statistique de chi2"],
                                        "Quelle est l'interpretation de la p_value d'un test statistique de niveau alpha ?":
                                        ["Si p_value=0 alors on accepte l'hypothèse nulle", "si p_value > alpha alors on rejette l'hypothèse nulle", "si p_value < alpha alors on rejette l'hupothèse alternative", "Aucne interprètation n'est juste"]
                                        }

correction_stat =                     {"Question1": [1, 2, 4],
                                      "Question2": [3, 4],
                                      "Question3": [3, 4],
                                      "Question4": [4]
                                      }

questions_reponses_domaine_programmation_python = {
                                                  "Comment affiche-t-on un texte à l'écran ?":
                                                  ["print()", "input()", "show()", "display()"],
                                                  "Les tuples sont des ojects ...":
                                                  ["Immuables", "Muables", "Ordonnés", "Non ordonnés"],
                                                  " Que sognifie 00P : ":
                                                  ["Programmation Orientée Object", "Optimisation Oject Python", "Oject Orienté Programme", "Programmation Orientée Opération"],
                                                  "Comment créer une classe en python ?":
                                                  ["class", "New_class", "Class", "Classe"]
                                                  }

correction_python =                               {"Question1": [1],
                                                  "Question2": [1, 4],
                                                  "Question3": [1],
                                                  "Question4": [1]
                                                  }

donnees_domaines =                                {
                                                    1: (questions_reponses_domaine_culture_geneale, correction_culture_generale),
                                                    2: (questions_reponses_domaine_maths, correction_maths),
                                                    3: (questions_reponses_domaine_statistiques, correction_stat),
                                                    4: (questions_reponses_domaine_programmation_python, correction_python)
                                                  }
    