from tkinter import *
from definitions import *
from zipfile import ZipFile
import os


def initialize():
    ModListDisplayer.config(text=ModListDisplayer.cget("text")+mod_log("empty", "Initialization started..."))
    for i in os.listdir(mods_dir):
        if i.endswith(".zip"):
            ModListDisplayer.config(text=ModListDisplayer.cget("text")+mod_log("Detected",i))
    ModListDisplayer.config(text=ModListDisplayer.cget("text")+mod_log("empty", "Initialization completed."))

def load_everything():
    ModListDisplayer.config(text=ModListDisplayer.cget("text")+mod_log("empty", "Loading started..."))
    for i in os.listdir(mods_dir):
        if i.endswith(".zip"):
            mod_zip = ZipFile(f"{mods_dir}\{i}", "r")
            mod_zip.extractall(game_dir)
            mod_zip.close
            ModListDisplayer.config(text=ModListDisplayer.cget("text")+mod_log("Loaded",i))
    ModListDisplayer.config(text=ModListDisplayer.cget("text")+mod_log("empty", "Loading completed."))


MainWindow = Tk()
MainWindow.title("Brutal Squad Mod Loader")
MainWindow.geometry("640x480")
MainWindow.resizable(0,0)
MainWindowBackground = Canvas(MainWindow, width=640, height=480)
BackgroundImage = PhotoImage(file=f"{textures_dir}\loader_background.png")
#MainWindow.iconbitmap("Icon.ico")
ModListDisplayer = Label(MainWindowBackground, width=640, height=480, image=BackgroundImage, compound="center", fg="white", font=("Times",12))
MainWindowBackground.pack()

LoadButton = Button(MainWindow, bg="white", text="Load mods", command=lambda:load_everything())
MainWindowBackground.create_window((320,400), window=LoadButton)
MainWindowBackground.create_window((320,240), window=ModListDisplayer)

initialize()

MainWindowBackground.mainloop()
