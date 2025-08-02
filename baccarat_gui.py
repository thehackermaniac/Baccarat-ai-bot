import tkinter as tk
from tkinter import ttk, messagebox
import pandas as pd
import joblib
import numpy as np

class BaccaratPredictor:
    def __init__(self, root):
        self.root = root
        self.root.title("Prédicteur de Baccarat")
        self.root.geometry("800x600")
        
        # Load the trained model
        try:
            self.model = joblib.load("baccarat_model.pkl")
        except FileNotFoundError:
            messagebox.showerror("Erreur", "Modèle non trouvé. Veuillez d'abord entraîner le modèle.")
            return
        
        # Initialize game history
        self.game_history = []
        self.current_streak = 0
        self.current_streak_type = None
        
        self.setup_ui()
    
    def setup_ui(self):
        # Main frame
        main_frame = ttk.Frame(self.root, padding="10")
        main_frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
        
        # Title
        title_label = ttk.Label(main_frame, text="Prédicteur de Baccarat", font=("Arial", 16, "bold"))
        title_label.grid(row=0, column=0, columnspan=3, pady=(0, 20))
        
        # Input section
        input_frame = ttk.LabelFrame(main_frame, text="Saisir le résultat", padding="10")
        input_frame.grid(row=1, column=0, columnspan=3, sticky=(tk.W, tk.E), pady=(0, 20))
        
        ttk.Label(input_frame, text="Résultat:").grid(row=0, column=0, padx=(0, 10))
        
        self.result_var = tk.StringVar()
        result_combo = ttk.Combobox(input_frame, textvariable=self.result_var, 
                                   values=["Player", "Banker", "Tie"], state="readonly")
        result_combo.grid(row=0, column=1, padx=(0, 10))
        
        add_button = ttk.Button(input_frame, text="Ajouter Résultat", command=self.add_result)
        add_button.grid(row=0, column=2)
        
        # Prediction section
        prediction_frame = ttk.LabelFrame(main_frame, text="Prédiction", padding="10")
        prediction_frame.grid(row=2, column=0, columnspan=3, sticky=(tk.W, tk.E), pady=(0, 20))
        
        self.prediction_label = ttk.Label(prediction_frame, text="Aucune prédiction disponible", 
                                         font=("Arial", 12))
        self.prediction_label.grid(row=0, column=0, columnspan=2)
        
        self.confidence_label = ttk.Label(prediction_frame, text="")
        self.confidence_label.grid(row=1, column=0, columnspan=2)
        
        predict_button = ttk.Button(prediction_frame, text="Prédire Prochain Résultat", 
                                   command=self.predict_next)
        predict_button.grid(row=2, column=0, pady=(10, 0))
        
        # Betting recommendation section
        betting_frame = ttk.LabelFrame(main_frame, text="Recommandation de Paris", padding="10")
        betting_frame.grid(row=3, column=0, columnspan=3, sticky=(tk.W, tk.E), pady=(0, 20))
        
        self.betting_label = ttk.Label(betting_frame, text="Aucune recommandation disponible", 
                                      font=("Arial", 11))
        self.betting_label.grid(row=0, column=0)
        
        # History section
        history_frame = ttk.LabelFrame(main_frame, text="Historique des Résultats", padding="10")
        history_frame.grid(row=4, column=0, columnspan=3, sticky=(tk.W, tk.E, tk.N, tk.S), pady=(0, 20))
        
        # Treeview for history
        self.history_tree = ttk.Treeview(history_frame, columns=("Game", "Result", "Streak"), show="headings", height=8)
        self.history_tree.heading("Game", text="Partie")
        self.history_tree.heading("Result", text="Résultat")
        self.history_tree.heading("Streak", text="Série")
        
        self.history_tree.column("Game", width=80)
        self.history_tree.column("Result", width=100)
        self.history_tree.column("Streak", width=80)
        
        scrollbar = ttk.Scrollbar(history_frame, orient="vertical", command=self.history_tree.yview)
        self.history_tree.configure(yscrollcommand=scrollbar.set)
        
        self.history_tree.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
        scrollbar.grid(row=0, column=1, sticky=(tk.N, tk.S))
        
        # Clear history button
        clear_button = ttk.Button(history_frame, text="Effacer Historique", command=self.clear_history)
        clear_button.grid(row=1, column=0, pady=(10, 0))
        
        # Configure grid weights
        main_frame.columnconfigure(0, weight=1)
        main_frame.rowconfigure(4, weight=1)
        history_frame.columnconfigure(0, weight=1)
        history_frame.rowconfigure(0, weight=1)
    
    def add_result(self):
        result = self.result_var.get()
        if not result:
            messagebox.showwarning("Attention", "Veuillez sélectionner un résultat.")
            return
        
        # Update streak
        if result == self.current_streak_type:
            self.current_streak += 1
        else:
            self.current_streak_type = result
            self.current_streak = 1
        
        # Add to history
        game_number = len(self.game_history) + 1
        self.game_history.append({
            'game': game_number,
            'result': result,
            'streak': self.current_streak
        })
        
        # Update history display
        self.history_tree.insert("", "end", values=(game_number, result, self.current_streak))
        
        # Scroll to bottom
        self.history_tree.see(self.history_tree.get_children()[-1])
        
        # Clear selection
        self.result_var.set("")
        
        # Auto-predict if we have enough history
        if len(self.game_history) >= 10:
            self.predict_next()
    
    def predict_next(self):
        if len(self.game_history) < 10:
            messagebox.showinfo("Information", "Au moins 10 résultats sont nécessaires pour faire une prédiction.")
            return
        
        # Calculate features for prediction
        recent_games = self.game_history[-10:]
        
        player_wins = sum(1 for game in recent_games if game['result'] == 'Player')
        banker_wins = sum(1 for game in recent_games if game['result'] == 'Banker')
        ties = sum(1 for game in recent_games if game['result'] == 'Tie')
        
        player_ratio = player_wins / 10
        banker_ratio = banker_wins / 10
        tie_ratio = ties / 10
        
        current_streak = self.current_streak
        
        # Make prediction
        features = np.array([[current_streak, player_ratio, banker_ratio, tie_ratio]])
        prediction = self.model.predict(features)[0]
        probabilities = self.model.predict_proba(features)[0]
        
        # Get class names
        classes = self.model.classes_
        max_prob_idx = np.argmax(probabilities)
        confidence = probabilities[max_prob_idx] * 100
        
        # Update prediction display
        self.prediction_label.config(text=f"Prédiction: {prediction}")
        self.confidence_label.config(text=f"Confiance: {confidence:.1f}%")
        
        # Generate betting recommendation
        self.generate_betting_recommendation(prediction, confidence, probabilities, classes)
    
    def generate_betting_recommendation(self, prediction, confidence, probabilities, classes):
        recommendation = ""
        
        if confidence > 60:
            recommendation = f"RECOMMANDÉ: Parier sur {prediction} (Confiance élevée: {confidence:.1f}%)"
        elif confidence > 45:
            recommendation = f"MODÉRÉ: Considérer parier sur {prediction} (Confiance moyenne: {confidence:.1f}%)"
        else:
            # Find the two highest probabilities
            sorted_indices = np.argsort(probabilities)[::-1]
            first_choice = classes[sorted_indices[0]]
            second_choice = classes[sorted_indices[1]]
            first_prob = probabilities[sorted_indices[0]] * 100
            second_prob = probabilities[sorted_indices[1]] * 100
            
            recommendation = f"PRUDENCE: Faible confiance. {first_choice} ({first_prob:.1f}%) ou {second_choice} ({second_prob:.1f}%)"
        
        self.betting_label.config(text=recommendation)
    
    def clear_history(self):
        self.game_history = []
        self.current_streak = 0
        self.current_streak_type = None
        
        # Clear treeview
        for item in self.history_tree.get_children():
            self.history_tree.delete(item)
        
        # Clear predictions
        self.prediction_label.config(text="Aucune prédiction disponible")
        self.confidence_label.config(text="")
        self.betting_label.config(text="Aucune recommandation disponible")

def main():
    root = tk.Tk()
    app = BaccaratPredictor(root)
    root.mainloop()

if __name__ == "__main__":
    main()

