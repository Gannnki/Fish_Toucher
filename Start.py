from gui_main import FishTouch
import sys
import os

# visit resource lib
def resource_path(relative_path):
    # check if Bundle Resource
    if getattr(sys, 'frozen', False):
        base_path = sys._MEIPASS
    else:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)

if __name__ == "__main__":
    path = resource_path("library")
    DaGongRen = FishTouch(path)
    DaGongRen.mainloop()