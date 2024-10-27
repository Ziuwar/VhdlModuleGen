##################################################################################
# File: 		FileOps.py
# Author: 		Ziuwar
# Date: 		27.09.2021
#
# Description: 	File handling - Open - Write - Read - Close - Directory selection and change
# Revision: 	R0.0.0 Not Tested
##################################################################################


def write_source_file(file,text):
    file_open_mode = "w"
    #Create the file.
    imp_source = open(file, file_open_mode)
    imp_source.write(text)
    imp_source.close()

def append_source_file(file,text):
    file_open_mode = "a"
    #Create the file.
    imp_source = open(file, file_open_mode)
    imp_source.write(text)
    imp_source.close()

