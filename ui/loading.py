from tkinter import Label, Toplevel
import tkinter as tk


class LoadingScreen(Toplevel):
    def __init__(self, master):
        super().__init__(master)
        self.master = master

        self.title("Chargement...")

        self.label_introduction = Label(self, text="Transformation en cours...")
        self.label_introduction.grid(row=0, column=0, padx=10, pady=10)