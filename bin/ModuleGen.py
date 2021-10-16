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

generics = [("target_time", "integer", 5),("target_aquired", "integer", 1)] #ToDo
entity_in = [("Clock", 1),("Reset_n", 1),("TimingPulse", 15),("WarningEnable_n", 11)] #ToDo
entity_out = [("SirenOn", 1),("HornControl", 9), ("MuteActive", 3)]#Todo

def generate_write_files(module_name, author, software_version):

    source_file= "./output/"+ module_name +".vhd" #Todo
    testbench_source_file_vunit = "./output/"+ module_name +"_tb.vhd"#ToDo
    testbench_source_file_basic = "./output/"+ module_name +"_test.vhd"#ToDo

    lib.write_source_file(source_file,lib.assemble_source_file(module_name,author,software_version,generics,entity_in,entity_out))
    lib.write_source_file(testbench_source_file_vunit,lib.assemble_testbench_vunit_file(module_name,author,software_version,generics,entity_in,entity_out))
    lib.write_source_file(testbench_source_file_basic,lib.assemble_testbench_basic_file(module_name,author,software_version,generics,entity_in,entity_out))

