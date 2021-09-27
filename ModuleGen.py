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

module_name = "SuperDuperThing"
quartus_version = "20.3.0"
author = "Andreas Schroeder"

generics = [("target_time", "integer", 5)]
entity_in = [("Clock", 1),("Reset_n", 1),("TimingPulse", 15),("WarningEnable_n", 11)]
entity_out = [("SirenOn", 1),("HornControl", 9), ("MuteActive", 3)]

source_dir = "C:\\Temp\\vhdl_gen\\"+ module_name +".vhd"

def assemble_source_file():
    source_file = SourceText.header_gen(module_name, author, quartus_version)
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

FileOps.write_source_file(source_dir,assemble_source_file())

