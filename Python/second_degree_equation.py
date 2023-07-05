import math
import tkinter as tk
from tkinter import *
from number_entry import IntEntry

def main():
    try:
        
        a = float(input("What is the value(a): "))
        b = float(input("What is the value(b): "))
        c = float(input("What is the value(c): "))

        dis = discriminant(b, a, c)
        x_value = X_value(dis, b, a)

        text_result["text"] = f"{x_value: .1f}"
      

    except (FileNotFoundError, PermissionError) as error:
        print(type(error).__name__, error, sep=": ")

def discriminant(b, a, c):
    discriminant = (b**2) - (4 * a * c)
    return discriminant

def X_value(discriminant, b, a):

    x = (- b + discriminant ** (1/2)) / (2 * a)
  
    #x = (- b - discriminant ** (1/2)) / (2 * a)
    return x

equation = Tk()

# Muda o titulo do programa por isso usamos o title.
equation.title("Second degree equation")

tk.Label(equation, text="What is the value(a): ").grid(row=1)
tk.Label(equation, text="What is the value(b): ").grid(row=2)
tk.Label(equation, text="What is the value(c): ").grid(row=3)
e1 = tk.Entry(equation)
e2 = tk.Entry(equation)
e3 = tk.Entry(equation)

e1.grid(row=1, column=1)
e2.grid(row=2, column=1)
e3.grid(row=3, column=1)

# Coloca texto na Janela por isso usamos o Label
text_orientation = Label(equation, text="Calculate the second degree equation")

# Escolher a posição do texto usamos o grid e depois dizemos qual é a coluna e a linha.
text_orientation.grid(column=0, row=0, padx=10, pady=10) #se querermos colocar um outro texto abaixo do primeiro é so mudar o numero de linha e deixar a coluna igual do primeiro.

# Quando queremos adicionar um botão precisamos chamar o Button e dizer em qual tela ou janela ela esta, também devemos colocar no botão o que as pessoas devem fazer então para isso usamos o (Command=) e diz para ele o nome de uma função sem parenteses.
botão = Button(equation, text="Calculate", command= main)

# Quando criamos o botão devemos dizer em que coluna e linha deve estar ou seja deve estar dentro do grid.
botão.grid(column=1, row=4, padx=10, pady=10) # Para dar espaço nos elementos usamos (padx e pady) que significa pading

# Onde vai aparecer as cotações
text_result = Label(equation, text="Result is:")

# Usamos o grid também para indicar onde estará.
text_result.grid(column=0, row=5, padx=10, pady=10)


equation.mainloop()

