from tkinter import *
import os


main_dir = os.path.dirname(os.path.abspath(__file__))
game_dir = (f"{os.path.abspath(os.path.join(main_dir, os.pardir))}\Brutal Squad")
presets_dir = (f"{main_dir}\presets")
mods_dir = (f"{main_dir}\mods")
data_dir = (f"{main_dir}\data")
textures_dir = (f"{data_dir}\\textures")


def mod_log(p_type: str="empty", to_print: str = ""):
    if p_type == "empty":
        return(to_print + "\n")
    else:
        return(f"{p_type}: {to_print}" + "\n")