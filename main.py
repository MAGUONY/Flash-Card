from tkinter import *
import pandas
import random

BACKGROUND_COLOR = "#B1DDC6"

currentWord = {}
theData = {}

try:
    theDataFrame = pandas.read_csv("data/wordsToLearn.csv")

except FileNotFoundError:
    originalData = pandas.read_csv("data/french_words.csv")
    theData = originalData.to_dict(orient="records")

else:
    theData = theDataFrame.to_dict(orient="records")


def randomFrenchWord():
    global currentWord, flipTimer
    window.after_cancel(flipTimer)
    currentWord = random.choice(theData)
    theCanvas.itemconfig(theImage, image=cardFront)
    theCanvas.itemconfig(theWord, fill="black", text=currentWord["French"])
    theCanvas.itemconfig(theLanguage, fill="black", text="French")
    window.after(3000, func=flipCard)


def flipCard():
    theCanvas.itemconfig(theImage, image=cardBack)
    theCanvas.itemconfig(theWord, fill="white", text=currentWord["English"])
    theCanvas.itemconfig(theLanguage, fill="white", text="English")


def knowWord():
    theData.remove(currentWord)
    data = pandas.DataFrame(theData)
    data.to_csv("data/wordsToLearn.csv", index=False)
    randomFrenchWord()


window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

flipTimer = window.after(3000, func=flipCard)


# -----------------------------------------------UI SETUP--------------------------------------------------------------
# Canvas and pictures setup
theCanvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)

cardFront = PhotoImage(file="images/card_front.png")
cardBack = PhotoImage(file="images/card_back.png")
wrongImage = PhotoImage(file="images/wrong.png")
rightImage = PhotoImage(file="images/right.png")

theImage = theCanvas.create_image(410, 270, image=cardFront)
theLanguage = theCanvas.create_text(400, 150, text="Title", fill="black", font=("Ariel", 40, "italic"))
theWord = theCanvas.create_text(400, 263, text="Word", fill="black", font=("Ariel", 60, "bold"))

theCanvas.grid(column=0, row=0, columnspan=2)

# Buttons
wrongButton = Button(image=wrongImage, highlightthickness=0, command=randomFrenchWord)
wrongButton.grid(column=0, row=1)

rightButton = Button(image=rightImage, highlightthickness=0, command=knowWord)
rightButton.grid(column=1, row=1)

randomFrenchWord()


window.mainloop()

