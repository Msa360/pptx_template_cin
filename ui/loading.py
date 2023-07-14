from tkinter import Label, Toplevel
import tkinter as tk


class StatusScreen(Toplevel):
    def __init__(self, master, message: str):
        super().__init__(master)
        self.master = master

        self.title("Status de la transformation")

        self.label_introduction = Label(self, text=message)
        self.label_introduction.grid(row=0, column=0, padx=10, pady=10)