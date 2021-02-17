# MADE BY: Lisette Spalding
# FILE NAME: tkinter_starter_template.py
# DATE CREATED: 02/17/2021
# DATE LAST MODIFIED: 02/17/2021

###### IMPORTS ######
from tkinter import *
from tkinter import messagebox as mb, filedialog
from tkinter import colorchooser as cc
######## FIN ########

##### CONSTANTS #####
HEIGHT = 200
WIDTH = 500
TITLE = "New Program"
BACKGROUND = "darkgrey"
FONT = "San_Serif"
######## FIN ########

######## CLASS #######
class App(Frame):
    """ To use: App(root)
        This is the App class, this class creates the application. """
    def __init__(self, master):
        """ To Use: You don't.
         This is the "in it" function. This function determines the constant variables in this class."""
        super(App, self).__init__(master)
        # self.grid()
        self.pack(fill=BOTH, expand=1)
        self.create()

    def create(self):
        """ To use: create()
         This is the create function, it creates the app widgets."""
        menubar = Menu(self.master)
        self.master.config(menu=menubar)
        fileMenu = Menu(menubar)
        fileMenu.add_command(label="Open", command=self.onOpen)
        menubar.add_cascade(label="File", menu=fileMenu)

        self.txt = Text(self)
        self.txt.pack(fill=BOTH, expand=1)

    def onOpen(self):
        ftypes = [("Python Files","*.py"),("Plain Text","*.txt"),("All Files","*")]
        dlg = filedialog.Open(self, filetypes=ftypes)
        f1 = dlg.show()
        if f1 != "":
            text = self.readFile(f1)
            self.txt.insert(END, text)

    def readFile(self, filename):
        with open(filename, "r") as f:
            text = f.read()
            return text

    #     ####### !! BUTTONS !! #######
    #     ## Creating Buttons ##
    #     self.bttn = Button (self, text="Choose Color:",
    #                         command=self.onChoose)
    #     self.bttn.place(x=30, y=30)
    #
    #     self.frame = Frame(self, border=1,
    #                        relief=RIDGE, width=100, height=100)
    #     self.frame.place(x=160, y=30)
    #
    # def onChoose(self):
    #     (rgb, hx) = cc.askcolor()
    #     self.frame.config(bg=hx)

    #     ####### !! BUTTONS !! #######
    #     ## Creating Buttons ##
    #     errorBttn = Button(self, text="Error", command=self.onError)
    #     warningBttn = Button(self, text="Warning", command=self.onWarn)
    #     questionBttn = Button(self, text="Question", command=self.onQuest)
    #     informBttn = Button(self, text="Information", command=self.onInfo)
    #     ## FIN ##
    #
    #     ### Grid Placement ###
    #     errorBttn.grid(row=0, column=0, padx=5, pady=5)
    #     warningBttn.grid(row=1, column=0)
    #     questionBttn.grid(row=0, column=1)
    #     informBttn.grid(row=1, column=1)
    #     ## FIN ##
    #
    # def onError(self):
    #     mb.showerror("Error", "You had an error... :(")
    #     self.master.destroy()
    #
    # def onWarn(self):
    #     mb.showwarning("Warning!!", "You did something wrong!! Don't do that!")
    #
    # def onQuest(self):
    #     result = mb.askquestion("Question...", "Are you sure that you want to quit?")
    #     if result == "yes":
    #         mb.showinfo("Information...", "Goodbye")
    #         self.master.destroy()
    #     else:
    #         return
    #
    # def onInfo(self):
    #     mb.showinfo("Information", "Loading information...")


def main():
    # General Setup
    root = Tk()
    root.geometry(str.format("{}x{}", WIDTH, HEIGHT))
    root.title(TITLE)

    ## Configurations ##
    root.configure(bg=BACKGROUND)
    ####### FIN ########

    # Conjuring the App
    app = App(root)
    root.mainloop() # Running the loop
######## FIN #########

main()