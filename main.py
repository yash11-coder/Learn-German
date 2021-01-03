from tkinter import *
import random
import pandas

try:
    data = pandas.read_csv("data/words_to_learn.csv")
except FileNotFoundError:
    data = pandas.read_csv("data/german_words.csv")
finally:
    to_learn = data.to_dict(orient="records")

word={}


BACKGROUND_COLOR ="#B1DDC6"
#--------------------------------------------------------------------------------------------#
def generate():
    global word, flip_timer
    window.after_cancel(flip_timer)
    word = random.choice(to_learn)
    canvas.itemconfig(card_background, image=old_image)
    canvas.itemconfig(card_title, text="German", fill="black")
    canvas.itemconfig(card_word, text=word["German"], fill="black")
    flip_timer = window.after(3000, func=flip_card)



def flip_card():
    canvas.itemconfig(card_background, image=new_image)
    canvas.itemconfig(card_title, text="English", fill="white")
    canvas.itemconfig(card_word, text=word["English"], fill="white")

def is_known():
    to_learn.remove(word)
    print(len(to_learn))
    data = pandas.DataFrame(to_learn)
    data.to_csv("data/words_to_learn.csv", index=False)
    generate()










#--------------------------------------------------------------------------------------------#


window = Tk()
window.title("Flash Card")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

flip_timer = window.after(3000, func=flip_card)


canvas = Canvas(width=800, height=526)
old_image = PhotoImage(file="images/card_front.png")
new_image = PhotoImage(file="images/card_back.png")
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
card_background = canvas.create_image(400, 263, image=old_image)
card_title = canvas.create_text(400, 150, text="Title", font=("Ariel", 40, "italic"))
card_word = canvas.create_text(400, 263, text="word", font=("Ariel", 60, "bold"))
canvas.grid(column=0, row=0, columnspan=2)


right_img = PhotoImage(file="images/right.png")
right_button = Button(image=right_img, highlightthickness=0, command=is_known)
right_button.grid(column=1, row=1)

wrong_img = PhotoImage(file="images/wrong.png")
wrong_button = Button(image=wrong_img, highlightthickness=0, command=generate)
wrong_button.grid(column=0, row=1)




generate()

















window.mainloop()
