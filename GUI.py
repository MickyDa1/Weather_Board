from tkinter import *

def change(userInput):
    with open("D:\\city.txt", "w") as f:
        f.write(userInput)

root = Tk()
root.title("Temperature Location")
root.geometry("500x300")
root.config(bg="lightblue")

label = Label(root, text="Enter The Place", height=1, width=14, font=("Arial", 30))
label.place(x=100, y=40)

entry = Entry(root, font=("Arial", 20), width=15)
entry.place(x=150, y=100)

Quit = Button(root, text="Load Location", command=lambda: change(entry.get()), height=2, width=15, font=("Arial", 15))
Quit.place(x=150, y=147)

root.mainloop()
