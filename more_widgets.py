# MADE BY: Lisette Spalding
# FILE NAME: more_widgets.py
# DATE CREATED: 02/05/2021
# DATE LAST MODIFIED: 02/05/2021

###### IMPORTS ######
from tkinter import *
from tkinter.ttk import *
######## FIN ########

##### CONSTANTS #####
HEIGHT = 200
WIDTH = 200
TITLE = "List Boxes and Combo Boxes"
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
        self.pack(fill=BOTH)

        self.create()

    def create(self):
        """ To use: create()
         This is the create function, it creates the app widgets."""
        ##### !! SELECT MENUS !! #####
        ##### ..Listboxes.. #####
        self.listbox = Listbox(self, selectmode=EXTENDED)
        self.listboxItems = ["test1", "test2", "test3", "test4", "test5"]

        for i in range(len(self.listboxItems)):
            self.listbox.insert(END, self.listboxItems[i])

        self.listbox.pack(side=LEFT)
        ######## ..FIN.. ########

        ##### ..Comboboxes.. #####
        self.itemslistcb = [1, 2, 3, 4, 5, "hello"]
        self.combobox = Combobox(self, value=self.itemslistcb)
        ## Other ways of doing combobox selections:
        ### self.combobox.config(value=self.itemslistcb)
        ### self.combobox["value"] = self.itemslistcb
        self.combobox.current(5)
        self.combobox.pack(side=LEFT)
        ######## ..FIN.. #########
        ########## !! FIN !! #########

        ###### ..Buttons.. ######
        self.submit = Button(self, text="Try me!", command=self.update)
        self.submit.pack(side=LEFT)

        self.increase = Button(self, text=">>>>>>", command=self.inc)
        self.increase.pack(side=LEFT)

        self.decrease = Button(self, text="<<<<<<", command=self.dec)
        self.decrease.pack(side=LEFT)
        ######## ..FIN.. ########

        ###### ..Progressbars.. ######
        self.progressbar = Progressbar(self, length=500)
        self.progressbar.pack(side=LEFT)
        ########### ..FIN.. ##########

    def inc(self):
        self.progressbar["value"] = self.progressbar["value"] + 1

    def dec(self):
        self.progressbar["value"] = self.progressbar["value"] - 1

    def update(self):
        # !! COMBOBOXES:
        cbtext = self.combobox.get()
        print(cbtext)
        # !! FIN

        # !! LISTBOXES:
        ## Single Selection Code:
        ### x = self.listbox.get(ANCHOR)
        ### print(x)
        x = ""
        selected = self.listbox.curselection()
        for i in selected:
            x += " "+self.listbox.get([i])

            # How to insert listbox stuff into combobox:
            self.itemslistcb.append(self.listbox.get(i))
        self.combobox["value"] = self.itemslistcb

        print(x)

        # How to insert combobox stuff into listbox:
        self.listbox.insert(END, cbtext)
        # !! FIN

def main():
    # General Setup
    root = Tk()
    ## UNEEDED: root.geometry(str.format("{}x{}", WIDTH, HEIGHT))
    root.title(TITLE)

    ## Configurations ##
    root.configure(bg=BACKGROUND)
    ####### FIN ########

    # Conjuring the App
    app = App(root)
    root.mainloop() # Running the loop
######## FIN #########

main()