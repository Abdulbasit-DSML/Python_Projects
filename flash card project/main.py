from tkinter import *
import pandas
import random















window = Tk()
window.title("Flash-Card")

window.config(padx=20, pady=20, bg=BACKGROUND_COLOR)
canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
card_front_img = PhotoImage(file="images/card_front.png")
