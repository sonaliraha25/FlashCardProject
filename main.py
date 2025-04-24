from tkinter import *
import pandas
import random
BACKGROUND_COLOR = "#B1DDC6"
window=Tk()
window.config(padx=50,pady=50,bg=BACKGROUND_COLOR)
window.title('Flashy')

data=pandas.read_csv("data/french_words.csv")
to_learn=data.to_dict(orient="records")
current_card={}
def next_card():
    global current_card
    current_card=random.choice(to_learn)
    canvas.itemconfig(card_title,text="French")
    canvas.itemconfig(card_word,text=current_card['French'])
    window.after(3000, func=flip_card)
def flip_card():
    canvas.itemconfig(card_title, text="English")
    canvas.itemconfig(card_word, text=current_card['English'])
    back_card = PhotoImage(file="images/card_back.png")
    canvas.itemconfig(card_background, image=back_card)
    window.after(3000, func=next_card)
def is_known():
   to_learn.remove(current_card)
   recent_data=pandas.DataFrame(to_learn)
   recent_data.to_csv('data/to_learn_file.csv',index=False)
   next_card()

front_card=PhotoImage(file="images/card_front.png")
canvas=Canvas(height=500,width=526,bg=BACKGROUND_COLOR)
card_background=canvas.create_image(400,263,image=front_card)
canvas.config(highlightthickness=0,bg=BACKGROUND_COLOR)
canvas.grid(row=0,column=0,columnspan=2 )
card_title=canvas.create_text(250,100,font=("Arial", 40))
card_word=canvas.create_text(250,263,font=("Arial", 40))
right_button_img=PhotoImage(file="images/right.png")
wrong_button_img=PhotoImage(file="images/wrong.png")
right_button=Button(command=is_known,image=right_button_img,highlightthickness=0,bg=BACKGROUND_COLOR)
right_button.grid(row=1,column=0)
wrong_button=Button(command=flip_card,image=wrong_button_img,highlightthickness=0,bg=BACKGROUND_COLOR)
wrong_button.grid(row=1,column=1)
next_card()

window.mainloop()
