from tkinter import *
import pandas
import random








def flip_card():
    canvas.itemconfig(card_title, text="English", fill="white")






window = Tk()
window.title("Flash-Card")

window.config(padx=20, pady=20, bg=BACKGROUND_COLOR)
canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
card_front_img = PhotoImage(file="images/card_front.png")
card_back_img = PhotoImage(file="images/card_back.png")
card_background = canvas.create_image(400, 263, image=card_front_img)
card_title = canvas.create_text(400, 150, text="", font=("Ariel", 40, "italic"))
card_word = canvas.create_text(400, 263, text="", font=("Ariel", 60, "bold"))
canvas.grid(row=0, column=0, columnspan=2)
cross_image = PhotoImage(file="images/wrong.png")
unknown_button = Button(image=cross_image, highlightthickness=0, borderwidth=0, bg=BACKGROUND_COLOR, command=next_card)
unknown_button.grid(row=1, column=0, pady=(20, 20))

check_image = PhotoImage(file="images/right.png")
known_button = Button(image=check_image, highlightthickness=0, borderwidth=0, bg=BACKGROUND_COLOR, command=is_known)
known_button.grid(row=1, column=1, pady=(20, 20))

window.mainloop()
