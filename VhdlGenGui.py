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

import bin as lib

def main():

    geometry = '1000x1000'
    column_numbers = ('#1','#2','#3')
    columns = ('Identifier','Data Type','Value')
    Title = "VHDL Module Gen!"

    window = Tk()
    window.geometry(geometry)
    window.resizable(True,False)
    window.title(Title)

    def generate_button_action():
        lib.generate_write_files(entry_module_name.get(), author_name.get(), software_version.get())
        labeltest = Label(window, text = entry_module_name.get())
        labeltest.grid(column=0)

    def generic_insert_button_action():
        print("Click!")
        generic[0] = generic_identifier.get()
        generic[1] = generic_datatype.get()
        generic[2] = software_version.get()
        tree_generics.insert('', END, values=generic)

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
    label_top_row = Label(frame, text = Title)
    # Row 1: Description
    label_desc = Label(frame, text = "Lorem ipsum dolor sit amet.")
    # Row 2: Module Name input
    label_module_name = Label(frame, text = "Module Name: ")
    entry_module_name = Entry(frame, width=20)
    entry_module_name.insert(0,"ModuleName")
    # Row 3: Author input
    label_author = Label(frame, text = "Author Name: ")
    author_name = Entry(frame, width=20)
    author_name.insert(1,"Andreas Schroeder")
    # Row 4: Software Version input
    label_sw_version = Label(frame, text = "Software Version: ")
    software_version = Entry(frame, width=20)
    software_version.insert(2,"20.8.0")

    # Row 5: Generics input
    label_generic_identifier = Label(frame, text = "Identifier: ")
    generic_identifier = Entry(frame, width=20)
    generic_identifier.insert(2,"max_level")
    label_generic_datatype = Label(frame, text = "Data Type: ")
    generic_datatype = Entry(frame, width=20)
    generic_datatype.insert(2,"integer")
    label_generic_value = Label(frame, text = "Value: ")
    generic_value = Entry(frame, width=20)
    generic_value.insert(2,"42")

    button_generic_insert = Button(frame, text="Insert", padx = 10, pady = 2, command=generic_insert_button_action)

    label_generic = Label(frame, text = "Enter VHDL Module Generics")
    tree_generics = ttk.Treeview(frame, columns=column_numbers, show = 'headings')

    # Define headings 
    tree_generics.heading(column_numbers[0], text=columns[0])
    tree_generics.heading(column_numbers[1], text=columns[1])
    tree_generics.heading(column_numbers[2], text=columns[2])

    generics = [("target_time", "integer", 5),("target_acquired", "integer", 1)]

    for generic in generics:
        tree_generics.insert('', END, values=generic)


    # Row 6, Column 0: Module Inputs

    # Row 6, Column 1: Module Outputs

    # Row 7: Generate Button
    button_generate = Button(frame, text="Generate", padx = 20, pady = 20, command=generate_button_action)

    seperator_hor_top = ttk.Separator(frame, orient="horizontal")
    seperator_hor_mid = ttk.Separator(frame, orient="horizontal")
    seperator_hor_bot = ttk.Separator(frame, orient="horizontal")

    #Put it on the screen
    label_top_row.grid(row=0,column=0,columnspan=4)

    label_desc.grid(row=1,column=0,columnspan=4)

    seperator_hor_top.grid(row = 2, columnspan = 4, sticky='NSEW')

    label_module_name.grid(row=3, column=0)
    entry_module_name.grid(row=3, column=1)

    label_author.grid(row=4, column=0)
    author_name.grid(row=4, column=1)

    label_sw_version.grid(row=5, column=0)
    software_version.grid(row=5, column=1)

    seperator_hor_mid.grid(row = 6, columnspan = 4, sticky='NSEW')

    label_generic.grid(row=7,column=0,columnspan=4)

    label_generic_identifier.grid(row=8,column=0)
    label_generic_datatype.grid(row=8,column=1)
    label_generic_value.grid(row=8,column=2)

    generic_identifier.grid(row=9,column=0)
    generic_datatype.grid(row=9,column=1)
    generic_value.grid(row=9,column=2)

    button_generic_insert.grid(row=9,column=3)

    tree_generics.grid(row = 10, column=0, columnspan = 4)



    seperator_hor_bot.grid(row = 19, columnspan = 4, sticky='NSEW')
    button_generate.grid(row=20, column=0, sticky='NSEW')

    #Application loop
    window.mainloop()


if __name__ == '__main__':
    main()