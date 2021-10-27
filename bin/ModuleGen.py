##################################################################################
# Company: 	    AS Eng / AVSR
# File: 		VhdlModuleGen.py
# Author: 		Andreas Schroeder
# Date: 		27.09.2021
#
# Description: 	Creates a VHDL module and VUNIT testbench file in the given directory
# Revision: 	R0.0.0 Not Tested
##################################################################################

import bin as lib

def generate_write_files(module_name, author, software_version, generics_in, entity_in_in, entity_out_in):

    source_file = "./output/"+ module_name +".vhd" #Todo
    testbench_source_file_vunit = "./output/"+ module_name +"_tb.vhd"#ToDo
    testbench_source_file_basic = "./output/"+ module_name +"_test.vhd"#ToDo

    lib.write_source_file(source_file,lib.assemble_source_file(module_name,author,software_version,generics_in,entity_in_in,entity_out_in))
    lib.write_source_file(testbench_source_file_vunit,lib.assemble_testbench_vunit_file(module_name,author,software_version,generics_in,entity_in_in,entity_out_in))
    lib.write_source_file(testbench_source_file_basic,lib.assemble_testbench_basic_file(module_name,author,software_version,generics_in,entity_in_in,entity_out_in))
