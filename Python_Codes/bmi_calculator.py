from cgitb import text
from email import message
from importlib.metadata import EntryPoint
from tkinter import *
from tkinter import messagebox

tk = Tk()

tk.title("BMI Calculator")
tk.geometry("1000x500")

entry1 = Entry(tk, width=20)
entry1.place(x=90, y=10)
entry2 = Entry(tk, width=20)
entry2.place(x=90, y=40)
text1 = Label(tk, text="Your weight:", font="Arial 10")
text1.place(x=10, y=10)
text2 = Label(tk, text="Your height:", font="Arial 10")
text2.place(x=10, y=40)

def calculate(height, weight):   
    return (weight/(height**2))

def result():
    
    if entry1.get() == "" or entry2.get() == "":
        messagebox.showerror("ERROR", "Empty value!")
        return
    
    weight = entry1.get()
    height = entry2.get()
    
    weight = float(weight)
    height = float(height)
    
    if(height > 5):
         height /= 100
        
    if(height <= 0) or (weight <= 0):
        messagebox.showerror("ERROR", "Incorrect information entry, try again!")
        return

    value = calculate(height, weight)

    if(value < 18.5):
        messagebox.showinfo("RESULT", f"You are underweight.\nYour BMI:{value}")
        return
    
    elif(18.5 <= value < 25):
        messagebox.showinfo("RESULT", f"You are healthy weight.\nYour BMI:{value}")
        return
    
    elif(25 <= value < 30):
        messagebox.showinfo("RESULT", f"You are overweight.\nYour BMI:{value}")
        return
    
    elif(30 <= value):
        messagebox.showinfo("RESULT", f"You are obese.\nYour BMI:{value}")
        return

    else:
        print("Incorrect information entry, try again.")
        return

button = Button(tk, text="Calculate", font="Verdana 12 bold",
                padx=10, pady=10,
                activebackground="green",
                command=result).place(x=10, y=70)

tk.mainloop()