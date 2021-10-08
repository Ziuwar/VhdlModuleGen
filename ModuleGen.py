##################################################################################
# Company: 	    AS Eng / AVSR
# File: 		VhdlModuleGen.py
# Author: 		Andreas Schroeder
# Date: 		27.09.2021
#
# Description: 	Creates a VHDL module and VUNIT testbench file in the given directory
# Revision: 	R0.0.0 Not Tested
##################################################################################

import FileOps
import SourceText
import TestbenchGen

module_name = "SuperDuperThing"
quartus_version = "20.3.0"
author = "Andreas Schroeder"

generics = [("target_time", "integer", 5),("target_aquired", "std_logic", 1)]
entity_in = [("Clock", 1),("Reset_n", 1),("TimingPulse", 15),("WarningEnable_n", 11)]
entity_out = [("SirenOn", 1),("HornControl", 9), ("MuteActive", 3)]

source_dir = "./Output/"+ module_name +".vhd"
testbench_source_dir = "./Output/"+ module_name +"_tb.vhd"

def assemble_source_file():
    source_file =  SourceText.header_gen(module_name, author, quartus_version)
    source_file += SourceText.blank_lines(1)
    source_file += SourceText.include_libs()
    source_file += SourceText.blank_lines(1)
    source_file += SourceText.doxygen_start(module_name)
    source_file += SourceText.blank_lines(1)
    source_file += SourceText.entity(module_name, generics, entity_in, entity_out)
    source_file += SourceText.blank_lines(1)
    source_file += SourceText.architecture(module_name)
    source_file += SourceText.doxygen_end()
    return source_file

def assemble_testbench_vunit_file():
    testbench_file =  TestbenchGen.header_gen_tb(module_name, author, quartus_version)
    testbench_file += SourceText.blank_lines(1)
    testbench_file += TestbenchGen.include_libs_vunit_tb()
    testbench_file += SourceText.blank_lines(1)
    testbench_file += TestbenchGen.doxygen_start_tb(module_name)
    testbench_file += SourceText.blank_lines(1)
    testbench_file += TestbenchGen.entity_vunit_tb(module_name)
    testbench_file += SourceText.blank_lines(1)
    testbench_file += TestbenchGen.assamble_architecture_vunit_tb(module_name, generics, entity_in, entity_out)
    testbench_file += TestbenchGen.doxygen_end_tb()
    return testbench_file

FileOps.write_source_file(source_dir,assemble_source_file())
FileOps.write_source_file(testbench_source_dir,assemble_testbench_vunit_file())

