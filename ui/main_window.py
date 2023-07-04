from tkinter import Tk, Button, Label, messagebox

class MainWindow(Tk):
    def __init__(self):
        """
        This is the main window of the app.
        """
        super().__init__()
        self.title("Word-2-Powerpoint")
        self.label_bienvenue = Label(text="Bienvenue aux GlaDéateurs!")
        self.label_bienvenue.grid(row=0, column=0, padx=10, pady=10)
        self.bouton_commencer = Button(text="Commencer", width=20, command=self.lancer_fenetre_introduction)
        self.bouton_commencer.grid(row=1, column=0, padx=10, pady=10)