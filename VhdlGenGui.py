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

    #geometry = '1000x1000'
    generic_column_numbers = ('#1','#2','#3')
    io_column_numbers = ('#1','#2')
    generic_columns = ('Identifier','Data Type','Value')
    io_columns = ('Identifier','Number of Bits')
    Title = "VHDL Module Gen!"
    collected_generics = []
    collected_inputs = []
    collected_outputs = []

    def generate_button_action():
        lib.generate_write_files(entry_module_name.get(), author_name.get(), software_version.get(), collected_generics, collected_inputs, collected_outputs)
        #lib.generate_write_files(entry_module_name.get(), author_name.get(), software_version.get(), collected_generics)
        labeltest = Label(window, text = entry_module_name.get())
        labeltest.grid(column=0)

    def generic_insert_button_action():
        generic = []
        generic.append(generic_identifier.get())
        generic.append(generic_datatype.get())
        generic.append(generic_value.get())
        collected_generics.append(generic)
        tree_generics.insert('', END, values=generic)
    
    def generic_delete_button_action():
        collected_generics.clear()
        tree_generics.delete(*tree_generics.get_children())
    
    def input_insert_button_action():
        input = []
        input.append(input_identifier.get())
        input.append(input_bits.get())
        collected_inputs.append(input)
        tree_inputs.insert('',END,values=input)
    
    def output_insert_button_action():
        output = []
        output.append(output_identifier.get())
        output.append(output_bits.get())
        collected_outputs.append(output)
        tree_outputs.insert('',END,values=output)

    def inputs_delete_button_action():
        collected_inputs.clear()
        tree_inputs.delete(*tree_inputs.get_children())

    def outputs_delete_button_action():
        collected_outputs.clear()
        tree_outputs.delete(*tree_outputs.get_children())

    window = Tk()
    #window.geometry(geometry)
    window.resizable(False,False)
    window.title(Title)

    canvas = Canvas(window)
    canvas.grid(row=0, column=0, sticky="NSEW")

    #scrollbar = Scrollbar(window, command=canvas.yview)
    #scrollbar.grid(row=0, column=1, rowspan=50)
    #canvas.configure(yscrollcommand = scrollbar.set)

    #frame = ttk.Frame(window, padding = 20)
    frame = ttk.Frame(canvas)
    canvas.create_window((0,0), window=frame, anchor='nw')
    frame.grid(padx = 20, pady = 5)

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

    button_generic_insert = Button(frame, text="Add", padx = 10, pady = 2, command=generic_insert_button_action)

    label_generic = Label(frame, text = "Enter VHDL Module Generics")
    tree_generics = ttk.Treeview(frame, height = 3, columns=generic_column_numbers, show = 'headings')

    generic_scrollbar = Scrollbar(frame, orient=VERTICAL)
    tree_generics.config(yscrollcommand=generic_scrollbar.set)
    generic_scrollbar.config(command=tree_generics.yview)

    button_generic_delete = Button(frame, text="DELETE ALL", padx = 10, pady = 2, command=generic_delete_button_action)

    # Define headings 
    tree_generics.heading(generic_column_numbers[0], text=generic_columns[0])
    tree_generics.heading(generic_column_numbers[1], text=generic_columns[1])
    tree_generics.heading(generic_column_numbers[2], text=generic_columns[2])

    # Row 6, Column 0: Module Inputs
    label_input_identifier = Label(frame, text = "Identifier: ")
    input_identifier = Entry(frame, width=20)
    input_identifier.insert(2,"input_level")
    label_input_bits = Label(frame, text = "Number of bits: ")
    input_bits = Entry(frame, width=20)
    input_bits.insert(2,"8")

    button_input_insert = Button(frame, text="Add", padx = 10, pady = 2, command=input_insert_button_action)
    label_inputs = Label(frame, text = "Enter VHDL Module Inputs")
    tree_inputs = ttk.Treeview(frame, height = 3, columns=io_column_numbers, show = 'headings')

    inputs_scrollbar = Scrollbar(frame, orient=VERTICAL)
    tree_inputs.config(yscrollcommand=inputs_scrollbar.set)
    inputs_scrollbar.config(command=tree_inputs.yview)

    # Define headings 
    tree_inputs.heading(io_column_numbers[0], text=io_columns[0])
    tree_inputs.heading(io_column_numbers[1], text=io_columns[1])

    button_inputs_delete = Button(frame, text="DELETE ALL", padx = 10, pady = 2, command=inputs_delete_button_action)

    # Row 6, Column 1: Module Outputs
    label_output_identifier = Label(frame, text = "Identifier: ")
    output_identifier = Entry(frame, width=20)
    output_identifier.insert(2,"output_level")
    label_output_bits = Label(frame, text = "Number of bits: ")
    output_bits = Entry(frame, width=20)
    output_bits.insert(2,"8")

    button_output_insert = Button(frame, text="Add", padx = 10, pady = 2, command=output_insert_button_action)
    label_outputs = Label(frame, text = "Enter VHDL Module Outputs")
    tree_outputs = ttk.Treeview(frame, height = 3, columns=io_column_numbers, show = 'headings')

    # Define headings 
    tree_outputs.heading(io_column_numbers[0], text=io_columns[0])
    tree_outputs.heading(io_column_numbers[1], text=io_columns[1])

    button_outputs_delete = Button(frame, text="DELETE ALL", padx = 10, pady = 2, command=outputs_delete_button_action)

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

    # Input Generics
    label_generic_identifier.grid(row=8,column=0)
    label_generic_datatype.grid(row=8,column=1)
    label_generic_value.grid(row=8,column=2)

    generic_identifier.grid(row=9,column=0)
    generic_datatype.grid(row=9,column=1)
    generic_value.grid(row=9,column=2)
    button_generic_insert.grid(row=9,column=3)

    tree_generics.grid(row = 10, column=0, columnspan = 4, sticky='NSEW')
    generic_scrollbar.grid(row = 10, column=5, sticky='NSEW')
    button_generic_delete.grid(row = 11, column=0)

    # Input VHDL Module Inputs
    label_inputs.grid(row=12,column=0,columnspan=4)

    label_input_identifier.grid(row=13,column=0)
    label_input_bits.grid(row=13,column=1)

    input_identifier.grid(row=14,column=0)
    input_bits.grid(row=14,column=1)
    button_input_insert.grid(row=14,column=2)

    tree_inputs.grid(row = 15, column=0, columnspan = 4, sticky='NSEW')
    inputs_scrollbar.grid(row = 15, column=5, sticky='NSEW')
    button_inputs_delete.grid(row=16,column=0)

    # Input VHDL Module Outputs
    label_outputs.grid(row=17,column=0,columnspan=4)

    label_output_identifier.grid(row=18,column=0)
    label_output_bits.grid(row=18,column=1)

    output_identifier.grid(row=19,column=0)
    output_bits.grid(row=19,column=1)
    button_output_insert.grid(row=19,column=2)

    tree_outputs.grid(row = 20, column=0, columnspan = 4, sticky='NSEW')
    button_outputs_delete.grid(row=21,column=0)

    seperator_hor_bot.grid(row = 50, columnspan = 4, sticky='NSEW')
    button_generate.grid(row=51, column=0, sticky='NSEW')

    #Application loop
    window.mainloop()

if __name__ == '__main__':
    main()