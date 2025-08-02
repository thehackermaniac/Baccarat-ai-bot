# Prédicteur de Baccarat - Modèle Prédictif avec Interface Graphique

## Description du Projet

Ce projet développe un modèle prédictif pour les résultats de baccarat en utilisant des données historiques de jeu. L'application comprend une interface graphique Python permettant de saisir les résultats en temps réel et de recevoir des recommandations de paris basées sur l'analyse statistique et l'apprentissage automatique.

## Fonctionnalités Principales

- **Collecte et traitement de données** : Analyse de 100 000 parties de baccarat simulées
- **Ingénierie des caractéristiques** : Calcul des séries gagnantes, ratios de victoires, et autres métriques prédictives
- **Modèle d'apprentissage automatique** : Utilisation de Random Forest pour la prédiction des résultats
- **Interface graphique intuitive** : Application Tkinter pour la saisie des résultats et l'affichage des prédictions
- **Recommandations de paris** : Suggestions basées sur la confiance du modèle

## Structure du Projet

```
baccarat-predictor/
├── data/                          # Données historiques de baccarat (100k fichiers JSON)
├── process_baccarat_data.py       # Script de traitement des données brutes
├── feature_engineering.py        # Script d'ingénierie des caractéristiques
├── train_model.py                # Script d'entraînement du modèle
├── baccarat_gui.py               # Interface graphique principale
├── run_baccarat_app.py           # Script de lancement de l'application
├── test_gui.py                   # Script de test de l'interface
├── baccarat_outcomes.csv         # Données traitées des résultats
├── baccarat_features.csv         # Données avec caractéristiques engineerées
├── baccarat_model.pkl            # Modèle entraîné sauvegardé
└── README.md                     # Cette documentation
```

## Installation et Configuration

### Prérequis

- Python 3.11+
- Système Ubuntu/Linux (pour tkinter)
- Connexion Internet pour le téléchargement des données

### Installation des Dépendances

```bash
# Installer les packages système nécessaires
sudo apt-get update
sudo apt-get install -y python3-tk

# Installer les packages Python
pip install pandas scikit-learn joblib
```

### Téléchargement des Données

Les données historiques de baccarat sont automatiquement téléchargées depuis Kaggle lors de la première exécution. Le dataset contient 100 000 parties simulées avec des jeux de 8 cartes.

## Utilisation

### Lancement de l'Application

```bash
# Méthode 1 : Lancement direct
python3 baccarat_gui.py

# Méthode 2 : Utilisation du script de lancement
python3 run_baccarat_app.py
```

### Interface Utilisateur

L'application présente plusieurs sections :

1. **Saisie des Résultats** : Menu déroulant pour sélectionner Player, Banker, ou Tie
2. **Prédictions** : Affichage du prochain résultat prédit avec niveau de confiance
3. **Recommandations de Paris** : Suggestions basées sur la confiance du modèle
4. **Historique** : Tableau des résultats précédents avec séries gagnantes

### Workflow d'Utilisation

1. Sélectionnez le résultat de la partie dans le menu déroulant
2. Cliquez sur "Ajouter Résultat" pour l'enregistrer
3. Après 10 résultats, le modèle génère automatiquement des prédictions
4. Consultez les recommandations de paris basées sur la confiance
5. Utilisez "Effacer Historique" pour recommencer une nouvelle session

## Méthodologie Technique

### Traitement des Données

Le script `process_baccarat_data.py` :
- Lit les 100 000 fichiers JSON de parties simulées
- Calcule les scores des mains Player et Banker selon les règles du baccarat
- Détermine le gagnant de chaque partie
- Génère un fichier CSV consolidé

### Ingénierie des Caractéristiques

Le script `feature_engineering.py` crée :
- **Séries gagnantes** : Longueur de la série actuelle pour chaque type de résultat
- **Ratios glissants** : Pourcentages de victoires sur une fenêtre de 10 parties
- **Indicateurs binaires** : Variables pour Player, Banker, et Tie

### Modèle d'Apprentissage

Le modèle utilise :
- **Algorithme** : Random Forest Classifier avec 100 arbres
- **Caractéristiques** : Série actuelle, ratios Player/Banker/Tie
- **Validation** : Division 80/20 pour entraînement/test
- **Équilibrage** : Pondération des classes pour gérer les déséquilibres

### Métriques d'Évaluation

Le modèle est évalué sur :
- **Précision (Accuracy)** : Pourcentage de prédictions correctes
- **Précision pondérée** : Précision ajustée pour les classes déséquilibrées
- **Rappel pondéré** : Capacité à identifier tous les cas positifs
- **F1-Score pondéré** : Moyenne harmonique de précision et rappel

## Recommandations de Paris

Le système génère trois types de recommandations :

### Confiance Élevée (>60%)
- **Action** : RECOMMANDÉ
- **Message** : "Parier sur [Résultat] (Confiance élevée: X%)"

### Confiance Moyenne (45-60%)
- **Action** : MODÉRÉ
- **Message** : "Considérer parier sur [Résultat] (Confiance moyenne: X%)"

### Confiance Faible (<45%)
- **Action** : PRUDENCE
- **Message** : "Faible confiance. [Option1] (X%) ou [Option2] (Y%)"

## Limitations et Considérations

### Limitations Techniques
- Le modèle nécessite au moins 10 résultats pour générer des prédictions
- La précision dépend de la qualité et de la représentativité des données d'entraînement
- Les prédictions sont basées sur des patterns statistiques, pas sur des certitudes

### Considérations Éthiques
- **Avertissement** : Ce logiciel est destiné à des fins éducatives et de recherche
- **Responsabilité** : L'utilisateur est responsable de ses décisions de paris
- **Risques** : Les jeux d'argent comportent des risques financiers importants

### Limitations du Baccarat
- Le baccarat est un jeu de hasard avec un avantage de la maison
- Les résultats passés n'influencent pas les résultats futurs (indépendance statistique)
- Aucun système ne peut garantir des gains à long terme

## Développement et Maintenance

### Structure du Code
- **Modularité** : Chaque phase du pipeline est dans un script séparé
- **Réutilisabilité** : Les fonctions peuvent être adaptées pour d'autres jeux
- **Extensibilité** : Nouvelles caractéristiques peuvent être ajoutées facilement

### Tests et Validation
- Test de l'interface graphique avec `test_gui.py`
- Validation croisée du modèle lors de l'entraînement
- Vérification de la cohérence des données

### Améliorations Futures
- Intégration de modèles plus sophistiqués (réseaux de neurones, LSTM)
- Ajout de caractéristiques avancées (patterns complexes, analyse temporelle)
- Interface web pour une meilleure accessibilité
- Intégration avec des APIs de casinos en ligne (où légal)

## Support et Contact

Pour des questions techniques ou des améliorations :
- Vérifiez que toutes les dépendances sont installées
- Assurez-vous que les fichiers de données sont présents
- Consultez les logs d'erreur pour le débogage

## Licence et Responsabilité

Ce projet est fourni "tel quel" sans garantie. L'utilisation pour des paris réels est à vos risques et périls. Respectez les lois locales concernant les jeux d'argent.

