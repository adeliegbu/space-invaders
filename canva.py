import tkinter as tk

fenetre = tk.Tk()
fenetre.title("Disposition avec Grid")
fenetre.geometry("300x200")

label1 = tk.Label(fenetre, text="Label 1")
label1.grid(row=0, column=0)  # Première ligne, première colonne

label2 = tk.Label(fenetre, text="Label 2")
label2.grid(row=0, column=1)  # Première ligne, deuxième colonne

label3 = tk.Label(fenetre, text="Label 3")
label3.grid(row=1, column=0)  # Deuxième ligne, première colonne

fenetre.mainloop()
