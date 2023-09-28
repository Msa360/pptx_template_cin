from tkinter import Tk, Button, Label, Entry, filedialog
import tkinter as tk
import webbrowser
import os, sys
from ui.loading import StatusScreen

def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)



class MainWindow(Tk):
    def __init__(self):
        """
        This is the main window of the app.
        """
        super().__init__()

        self.title("Word-2-PDF")
        self.label_bienvenue = Label(text="Veuiller chosir un fichier word a transformer")
        self.label_bienvenue.grid(row=0, column=0, padx=10, pady=10)

        # input file
        self.btn_input_file = Button(text="Choisir un fichier", width=20, command=self.choose_input_file)
        self.btn_input_file.grid(row=1, column=0, padx=10, pady=10)

        self.file_entry_var = tk.StringVar()
        self.file_entry = Entry(self, width=30, textvariable=self.file_entry_var)
        self.file_entry.grid(row=2, column=0, padx=10, pady=0)

        # output file
        self.btn_output_file = Button(text="Choisir le dossier sortant", width=20, command=self.choose_output_dir)
        self.btn_output_file.grid(row=3, column=0, padx=10, pady=10)

        self.dir_entry_var = tk.StringVar()
        self.dir_entry = Entry(self, width=30, textvariable=self.dir_entry_var)
        self.dir_entry.grid(row=4, column=0, padx=10, pady=0)

        # font size
        self.label_bienvenue = Label(text="Veuiller chosir la taille de la police pour le titre et sous-titre")
        self.label_bienvenue.grid(row=5, column=0, padx=10, pady=10)

        self.title_size_var = tk.StringVar()
        self.title_size_var.set("24")
        self.title_size = Entry(self, width=30, textvariable=self.title_size_var)
        self.title_size.grid(row=6, column=0, padx=10, pady=0)

        self.subtitle_size_var = tk.StringVar()
        self.subtitle_size_var.set("10")
        self.subtitle_size = Entry(self, width=30, textvariable=self.subtitle_size_var)
        self.subtitle_size.grid(row=7, column=0, padx=10, pady=0)

        # image
        self.btn_img_file = Button(text="Choisir une image (optionnel)", width=20, command=self.choose_image_file)
        self.btn_img_file.grid(row=8, column=0, padx=10, pady=10)

        self.image_entry_var = tk.StringVar()
        self.image_entry = Entry(self, width=30, textvariable=self.image_entry_var)
        self.image_entry.grid(row=9, column=0, padx=10, pady=0)

        # start
        self.btn_make_document = Button(text="Go", width=20, command=self.make_document)
        self.btn_make_document.grid(row=10, column=0, padx=10, pady=10)

        # help
        self.help_link = Label(text="Aide", font=('Helveticabold', 15), fg="blue")
        self.help_link.grid(row=11, column=0, padx=10, pady=10)
        self.help_link.bind("<Button-1>", lambda e: webbrowser.open_new_tab("https://github.com/Msa360/word-2-pptx/blob/master/docs.md"))

    def choose_input_file(self):
        filename = filedialog.askopenfilename(parent=self)
        if filename != "":
            self.file_entry_var.set(filename)

    def choose_output_dir(self):
        dir = filedialog.askdirectory(parent=self, mustexist=True)
        if dir != "":
            self.dir_entry_var.set(dir)
    
    def choose_image_file(self):
        filename = filedialog.askopenfilename(parent=self)
        if filename != "":
            self.image_entry_var.set(filename)

    def make_output_file(self):
        output_file = os.path.join(self.dir_entry_var.get(), os.path.basename(self.file_entry_var.get()).rsplit(".", 1)[0]+".PDF")
        i = 1
        while os.path.exists(output_file):
            if i == 1:
                output_file = output_file[:-4] + str(i) + ".PDF"
            else:
                output_file = output_file[:-5] + str(i) + ".PDF"
            i += 1
        return output_file

    def make_document(self):
        # create a loading window
        # loading_screen = LoadingScreen(self)
        from datetime import datetime
        from word2pptx import transform
        try:
            transform(
                self.file_entry_var.get(),
                self.make_output_file(),
                datetime.now().strftime("%d-%m-%Y"),
                title_size=float(self.title_size_var.get()),
                subtitle_size=float(self.subtitle_size_var.get()),
                img_path=self.image_entry_var.get()
                )
        except Exception as e:
            loading_screen = StatusScreen(self, str(e))
        else:
            loading_screen = StatusScreen(self, "Succès!")
        self.wait_window(loading_screen)