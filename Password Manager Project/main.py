from tkinter import *
# --- COLORS ---
BG_COLOR = "#F5F5DC"
BTN_GEN_COLOR = "#FBC02D"
BTN_ADD_COLOR = "#C62828"
TEXT_COLOR = "#333333"

# --- UI SETUP ---
window = Tk()
window.title("MyPass Manager")
window.config(padx=50, pady=50, bg=BG_COLOR)

canvas = Canvas(width=200, height=200, bg=BG_COLOR, highlightthickness=0)
lock_image = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=lock_image)
canvas.grid(row=0, column=1)

# Labels
website_label = Label(text="Website:", bg=BG_COLOR, fg=TEXT_COLOR)
website_label.grid(row=1, column=0)
