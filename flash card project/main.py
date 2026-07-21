from tkinter import *
import pandas
import random















window = Tk()
window.title("Flash-Card")

window.config(padx=20, pady=20, bg=BACKGROUND_COLOR)
canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
card_front_img = PhotoImage(file="images/card_front.png")
card_back_img = PhotoImage(file="images/card_back.png")
card_background = canvas.create_image(400, 263, image=card_front_img)
