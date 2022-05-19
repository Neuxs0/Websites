import turtle
from tkinter import *
gui = Tk()

gui.geometry("900x600")
gui.title("Game")

def patternselect():
    gui2 = Tk()

    gui2.geometry("200x600")
    gui2.title("Pattern Selecter")

    def pattern1():
        colors = ['red', 'blue', 'green', 'purple', 'black', 'pink']

        t = turtle.Turtle()
        t.speed(10000000000)

        for i in range(5000000000000000):
            t.pencolor(colors[i % 4])
            t.forward(i)
            t.left(91)

    B = Button(gui2, text="Spiral 1", command=pattern1)
    B.place(x=50, y=50)
    gui2.mainloop()

B = Button(gui, text="Sellect Pattern", command=patternselect)
B.place(x=50, y=50)
gui.mainloop()

