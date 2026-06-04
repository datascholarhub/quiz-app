## 1. Description Générale
Il s'agit d'une application interactive fonctionnant dans console, qui au lancement demande à l'utilisateur son nom d'utlisateur et lui présente les fonctionnalités de l'application

### Menu Principal 
L'utilisateur peut choisir parmis les fonctionnalités suivantes:

* **Participez à un Quiz** : Lancer une session de questions après avoir choisir un domaine
* **Résultats** : Consulter les solutions et les scores détaillées
* **Tableau de bord** : Visualisez l'historique et l'historiques des quiz effectués
* **Aide** : Comprendre le fonctionnement global de l'appli.

## 2. Spécifications fonctionnelles

### 2-1. Participer à un quiz
1. **Sélection  d'un domaine ou thème:** : Afficher à l'utilisateur les thèmes disponibles:
    * Statistiques
    * Programmation en Python
    * Amour et Divertissement
    * ..... autres domaines à venir
2. **Types de questions gérés:**
    * QCM / choix unique
    * question ouverte
    * Avoir une liste ou une structure de données bien déterminée pour stocker les questions
3.  **Navigation pendant le quiz:**
    * Le sytème affiche en bas retour à la question précédente à partir de la deuxième question et question suivante à partir de la deuxième question
    * le sytème doit permettre à l'utilisateur de passer à une question suivante même si la question en cours n'est pas encore répondue 
4.  **Calcul du score**
5.  **Fin du quiz et validation**
    * Une fois toutes les questions parcourues, **un récaputulatif** des réponses et demande une validation définitive des réponses
    * on affiche un message à l'utilisatueur indiquant à l'utilisateur  de voir les résultats à la section **Résultats**

### 2-2. **Résultats**
    * Donnez le score obtenu après le test et affichez un message selon le score obtenu (bien, Assez bien, Tbien, Excellent)
### 2-3. **Tableau de bord**
    * Le sytème doit reconnaitre l'utilisateur et montrez ses scores avant s'il revient la deuxième fois pour jouer
### 2-4. **Aide**
    *Guider les utilisateurs pour l'utilisation de l'application