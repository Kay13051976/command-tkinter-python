from tkinter import *
root = Tk()
root.title("My GUI")
root.geometry("450x350+600+500")


def showChoice():
    choice1 = language1.get()
    choice2 = language2.get()
    choice3= language3.get()
    choice4 = language4.get()

    if choice1 == 1:
       Label(text="You have selected Python").pack(anchor=W)
    if choice2 == 1:
       Label(text="You have selected Java").pack(anchor=W)
    if choice3 == 1:
       Label(text="You have selected PHP").pack(anchor=W)
    if choice4 == 1:
       Label(text="You have selected C#").pack(anchor=W)

#0 = not selected, 1 = selected

language1 = IntVar()
Checkbutton(text="Python",variable=language1).pack(anchor=W)
language2 = IntVar()
Checkbutton(text="Java",variable=language2).pack(anchor=W)
language3 = IntVar()
Checkbutton(text="PHP",variable=language3).pack(anchor=W)
language4 = IntVar()
Checkbutton(text="C#",variable=language4).pack(anchor=W)

Button(text="Show Option",command=showChoice).pack(anchor=W)


root.mainloop()