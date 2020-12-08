from tkinter import Tk, Label, Button

class MyFirstGUI:
    def __init__(self, master):
        self.master = master
        master.title("My first simple GUI")

        self.w_button = Button(master, text="Click me", command=self.greet)
        self.w_button.pack()

    def greet(self):
        print("Wonderful!")

root = Tk()
my_gui = MyFirstGUI(root)
root.mainloop()