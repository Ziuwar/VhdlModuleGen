##################################################################################
# Company: 	    AS Eng / AVSR
# File: 		VhdlGenGui.py
# Author: 		Andreas Schroeder
# Date: 		09.10.2021
#
# Description: 	GUI for the VHDL module generator
# Revision: 	R0.0.0 Not Tested
##################################################################################

from tkinter import *
from tkinter import ttk
from typing import Sized
from bin.ModuleGen import generate_write_files

def main():

    window = Tk()
    window.geometry('500x300')
    window.resizable(False,False)
    window.title("VHDL Module Gen!")

    def generate_button_action():
        generate_write_files(entry_module_name.get(), author_name.get(), software_version.get())
        labeltest = Label(window, text = entry_module_name.get())
        labeltest.grid(column=0)

    #canvas = Canvas(window, width=128, height=128, bg="white")
    #canvas.grid()

    #frame = ttk.Frame(window, padding = 20)
    frame = Frame(window)
    frame.grid(padx = 20, pady = 5)

    #Create a label widget
    #Label(window, text = "Hello World!").grid(row=0,column=0)
    #Label(window, text = "Lorem ipsum dolor sit amet.").grid(row=1,column=0)   
    #Button(window, text= "Generate", padx=30, pady=30, command=ModuleGen.generate_write_files).grid(row=1,column=1)

    # Title Row
    label_top_row = Label(frame, text = "VHDL Module Gen!")
    # Row 1: Description
    label_desc = Label(frame, text = "Lorem ipsum dolor sit amet.")
    # Row 2: Module Name input
    label_module_name = Label(frame, text = "Module Name: ")
    entry_module_name = Entry(frame, width=20)
    entry_module_name.insert(0,"ModuleName")
    # Row 3: Author input
    lable_author = Label(frame, text = "Author Name: ")
    author_name = Entry(frame, width=20)
    author_name.insert(1,"Andreas Schroeder")
    # Row 4: Software Version input
    label_sw_version = Label(frame, text = "Software Version: ")
    software_version = Entry(frame, width=20)
    software_version.insert(2,"20.8.0")
    # Row 5: Generics input
    seperator_hor_top = ttk.Separator(frame, orient="horizontal")
    seperator_hor_mid = ttk.Separator(frame, orient="horizontal")
    seperator_hor_bot = ttk.Separator(frame, orient="horizontal")


    # Row 6, Column 0: Module Inputs

    # Row 6, Column 1: Module Outputs

    # Row 7: Generate Button
    button_generate = Button(frame, text="Generate", padx = 20, pady = 20, command=generate_button_action)

    #Put it on the sreen
    label_top_row.grid(row=0,column=0,columnspan=2)
    label_desc.grid(row=1,column=0,columnspan=2)
    seperator_hor_top.grid(row = 2, columnspan = 2, sticky='NSEW')
    label_module_name.grid(row=3, column=0)
    entry_module_name.grid(row=3, column=1)
    lable_author.grid(row=4, column=0)
    author_name.grid(row=4, column=1)
    label_sw_version.grid(row=5, column=0)
    software_version.grid(row=5, column=1)
    seperator_hor_mid.grid(row = 8, columnspan = 2, sticky='NSEW')




    button_generate.grid(row=9, column=0, columnspan=2)

    #Application loop
    window.mainloop()


if __name__ == '__main__':
    main()