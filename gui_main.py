import tkinter as tk
from tkinter import messagebox
import time
import random
import pyautogui

# TODO: Threading with exit button

class FishTouch(tk.Tk):

    def __init__(self):
        super().__init__()

        # Geometry parameter setting
        self.original_width = 220
        self.original_height = 180
        self.title("摸鱼王")
        self.iconbitmap("fish.ico")

        self.text_motivation =tk.Label(self, text="Good Good Study, day day up.")
        self.text_motivation.grid(row=0, rowspan=3, column=0,columnspan=4)

        self.photo = tk.PhotoImage(file="fishtouching.gif")
        self.imgphoto = tk.Label(self, image=self.photo)

        self.init_window()
        self.create_button()


    def init_window(self):
        self.geometry('{}x{}'.format(self.original_width, self.original_height))
        self.imgphoto.grid(row=3, rowspan=1, column=0)

    def create_button(self):
        self.bt_freedom = tk.Button(text="Begin Fish Touching", command=self.begin_freedom)
        self.bt_freedom.grid(row=4, rowspan=1, column=0)
        self.bt_work = tk.Button(text="Back to Work!", command=self.back_to_work)
        self.bt_work.grid(row=4, rowspan=1, column=2)


    def begin_freedom(self):
        while 1:
            time.sleep(2)
            pyautogui.moveTo(x=1400, y=random.randint(100, 700))
            pyautogui.click()

    def back_to_work(self):
        if 1:
            answer = messagebox.askyesno(title='confirmation',
                    message='Are you sure you want to go back to work?')
            if answer:
                self.destroy()


if __name__ == "__main__":
    DaGongRen = FishTouch()
    DaGongRen.mainloop()
