
import tkinter
from tkinter import *


root = Tk()
root.title("Grade calculator")
root.geometry("500x400")

def Calculation():
    english=int(englishentry.get())
    skill=int(anlytical_skillentry.get())
    general=int(generalentry.get())
    total=(english+skill+general)
    Label(text=f"{total}", font="arial 15 bold").place(x=250, y=170)
    
    average=int(total/3)
    Label(text=f"{average}", font="arial 15 bold").place(x=250, y=210)
    if (average>50):
        grade = "pass"
    else:
        grade = "Fail"

    Label(text=f"{grade}", font="arial 15 bold", fg="blue").place(x=250, y=250)



#coloca os nome que irão aparecer na janela
sub1 = Label(root, text="English: ", font="arial 10")
sub2 = Label(root, text="Analytical: ", font="arial 10")
sub3 = Label(root, text="General knowledge: ", font="arial 10")
total = Label(root, text="total: ", font="arial 10")
avg = Label(root, text="Average: ", font="arial 10")
grade = Label(root, text="Grade: ", font="arial 10")

sub1.place(x=50, y=20)
sub2.place(x=50, y=70)
sub3.place(x=50, y=120)
total.place(x=50, y=170)
avg.place(x=50, y=210)
grade.place(x=50, y=250)

englishvalue=StringVar()
anlytical_skillvalue=StringVar()
generalvalue=StringVar()

englishentry =Entry(root, textvariable=englishvalue, font="arial 15", width=15)
anlytical_skillentry =Entry(root, textvariable=anlytical_skillvalue, font="arial 15", width=15)
generalentry =Entry(root, textvariable=generalvalue, font="arial 15", width=15)

#Coloca as barras onde voce coloca os numeros.
englishentry.place(x=250, y=20) 
anlytical_skillentry.place(x=250, y=70)
generalentry.place(x=250, y=120)

#Colocar botão de calcular e sair
Button(text="Calculate", font="arial 15", bg="white",bd=10, command=Calculation).place(x=50, y=300)
Button(text="Exit", font="arial 15", bg="white",bd=10,  width=8, command=lambda:exit()).place(x=350, y=300)
root.mainloop()