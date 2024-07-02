from tkinter import *
from tkinter import ttk
from listWords import words
import random

def text_captcha():
    ROOT = Tk()
    ROOT.geometry("500x400")

    fontSizes = [15,25,30,35]
    newWords = []
    correctIndex = 0
    for x in range(4):
        tempString = random.choice(words)
        words.remove(tempString)
        newWords.append(tempString)

        textSize = random.choice(fontSizes)
        fontSizes.remove(textSize)
        
        tempLabel = Label(ROOT, text=tempString, font=("Arial", textSize))
        tempLabel.pack(pady=7)
        if(textSize == 35):
            correctIndex = x

    label=Label(ROOT, text="Which word is the biggest?", font=("Arial 22 bold underline"))
    label.pack()

    inputLabel = Entry(ROOT, width=300, font=("Arial 22"),justify='center')
    inputLabel.focus_set()
    inputLabel.pack(pady=10)

    s = ttk.Style()
    s.configure("TButton", font=("Arial 20"))

    global tries
    tries = 0

    def submit_action():
        global tries 
        answer = inputLabel.get()
        if(answer.upper() == newWords[correctIndex].upper()):
            print("Successful")
            ROOT.destroy()
        else:
            print("Wrong. Try: " + str(tries + 1))
            tries += 1

        if(tries == 4):
            ROOT.destroy()
            text_captcha()

    ttk.Button(ROOT, text= "Submit", width= 20, style="TButton", command=submit_action).pack(pady=7)

    ROOT.mainloop()

def math_captcha():
    ROOT = Tk()
    ROOT.geometry("500x225")

    numbers = []
    for x in range(2):
        tempNum = random.randint(1, 100)
        numbers.append(tempNum)
    
    mathAnswer = numbers[0] + numbers[1]

    mathLabel = Label(ROOT, text=str(numbers[0]) + " + " + str(numbers[1]), font=("Arial", 30))
    mathLabel.pack(pady=7)

    label=Label(ROOT, text="What is the answer?", font=("Arial 22 bold underline"))
    label.pack()

    inputLabel = Entry(ROOT, width=300, font=("Arial 22"), justify='center')
    inputLabel.focus_set()
    inputLabel.pack(pady=10)

    s = ttk.Style()
    s.configure("TButton", font=("Arial 20"))

    global tries
    tries = 0

    def submit_action():
        global tries 
        answer = inputLabel.get()
        if(answer.isdigit() == False):
            answer = 0
           
        if(int(answer) == mathAnswer):
            print("Successful")
            ROOT.destroy()
        else:
            print("Wrong. Try: " + str(tries + 1))
            tries += 1

        if(tries == 4):
            ROOT.destroy()
            math_captcha()

    ttk.Button(ROOT, text= "Submit", width= 20, style="TButton", command=submit_action).pack(pady=7)

    ROOT.mainloop()
