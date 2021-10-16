##################################################################################
# Company: 	    AS Eng / AVSR
# File: 		SourceText.py
# Author: 		Andreas Schroeder
# Date: 		27.09.2021
#
# Description: 	Blocks of text for the source file
# Revision: 	R0.0.0 Not Tested
##################################################################################

def assemble_source_file (module_name,author,software_version,generics,entity_in,entity_out):
    source_file =  header_gen(module_name, author, software_version)
    source_file += blank_lines(1)
    source_file += include_libs()
    source_file += blank_lines(1)
    source_file += doxygen_start(module_name)
    source_file += blank_lines(1)
    source_file += entity(module_name, generics, entity_in, entity_out)
    source_file += blank_lines(1)
    source_file += architecture(module_name)
    source_file += doxygen_end()
    return source_file

def header_gen (module_name,author,software_version): # Creation of the header for the implementation file
    header_text ="-----------------------------------------------------------------\n"
    header_text +="--! @file	"+ module_name +".vhd\n"
    header_text +="--! @brief	Implementation of the VHDL module "+ module_name +".vhd\n"
    header_text +="\n"
    header_text +="--! @copyright 2021 Avionik Straubing Entwicklungs GmbH\n"
    header_text +="--! @version Version 1.0, Platform: Quartus "+ software_version +"\n"
    header_text +="\n"
    header_text +="--! | Attribute | Value |\n"
    header_text +="--! | :-- | :-- |\n"
    header_text +="--! | Subversion revision | $Rev:$ |\n"
    header_text +="--! | Time of last change | $Date:$ |\n"
    header_text +="--! | Author(s) | @author "+ author +" |\n"
    header_text +="-----------------------------------------------------------------\n"
    return header_text

def doxygen_start (module_name): # Doxygen groups definition
    doxygen_groups = "--! \\addtogroup "+ module_name +"_Module\n"
    doxygen_groups += "--! @{\n"
    doxygen_groups += "--! \\addtogroup "+ module_name +"_Implementation\n"
    doxygen_groups += "--! @{\n"
    return doxygen_groups

def doxygen_end (): # Close the doxygen groups
    doxygen_close_grp = "--! @}\n"
    doxygen_close_grp += "--! @}\n"
    return doxygen_close_grp

def include_libs (): # Default list of libraries to include
    lib_list = "library ieee;\n"
    lib_list += "use ieee.std_logic_1164.all;\n"
    lib_list += "use ieee.std_logic_arith.all;\n"
    lib_list += "use ieee.numeric_std.all;\n"
    lib_list += "use ieee.std_logic_unsigned.all;\n"
    lib_list += "use ieee.math_real.all;\n"
    return lib_list

def blank_lines (count): # Adds blank lines from 1 to 99
    if count > 0 and count < 100:
        i = 1
        blank_lines = "\n"
        while i < count:
            blank_lines += "\n"
            i += 1
    else:
        return ""
    return blank_lines

def entity (module_name, generics, entity_in, entity_out): # Entity generation with inputs, outputs and generics
    entity_list = "--! @brief Entity of the "+ module_name +" logic module.\n"
    entity_list += "--! @details All test signal generation and result analysis is done here.\n" # TBD

    entity_list += "entity e_"+ module_name +" is\n"

    if generics:
        entity_list += "    generic(\n"
        for generic in generics:
            entity_list += "        "+ generic[0] +" : "+ generic[1] +" := "+ str(generic[2]) +";\n"
        entity_list += "    );\n"

    entity_list += "    port(\n"

    if entity_in:
        for entity in entity_in:
            entity_list += "        "+ entity[0] +" : in "
            
            if entity[1] == 1:
                 entity_list += "std_logic;\n"
            else:
                entity_list += "std_logic_vector ("+ str(entity[1]) +" downto 0);\n"

    entity_list += "\n"

    if entity_out:
        for entity in entity_out:
            entity_list += "        "+ entity[0] +" : out "

            if entity[1] == 1:
                 entity_list += "std_logic"
            else:
                entity_list += "std_logic_vector ("+ str(entity[1]) +" downto 0)"

            if entity_out[len(entity_out) - 1] == entity:
                entity_list += "\n"
            else:
                entity_list += ";\n"

    entity_list += "    );\n"
    entity_list += "end entity e_"+ module_name +";\n"

    return entity_list

def architecture (module_name): # Architecture generation
    architecture_list = "architecture a_"+ module_name +" of e_"+ module_name +" is\n"
    architecture_list += "begin\n"
    architecture_list += blank_lines(10)
    architecture_list += "end architecture a_"+ module_name +";\n"
    return architecture_list

