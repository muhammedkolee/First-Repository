from tkinter import *
from tkinter import messagebox

tk = Tk()

tk.title("Exam Calculator")
tk.geometry("750x400")
entry1 = Entry(tk)
entry1.place(x=110, y=11)
text1 = Label(tk, text="Your pass grade:", width=13)
text1.place(x=10, y=10)

entry2 = Entry(tk)
entry2.place(x=130, y=41)
text2 = Label(tk, text="Your midterm result:", width=16)
text2.place(x=10, y=40)

entry3 = Entry(tk)
entry3.place(x=140, y=71)
text3 = Label(tk, text="Your final/resit result:", width=17)
text3.place(x=10, y=70)

def calculate():
    if entry1.get() == "" or entry2.get() == "" or entry3.get() == "":
        messagebox.showerror("ERROR", "Empty value!")
    
    else:
        result = float(entry2.get())*(2/5) + float(entry3.get())*(3/5)
        if(result >= float(entry1.get())):
            messagebox.showinfo("RESULT", f"Congratulations, You have successfully passed the lesson!\nYour average:{result}")
    
        elif(0 <= result < float(entry1.get())):
            messagebox.showerror("FAIL", f"You failed the lesson. Your average:{result}")           

        else:
            messagebox.showerror("ERROR", "İncorrect information entry, try again.")

button = Button(tk, text="Calculate", font="Verdana 12 bold",
                padx=10, pady=10,
                activebackground="green",
                command=calculate).place(x=10, y=150)

tk.mainloop()