from tkinter import *
from tkinter import messagebox

print("hello world");
print("hello world");
print("hello world");
print("hello world");


root = Tk()
root.title("Simple Calculator")
root.geometry("350x300")
root.resizeable(0,0)
root.configure(bg="#77526b")
equa = ""
equation = StringVar()
Calculation = Label(root, textvariable=equation, bg="#77526b", fg="#e6a4ff", font="Tahoma", justify=CENTER)
equation.set("Enter your expression")
Calculation.grid(columnspan=4)


def buttonPress(number):
    global equa
    equa = equa + str(number)
    equation.set(equa)


def equalButtonPress():
    try:
        member = 0
        global equa
        total = str(eval(equa))
        for char in total:
            member += 1
        if member > 20:
            raise ValueError
        equation.set(total)
        equa = ""
    except ZeroDivisionError:
        messagebox.showwarning(title="Mathematic error", message="Division by Zero")
    except ValueError:
        messagebox.showerror(title="value Error", message="Too Big Number!")
    except:
        messagebox.showerror(title="Syntax error", message="an error occurd please try again")


def clearButtonPress():
    global equa
    equa = ""
    equation.set("")


btn0 = Button(root, text="0", width=7, height=2, command=lambda: buttonPress(0), padx=2, pady=2, relief=RAISED,
              bg="#e0b34a", font="Tahoma")
btn0.grid(row=4, column=1)

btn1 = Button(root, text="1", width=7, height=2, command=lambda: buttonPress(1), padx=2, pady=2, relief=RAISED,
              font="Tahoma", bg="#e0b34a")
btn1.grid(row=1, column=0)

btn2 = Button(root, text="2", width=7, height=2, command=lambda: buttonPress(2), padx=2, pady=2, relief=RAISED,
              font="Tahoma", bg="#e0b34a")
btn2.grid(row=1, column=1)

btn3 = Button(root, text="3", width=7, height=2, command=lambda: buttonPress(3), padx=2, pady=2, relief=RAISED,
              font="Tahoma", bg="#e0b34a")
btn3.grid(row=1, column=2)

btn4 = Button(root, text="4", width=7, height=2, command=lambda: buttonPress(4), padx=2, pady=2, relief=RAISED,
              font="Tahoma", bg="#e0b34a")
btn4.grid(row=2, column=0)

btn5 = Button(root, text="5", width=7, height=2, command=lambda: buttonPress(5), padx=2, pady=2, relief=RAISED,
              font="Tahoma", bg="#e0b34a")
btn5.grid(row=2, column=1)

btn6 = Button(root, text="6", width=7, height=2, command=lambda: buttonPress(6), padx=2, pady=2, relief=RAISED,
              font="Tahoma", bg="#e0b34a")
btn6.grid(row=2, column=2)

btn7 = Button(root, text="7", width=7, height=2, command=lambda: buttonPress(7), padx=2, pady=2, relief=RAISED,
              font="Tahoma", bg="#e0b34a")
btn7.grid(row=3, column=0)

btn8 = Button(root, text="8", width=7, height=2, command=lambda: buttonPress(8), padx=2, pady=2, relief=RAISED,
              font="Tahoma", bg="#e0b34a")
btn8.grid(row=3, column=1)

btn9 = Button(root, text="9", width=7, height=2, command=lambda: buttonPress(9), padx=2, pady=2, relief=RAISED,
              font="Tahoma", bg="#e0b34a")
btn9.grid(row=3, column=2)

plus = Button(root, text="+", width=7, height=2, command=lambda: buttonPress('+'), padx=2, pady=2, relief=RAISED,
              font="Tahoma", bg="#e0b34a")
plus.grid(row=1, column=3)

minus = Button(root, text="-", width=7, height=2, command=lambda: buttonPress('-'), padx=2, pady=2, relief=RAISED,
               font="Tahoma", bg="#e0b34a")
minus.grid(row=2, column=3)

multiply = Button(root, text="×", width=7, height=2, command=lambda: buttonPress('*'), padx=2, pady=2, relief=RAISED,
                  font="Tahoma", bg="#e0b34a")
multiply.grid(row=3, column=3)

divide = Button(root, text="÷", width=7, height=2, command=lambda: buttonPress('/'), padx=2, pady=2, relief=RAISED,
                font="Tahoma", bg="#e0b34a")
divide.grid(row=4, column=3)

equal = Button(root, text="=", width=7, height=2, command=equalButtonPress, padx=2, pady=2, relief=RAISED,
               font="Tahoma", bg="#e0b34a")
equal.grid(row=4, column=2)

clear = Button(root, text="c", width=7, height=2, command=clearButtonPress, padx=2, pady=2, relief=RAISED,
               font="Tahoma", bg="#e0b34a")
clear.grid(row=4, column=0)

root.mainloop()
