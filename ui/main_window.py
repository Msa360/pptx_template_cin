from tkinter import Tk, Button, Label, Entry, filedialog
import tkinter as tk
import webbrowser

from ui.loading import LoadingScreen

class MainWindow(Tk):
    def __init__(self):
        """
        This is the main window of the app.
        """
        super().__init__()
        self.title("Word-2-Powerpoint")
        self.label_bienvenue = Label(text="Veuiller chosir un fichier word a transformer")
        self.label_bienvenue.grid(row=0, column=0, padx=10, pady=10)

        self.btn_input_file = Button(text="Choisir un fichier", width=20, command=self.choose_input_file)
        self.btn_input_file.grid(row=1, column=0, padx=10, pady=10)

        self.file_entry_text = tk.StringVar()
        self.file_entry = Entry(self, width=30, textvariable=self.file_entry_text)
        self.file_entry.grid(row=2, column=0, padx=10, pady=0)

        self.btn_output_file = Button(text="Choisir le dossier sortant", width=20, command=self.choose_output_dir)
        self.btn_output_file.grid(row=3, column=0, padx=10, pady=10)

        self.dir_entry_text = tk.StringVar()
        self.dir_entry = Entry(self, width=30, textvariable=self.dir_entry_text)
        self.dir_entry.grid(row=4, column=0, padx=10, pady=0)

        self.btn_make_pptx = Button(text="Go", width=20, command=self.make_pptx)
        self.btn_make_pptx.grid(row=5, column=0, padx=10, pady=10)


        self.help_link = Label(text="Aide", font=('Helveticabold', 15), fg="blue", cursor="hand")
        self.help_link.grid(row=6, column=0, padx=10, pady=10)
        self.help_link.bind("<Button-1>", lambda e: webbrowser.open_new_tab("https://github.com/Msa360/pptx_template_cin/blob/master/docs.md"))

    def choose_input_file(self):
        f = filedialog.askopenfile(parent=self)
        if f is not None:
            self.input_filename = f.name
            self.input_file = f.read()
            f.close()
            self.file_entry_text.set(self.input_filename)

    def choose_output_dir(self):
        dir = filedialog.askdirectory(parent=self, mustexist=True)
        self.output_dir = dir
        self.dir_entry_text.set(self.output_dir)

    def make_pptx(self):
        # create a loading window
        loading_screen = LoadingScreen(self)
        # call pptx creator
        self.wait_window(loading_screen)