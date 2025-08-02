import tkinter as tk
from tkinter import ttk

def test_gui():
    root = tk.Tk()
    root.title("Test GUI")
    root.geometry("300x200")
    
    label = ttk.Label(root, text="Interface graphique fonctionne!")
    label.pack(pady=50)
    
    button = ttk.Button(root, text="Fermer", command=root.quit)
    button.pack()
    
    # Auto-close after 3 seconds for testing
    root.after(3000, root.quit)
    
    root.mainloop()
    print("Test GUI terminé avec succès")

if __name__ == "__main__":
    test_gui()

