import math
import tkinter as tk
from tkinter import *
from datetime import datetime


current_date_and_time = datetime.now()


def main():
       
    
    try:
        a=float(aentry.get())
        b=float(bentry.get())
        c=float(centry.get())
        # Calls the discriminant, X_value1 and X_value2
        dis = discriminant(b, a, c)
        x_value1 = X_value1(dis, b, a)
        x_value2 = X_value2(dis, b, a)
        total1=(x_value1)
        total2=(x_value2)
        Label(text=f"{dis: .0f}", font="arial 15 bold").place(x=250, y=170)
        Label(text=f"{total1: .1f}", font="arial 15 bold").place(x=250, y=210)
        Label(text=f"{total2: .1f}", font="arial 15 bold").place(x=250, y=250)

    


    except (FileNotFoundError, PermissionError) as error:
        print(type(error).__name__, error, sep=": ")
        print()
    print(current_date_and_time)

# calculate the discriminant
def discriminant(b, a, c):
    discrimi = (b**2) - (4 * a * c)
    return discrimi

# calculate the value of X_value1
def X_value1(discrimi, b, a):
    x1 = (- b + (discrimi ** 0.5)) / (2 * a)
    
    return x1

# calculate the value of X_value2
def X_value2(discrimi, b, a):
    x2 = (- b - (discrimi ** 0.5)) / (2 * a)

    return x2


equation = Tk()

# Muda o titulo do programa por isso usamos o title.
equation.title("Second degree equation")
equation.geometry("500x400")

a = Label(equation, text="What is the value(a): ", font="arial 10")
b = Label(equation, text="What is the value(b): ", font="arial 10")
c = Label(equation, text="What is the value(c): ", font="arial 10")
dis = Label(equation, text="total_discriminant: ", font="arial 10")
total1 = Label(equation, text="total_X_value1: ", font="arial 10")
total2 = Label(equation, text="total_X_value2: ", font="arial 10")

a.place(x=50, y=20)
b.place(x=50, y=70)
c.place(x=50, y=120)
dis.place(x=50, y=170)
total1.place(x=50, y=210)
total2.place(x=50, y=250)

avalue=StringVar()
bvalue=StringVar()
cvalue=StringVar()

aentry =Entry(equation, textvariable=avalue, font="arial 15", width=15)
bentry =Entry(equation, textvariable=bvalue, font="arial 15", width=15)
centry =Entry(equation, textvariable=cvalue, font="arial 15", width=15)

#Coloca as barras onde voce coloca os numeros.
aentry.place(x=250, y=20) 
bentry.place(x=250, y=70)
centry.place(x=250, y=120)

#Colocar botão de calcular e sair
Button(text="Calculate", font="arial 15", bg="white",bd=10, command=main).place(x=50, y=300)
Button(text="Exit", font="arial 15", bg="white",bd=10,  width=8, command=lambda:exit()).place(x=350, y=300)


equation.mainloop()