from tkinter import *
from pygame import mixer
import random
import numpy as np
import sys
input=sys.argv[1]

first_option=[]
second_option=[]
third_option=[]
fourth_option=[]
correct_answers=[]
mixer.init()
mixer.music.load('inspiring-action-epic-trailer-fantasy-SBA-346471683-preview.mp3')
mixer.music.play()
def select(event):
    b=event.widget
    value=b['text']

    for i in range(15):
        if value==correct_answers[i]:
            if value==correct_answers[14]:
                def close():
                    root2.destroy()
                    root.destroy()
                def playagain():
                    root2.destroy()
                    questionArea.delete(1.0, END)
                    questionArea.insert(END, questions[0])
                    optionButton1.config(text=first_option[0])
                    optionButton2.config(text=second_option[0])
                    optionButton3.config(text=third_option[0])
                    optionButton4.config(text=fourth_option[0])
                    amountLabel.config(image=amountimage)
                root2 = Toplevel()
                root2.overrideredirect(True)
                root2.config(bg='black')
                root2.geometry('800x600+140+30')
                root2.title('You won 0 pounds')
                imgLabel = Label(root2, image=centerImage, bd=0)
                imgLabel.pack(pady=30)

                WinLabel = Label(root2, text="Congratulations you have won 100 Bitcoins", font=('arial', 40, 'bold'), bg='black', fg='white')
                WinLabel.pack()

                playagainButton = Button(root2, text='Play Again', font=('arial', 20, 'bold'), bg='black', fg='white',
                                        activebackground='black', activeforeground='white', bd=0, cursor='hand2',
                                        command=playagain)
                playagainButton.pack()

                closeButton = Button(root2, text='Close', font=('arial', 20, 'bold'), bg='black', fg='white',
                                     activebackground='black', activeforeground='white', bd=0, cursor='hand2',
                                     command=close)
                closeButton.pack()

                root2.mainloop()
                break
            questionArea.delete(1.0,END)
            questionArea.insert(END,questions[i+1])

            optionButton1.config(text=first_option[i+1])
            optionButton2.config(text=second_option[i+1])
            optionButton3.config(text=third_option[i+1])
            optionButton4.config(text=fourth_option[i+1])
            amountLabel.config(image=amountimages[i])

        if value not in correct_answers:

            def close():
                root1.destroy()
                root.destroy()

            def tryagain():
                root1.destroy()
                questionArea.delete(1.0,END)
                questionArea.insert(END,questions[0])
                optionButton1.config(text=first_option[0])
                optionButton2.config(text=second_option[0])
                optionButton3.config(text=third_option[0])
                optionButton4.config(text=fourth_option[0])
                amountLabel.config(image=amountimage)



            root1=Toplevel()
            root1.overrideredirect(True)
            root1.config(bg='black')
            root1.geometry('800x600+140+30')
            root1.title('You won 0 pounds')
            imgLabel=Label(root1,image=centerImage,bd=0)
            imgLabel.pack(pady=30)

            loseLabel=Label(root1,text="You lose",font=('arial',40,'bold'),bg='black',fg='white')
            loseLabel.pack()

            tryagainButton=Button(root1,text='Try Again',font=('arial',20,'bold'),bg='black',fg='white',activebackground='black',activeforeground='white',bd=0,cursor='hand2',command=tryagain)
            tryagainButton.pack()

            closeButton = Button(root1, text='Close', font=('arial', 20, 'bold'), bg='black', fg='white',
                                    activebackground='black', activeforeground='white', bd=0, cursor='hand2',command=close)
            closeButton.pack()

            root1.mainloop()
            break

# This is where our prediction happens
initial_prices = [200, 220, 245, 134, 456, 321, 346, 567, 654, 896,899,123,145,897,378]
def predict_stock_prices():
    def generate_price(previous_price):
        change_percentage = random.uniform(-0.05, 0.05)
        price = previous_price * (1 + change_percentage)
        return price

    initial_prices = [200, 220, 245, 134, 456, 321, 346, 567, 654, 896,899,123,145,897,378]
    def simulate_market(initial_price, days):
        price = initial_price
        price_history = [price]
        for i in range(days):
            price = generate_price(price)
            price_history.append(price)
        return price_history

    def predict_future_price(price_history, days_to_predict):
        highest_price = max(price_history)
        lowest_price = min(price_history)
        current_price = price_history[-1]
        if current_price == highest_price:
            change_percentage = random.uniform(-0.05, 0)
        elif current_price == lowest_price:
            change_percentage = random.uniform(0, 0.05)
        elif current_price == (highest_price+lowest_price)/2:
            change_percentage= random.uniform(-0.75,0.75)
        else:
            change_percentage = random.uniform(-0.05, 0.05)
        predicted_price = current_price * (1 + change_percentage)
        for i in range(days_to_predict - 1):
            predicted_price = generate_price(predicted_price)
            predicted_price=round(predicted_price,2)
        return predicted_price

    simulation_days = 23
    prediction_days = 30
    predicted_prices = []
    for initial_price in initial_prices:
        price_history = simulate_market(initial_price, simulation_days)
        predicted_price = predict_future_price(price_history, prediction_days)
        predicted_prices.append(predicted_price)
    predicted_prices_array = np.array(predicted_prices)
    return predicted_prices_array

results = predict_stock_prices()


questions = ["Predict the stock price of which is currently 200 rupees in 30 days",
             "Predict the stock price of banana which is currently 220 rupees in 30 days",
             "Predict the stock price of meat which is currently 245 rupees in 30 days",
             "Predict the stock price of copy which is currently 134 rupees in 30 days",
             "Predict the stock price of pen which is currently 456 rupees in 30 days",
             "Predict the stock price of chair which is currently 321 rupees in 30 days",
             "Predict the stock price of bag which is currently 346 rupees in 30 days",
             "Predict the stock price of cement which is currently 567 rupees in 30 days",
             "Predict the stock price of metal which is currently 654 rupees in 30 days",
             "Predict the stock price of toys which is currently 896 rupees in 30 days",
             "Predict the stock price of Air conditioner which is currently 899 rupees in 30 days",
             "Predict the stock price of Chain which is currently 123 rupees in 30 days",
             "Predict the stock price of Hankey which is currently 145 rupees in 30 days",
             "Predict the stock price of Wood which is currently 897 rupees in 30 days",
             "Predict the stock price of Paint which is currently 378 rupees in 30 days"]

for i in range(15):
    randomIndex = random.randint(0, 3)
    if (randomIndex == 0):
        first_option.append(results[i])
        second_option.append(round(random.uniform(0.00, 1000.00), 2))
        third_option.append(round(random.uniform(0.00, 1000.00), 2))
        fourth_option.append(round(random.uniform(0.00, 1000.00), 2))
    elif (randomIndex == 1):
        first_option.append(round(random.uniform(0.00, 1000.00), 2))
        second_option.append(results[i])
        third_option.append(round(random.uniform(0.00, 1000.00), 2))
        fourth_option.append(round(random.uniform(0.00, 1000.00), 2))
    elif (randomIndex == 2):
        first_option.append(round(random.uniform(0.00, 1000.00), 2))
        second_option.append(round(random.uniform(0.00, 1000.00), 2))
        third_option.append(results[i])
        fourth_option.append(round(random.uniform(0.00, 1000.00), 2))
    elif (randomIndex == 3):
        first_option.append(round(random.uniform(0.00, 1000.00), 2))
        second_option.append(round(random.uniform(0.00, 1000.00), 2))
        third_option.append(round(random.uniform(0.00, 1000.00), 2))
        fourth_option.append(results[i])

    correct_answers.append(results[i])


root=Tk()
root.overrideredirect(True)
root.geometry('1920x1080+0+0')
root.title('A NEW LEASE')
root.config(bg='black')

leftframe=Frame(root,bg='black')
leftframe.grid()

topFrame=Frame(leftframe,bg='black',pady=15)
topFrame.grid()

centerFrame = Frame(leftframe,bg='black',pady=15)
centerFrame.grid(row=1,column=0)

bottomFrame=Frame(leftframe,bg='black')
bottomFrame.grid(row=2,column=0)

rightframe=Frame(root,bg='black',pady=25,padx=50)
rightframe.grid(row=0,column=1)
imageanewlease=PhotoImage(file='WhatsApp Image 2023-02-17 at 10.10.41 PM.png')

anewleaselable=Label(topFrame,image=imageanewlease,bg='black')
anewleaselable.grid(row=0,column=0)

centerImage=PhotoImage(file='WhatsApp Image 2023-02-16 at 9.40.26 PM.png')

logoLabel=Label(centerFrame,image=centerImage,bg='black')
logoLabel.grid(row=0,column=0)

amountimage=PhotoImage(file='Picture0.png')
amountimage1=PhotoImage(file='Picture1.png')
amountimage2=PhotoImage(file='Picture2.png')
amountimage3=PhotoImage(file='Picture3.png')
amountimage4=PhotoImage(file='Picture4.png')
amountimage5=PhotoImage(file='Picture5.png')
amountimage6=PhotoImage(file='Picture6.png')
amountimage7=PhotoImage(file='Picture7.png')
amountimage8=PhotoImage(file='Picture8.png')
amountimage9=PhotoImage(file='Picture9.png')
amountimage10=PhotoImage(file='Picture10.png')
amountimage11=PhotoImage(file='Picture11.png')
amountimage12=PhotoImage(file='Picture12.png')
amountimage13=PhotoImage(file='Picture13.png')
amountimage14=PhotoImage(file='Picture14.png')
amountimage15=PhotoImage(file='Picture15.png')

amountimages = [amountimage1, amountimage2, amountimage3, amountimage4, amountimage5, amountimage6, amountimage7, amountimage8, amountimage9, amountimage10, amountimage11, amountimage12, amountimage13
    , amountimage14, amountimage15]




amountLabel=Label(rightframe,image=amountimage,bg='black')
amountLabel.grid(row=0,column=0)

layoutImage=PhotoImage(file='lay (1).png')

LayoutLabel=Label(bottomFrame,image=layoutImage,bg='black')
LayoutLabel.grid(row=0,column=0)

questionArea=Text(bottomFrame,font=('arial',16,'bold'),width=34,height=2,wrap='word',bg='black',fg='white',bd=0)
questionArea.place(x=70,y=15)

questionArea.insert(END,questions[0])

LabelA=Label(bottomFrame,text='A:',bg='black',fg='white',font=('arial',16,'bold'))
LabelA.place(x=60,y=110)

optionButton1=Button(bottomFrame,text=first_option[0],font=('arial',18,'bold'),bg='black',fg='white',bd=0,activebackground='black',activeforeground='white',cursor='hand2')
optionButton1.place(x=100,y=100)

LabelB=Label(bottomFrame,text='B:',bg='black',fg='white',font=('arial',16,'bold'))
LabelB.place(x=330,y=110)

optionButton2=Button(bottomFrame,text=second_option[0],font=('arial',18,'bold'),bg='black',fg='white',bd=0,activebackground='black',activeforeground='white',cursor='hand2')
optionButton2.place(x=370,y=100)

LabelC=Label(bottomFrame,text='C:',bg='black',fg='white',font=('arial',16,'bold'))
LabelC.place(x=60,y=190)

optionButton3=Button(bottomFrame,text=third_option[0],font=('arial',18,'bold'),bg='black',fg='white',bd=0,activebackground='black',activeforeground='white',cursor='hand2')
optionButton3.place(x=100,y=180)

LabelD=Label(bottomFrame,text='D:',bg='black',fg='white',font=('arial',16,'bold'))
LabelD.place(x=330,y=190)

optionButton4=Button(bottomFrame,text=fourth_option[0],font=('arial',18,'bold'),bg='black',fg='white',bd=0,activebackground='black',activeforeground='white',cursor='hand2')
optionButton4.place(x=370,y=180)

optionButton1.bind('<Button>',select)
optionButton2.bind('<Button>',select)
optionButton3.bind('<Button>',select)
optionButton4.bind('<Button>',select)

root.mainloop()
print(input)