# Guide d'Installation - Prédicteur de Baccarat

## Installation Complète Étape par Étape

### 1. Préparation du Système

#### Ubuntu/Debian
```bash
# Mise à jour du système
sudo apt-get update
sudo apt-get upgrade -y

# Installation de Python et des outils de développement
sudo apt-get install -y python3 python3-pip python3-dev python3-tk

# Vérification de l'installation
python3 --version
pip3 --version
```

#### CentOS/RHEL/Fedora
```bash
# Pour CentOS/RHEL
sudo yum update -y
sudo yum install -y python3 python3-pip python3-tkinter

# Pour Fedora
sudo dnf update -y
sudo dnf install -y python3 python3-pip python3-tkinter
```

#### macOS
```bash
# Installation avec Homebrew
brew install python-tk

# Ou utiliser le Python système avec tkinter déjà inclus
```

#### Windows
```bash
# Télécharger Python depuis python.org (inclut tkinter)
# Ou utiliser Windows Subsystem for Linux (WSL)
```

### 2. Installation des Dépendances Python

```bash
# Installation des packages requis
pip3 install pandas scikit-learn joblib numpy

# Vérification des installations
python3 -c "import pandas, sklearn, joblib, numpy; print('Toutes les dépendances sont installées')"
```

### 3. Téléchargement du Projet

#### Option A : Téléchargement Direct
```bash
# Créer un répertoire pour le projet
mkdir baccarat-predictor
cd baccarat-predictor

# Télécharger les fichiers du projet (remplacer par l'URL réelle)
# wget [URL_DU_PROJET]/baccarat-predictor.zip
# unzip baccarat-predictor.zip
```

#### Option B : Copie Manuelle
```bash
# Copier tous les fichiers Python dans le répertoire du projet
# - process_baccarat_data.py
# - feature_engineering.py
# - train_model.py
# - baccarat_gui.py
# - run_baccarat_app.py
# - test_gui.py
```

### 4. Configuration des Données

#### Téléchargement Automatique (Recommandé)
```bash
# Le script téléchargera automatiquement les données depuis Kaggle
# Aucune action manuelle requise
```

#### Téléchargement Manuel (Si nécessaire)
```bash
# 1. Créer un compte sur Kaggle.com
# 2. Aller sur : https://www.kaggle.com/datasets/victornascimento/baccarat-dataset
# 3. Télécharger le dataset
# 4. Extraire dans le dossier 'data/'
mkdir data
# Copier les fichiers JSON dans le dossier data/
```

### 5. Test de l'Installation

#### Test des Dépendances
```bash
python3 test_gui.py
```

#### Test du Traitement des Données
```bash
# Si les données sont présentes
python3 process_baccarat_data.py
```

#### Test de l'Entraînement du Modèle
```bash
python3 train_model.py
```

### 6. Lancement de l'Application

```bash
# Lancement complet
python3 run_baccarat_app.py

# Ou lancement direct de l'interface
python3 baccarat_gui.py
```

## Résolution des Problèmes Courants

### Erreur : "No module named 'tkinter'"

#### Ubuntu/Debian
```bash
sudo apt-get install python3-tk
```

#### CentOS/RHEL
```bash
sudo yum install tkinter
# ou
sudo yum install python3-tkinter
```

#### macOS
```bash
# Réinstaller Python avec tkinter
brew reinstall python-tk
```

### Erreur : "No module named 'sklearn'"

```bash
pip3 install scikit-learn
# ou
pip3 install --upgrade scikit-learn
```

### Erreur : "Permission denied"

```bash
# Donner les permissions d'exécution
chmod +x run_baccarat_app.py
chmod +x *.py
```

### Erreur : "Display not found" (Serveurs sans interface graphique)

```bash
# Installer un serveur X virtuel
sudo apt-get install xvfb

# Lancer avec un display virtuel
xvfb-run -a python3 baccarat_gui.py
```

### Problèmes de Mémoire

```bash
# Pour les systèmes avec peu de RAM, traiter les données par lots
# Modifier process_baccarat_data.py pour traiter moins de fichiers à la fois
```

## Configuration Avancée

### Variables d'Environnement

```bash
# Définir le chemin Python (optionnel)
export PYTHONPATH="${PYTHONPATH}:/chemin/vers/baccarat-predictor"

# Définir le display pour X11 (si nécessaire)
export DISPLAY=:0
```

### Configuration de Performance

```bash
# Pour améliorer les performances sur de gros datasets
export OMP_NUM_THREADS=4
export OPENBLAS_NUM_THREADS=4
```

### Installation dans un Environnement Virtuel (Recommandé)

```bash
# Créer un environnement virtuel
python3 -m venv baccarat-env

# Activer l'environnement
source baccarat-env/bin/activate  # Linux/macOS
# ou
baccarat-env\Scripts\activate     # Windows

# Installer les dépendances
pip install pandas scikit-learn joblib numpy

# Désactiver l'environnement quand terminé
deactivate
```

## Vérification de l'Installation

### Script de Vérification Complète

```bash
#!/bin/bash
echo "=== Vérification de l'Installation du Prédicteur de Baccarat ==="

echo "1. Vérification de Python..."
python3 --version || echo "ERREUR: Python3 non trouvé"

echo "2. Vérification des modules Python..."
python3 -c "import pandas; print('✓ pandas')" || echo "✗ pandas manquant"
python3 -c "import sklearn; print('✓ scikit-learn')" || echo "✗ scikit-learn manquant"
python3 -c "import joblib; print('✓ joblib')" || echo "✗ joblib manquant"
python3 -c "import tkinter; print('✓ tkinter')" || echo "✗ tkinter manquant"

echo "3. Vérification des fichiers du projet..."
[ -f "baccarat_gui.py" ] && echo "✓ Interface graphique" || echo "✗ baccarat_gui.py manquant"
[ -f "train_model.py" ] && echo "✓ Script d'entraînement" || echo "✗ train_model.py manquant"
[ -f "process_baccarat_data.py" ] && echo "✓ Script de traitement" || echo "✗ process_baccarat_data.py manquant"

echo "4. Test de l'interface graphique..."
python3 test_gui.py && echo "✓ Interface graphique fonctionnelle" || echo "✗ Problème avec l'interface"

echo "=== Vérification Terminée ==="
```

### Sauvegardez ce script comme `check_installation.sh` et exécutez :

```bash
chmod +x check_installation.sh
./check_installation.sh
```

## Support Technique

Si vous rencontrez des problèmes :

1. Vérifiez que toutes les dépendances sont installées
2. Assurez-vous d'avoir les permissions nécessaires
3. Vérifiez l'espace disque disponible (au moins 1 GB)
4. Consultez les logs d'erreur pour plus de détails
5. Testez avec l'environnement virtuel pour isoler les problèmes

## Mise à Jour

Pour mettre à jour le projet :

```bash
# Sauvegarder les données existantes
cp baccarat_model.pkl baccarat_model_backup.pkl

# Télécharger la nouvelle version
# Remplacer les fichiers Python

# Réentraîner le modèle si nécessaire
python3 train_model.py
```

