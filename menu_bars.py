# MADE BY: Lisette Spalding
# FILE NAME: menu_bars.py
# DATE CREATED: 02/03/2021
# DATE LAST MODIFIED: 01/20/2021

###### IMPORTS ######
from tkinter import *
######## FIN ########

##### CONSTANTS #####
HEIGHT = 500
WIDTH = 500
TITLE = "Menu Bar Practice"
BACKGROUND = "white"
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
        self.grid()
        self.create()

    def create(self):
        """ To use: create()
         This is the create function, it creates the app widgets."""
        ## !! MENU !! ##
        # ..MAIN MENU.. #
        menubar = Menu(self.master) # This is stating that the 'master' of the menubar is the master class
        self.master.config(menu=menubar) # Configuring the master class. Adding the menubar
        fileMenu = Menu(menubar) # Opening the file Menu of the menubar

        editMenu = Menu(menubar)

        # Commands in the file menu
        fileMenu.add_command(label="Exit", command=self.onExit)
        fileMenu.add_command(label="Open", command=self.onOpen)
        fileMenu.add_command(label="Save", command=self.onSave)
        # Fin.

        menubar.add_cascade(label="File", menu=fileMenu)

        menubar.add_cascade(label="Edit", menu=editMenu)

        editMenu.add_command(label="Destroy Frame One", command=self.destroyFrame1)
        editMenu.add_command(label="Create Frame Three", command=self.createFrame3)
        # ..FIN.. #

        # ..SUB MENU.. #
        submenu = Menu(fileMenu)
        submenu.add_command(label="New Feed")
        submenu.add_command(label="Bookmarks")
        submenu.add_command(label="Mail")

        fileMenu.add_cascade(label="Import", menu=submenu, underline=0)
        fileMenu.add_separator()
        # ..FIN.. #
        ### !! FIN !! ###

        ## !! FRAMES !! ##
        self.frame1 = Frame(self, bg="red", width=250, height=250)
        self.frame1.grid(row=0, column=0)

        self.frame2 = Frame(self, bg="blue", width=250, height=250)
        self.frame2.grid(row=0, column=1)
        ### !! FIN !! ###

        # Label - Frame One
        self.lbl1 = Label(self.frame1, text="Testing...").pack(padx=20, pady=20,
                                                               fill=BOTH,
                                                               expand=True)
        # Label - Frame Two
        self.lbl2 = Label(self.frame2, text="Testing...").pack(padx=20, pady=20,
                                                               fill=BOTH,
                                                               expand=True)

    def onExit(self):
        self.quit()

    def onOpen(self):
        pass

    def onSave(self):
        pass

    def destroyFrame1(self):
        self.frame1.destroy()

    def createFrame3(self):
        self.frame3 = Frame(self, bg ="yellow", width=250, height=250)
        self.frame3.grid(row=2, column=0)

        self.lbl3 = Label(self.frame3, text="Testing...").pack(padx=20, pady=20,
                                                               fill=BOTH,
                                                               expand=True)
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
    root.mainloop()  # Running the loop
######## FIN #########

main()