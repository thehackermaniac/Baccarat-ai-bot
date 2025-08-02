#!/usr/bin/env python3
import os
import sys
import pandas
def main():
    # Check if model exists
    if not os.path.exists("baccarat_model.pkl"):
        print("Modèle non trouvé. Entraînement du modèle en cours...")
        os.system("python train_model.py")
    
    # Launch the GUI application
    print("Lancement de l'application de prédiction de baccarat...")
    os.system("python baccarat_gui.py")

if __name__ == "__main__":
    main()

