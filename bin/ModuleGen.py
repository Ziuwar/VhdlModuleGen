##################################################################################
# Company: 	    AS Eng / AVSR
# File: 		VhdlModuleGen.py
# Author: 		Andreas Schroeder
# Date: 		27.09.2021
#
# Description: 	Creates a VHDL module and VUNIT testbench file in the given directory
# Revision: 	R0.0.0 Not Tested
##################################################################################

from bin.FileOps import *
from bin.SourceText import *
from bin.TestbenchGen import *

#module_name = "SuperDuperThing"
#software_version = "20.3.0"
#author = "Andreas Schroeder"

generics = [("target_time", "integer", 5),("target_aquired", "std_logic", 1)]
entity_in = [("Clock", 1),("Reset_n", 1),("TimingPulse", 15),("WarningEnable_n", 11)]
entity_out = [("SirenOn", 1),("HornControl", 9), ("MuteActive", 3)]

def generate_write_files(module_name, author, software_version):

    source_file= "./output/"+ module_name +".vhd"
    testbench_source_file_vunit = "./output/"+ module_name +"_tb.vhd"
    testbench_source_file_basic = "./output/"+ module_name +"_test.vhd"

    write_source_file(source_file,assemble_source_file(module_name,author,software_version,generics,entity_in,entity_out))
    write_source_file(testbench_source_file_vunit,assemble_testbench_vunit_file(module_name,author,software_version,generics,entity_in,entity_out))
    write_source_file(testbench_source_file_basic,assemble_testbench_basic_file(module_name,author,software_version,generics,entity_in,entity_out))


#generate_write_files()