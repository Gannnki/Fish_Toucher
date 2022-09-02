# -*- encoding: utf-8 -*-
import threading
import tkinter as tk
from tkinter import messagebox
from main import random_mouse
from config_thread import stop_thread

class FishTouch(tk.Tk):

    def __init__(self, path):
        super().__init__()

        # Geometry parameter setting
        self.dir = path
        self.original_width = 250
        self.original_height = 200
        self.title("Fish Toucher")
        self.iconbitmap(str(self.dir + "\\fish.ico"))

        self.text_motivation =tk.Label(self, text="In me the tiger sniffs the rose." + "\n" + "心有猛虎，细嗅蔷薇")
        self.text_motivation.grid(row=0, rowspan=3, column=0,columnspan=3)

        self.photo = tk.PhotoImage(file=self.dir + "\\fishtouching.gif")
        self.imgphoto = tk.Label(self, image=self.photo, anchor="center")

        self.init_window()
        self.create_button()

    def init_window(self):
        self.geometry('{}x{}'.format(self.original_width, self.original_height))
        self.resizable(0,0)
        self.imgphoto.grid(row=3, rowspan=1, column=0, columnspan=3, padx =10, pady = 10)

    def create_button(self):
        self.bt_freedom = tk.Button(text="Begin Fish Touching", command=self.begin_freedom)
        self.bt_freedom.grid(row=6, rowspan=1, column=0, padx = 10)
        self.bt_work = tk.Button(text="Back to Work!", command=self.back_to_work)
        self.bt_work.grid(row=6, rowspan=1, column=2, padx = 10)

    def begin_freedom(self):
        self.t = threading.Thread(target=random_mouse, args=(), daemon=True)
        self.t.start()


    def back_to_work(self):
        if 1:
            stop_thread(self.t)
            answer = messagebox.askyesno(title='confirmation',
                    message='Are you sure you want to go back to work?')
            if answer:
                self.destroy()