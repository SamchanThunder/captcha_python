from tkinter import *
from tkinter import ttk
from PIL import ImageTk, Image
from listWords import words
from captcha.image import ImageCaptcha
import random

def rotate_captcha():
    ROOT = Tk()
    ROOT.geometry("500x450")

    label=Label(ROOT, text="Make the cupcake the closest direction to the arrow.", font=("Arial 15 bold"))
    label.pack()

    global answerDirection
    answerDirection = 0
    answer = random.randint(1,7)
    arrows = ['', '↖', '←', '↙', '↓', '↘', '→', '↗']
    answerText = arrows[answer]

    arrow_label = Label(ROOT, text=answerText, font=("Arial", 50, "bold"))
    arrow_label.pack()

    img = Image.open("./images/cake.png").resize((180,180))
    img_tk = ImageTk.PhotoImage(img)
    panel = Label(ROOT, image=img_tk)
    panel.image = img_tk  
    panel.pack()

    s = ttk.Style()
    s.configure("TButton", font=("Arial 15"))

    def turnRight():
        global answerDirection
        answerDirection = (answerDirection - 1) % 8
        rotated_img = img.rotate(answerDirection * 45).resize((180, 180))
        img_tk = ImageTk.PhotoImage(rotated_img)
        panel.config(image=img_tk)
        panel.image = img_tk
 
    def turnLeft():
        global answerDirection
        answerDirection = (answerDirection + 1) % 8
        rotated_img = img.rotate(answerDirection * 45).resize((180, 180))
        img_tk = ImageTk.PhotoImage(rotated_img)
        panel.config(image=img_tk)
        panel.image = img_tk
    
    global tries
    tries = 0
    def submit_action():
        global tries 
        if(answer == answerDirection):
            print("Successful")
            ROOT.destroy()
        else:
            print("Wrong. Try: " + str(tries + 1))
            tries += 1

        if(tries == 4):
            ROOT.destroy()
            rotate_captcha()

    ttk.Button(ROOT, text= "<", width= 5, style="TButton", command=turnLeft).pack(side="left", padx=50)
    ttk.Button(ROOT, text= ">", width= 5, style="TButton", command=turnRight).pack(side="right", padx=50)
    ttk.Button(ROOT, text= "Submit", width= 20, style="TButton", command=submit_action).pack(side="bottom", pady=60)

    ROOT.mainloop()


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
    ROOT.geometry("550x320")

    numbers = []
    for x in range(2):
        tempNum = random.randint(1, 100)
        numbers.append(tempNum)
    
    mathAnswer = numbers[0] + numbers[1]
    mathDisplay = str(numbers[0]) + "  " + str(numbers[1])

    image = ImageCaptcha(width = 300, height = 150)
    data = image.generate(mathDisplay)  
    image.write(mathDisplay, 'CAPTCHA.png')

    captcha_image = PhotoImage(file='CAPTCHA.png')
    image_label = Label(ROOT, image=captcha_image)
    image_label.pack()

    label=Label(ROOT, text="What is the sum of the two numbers?", font=("Arial 22 bold underline"))
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
