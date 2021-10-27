##################################################################################
# Company: 	    AS Eng / AVSR
# File: 		TestbenchGen.py
# Author: 		Andreas Schroeder
# Date: 		27.09.2021
#
# Description: 	Blocks of text for the testbench source file 
# Revision: 	R0.0.0 Not Tested
##################################################################################

#from bin.TestbenchProcedures import *

import bin as lib

def assemble_testbench_vunit_file (module_name, author, software_version, generics, entity_in, entity_out):
    testbench_file =  header_gen_tb(module_name, author, software_version)
    testbench_file += lib.blank_lines(1)
    testbench_file += include_libs_vunit_tb()
    testbench_file += include_libs_tb()
    testbench_file += lib.blank_lines(1)
    testbench_file += doxygen_start_tb(module_name)
    testbench_file += lib.blank_lines(1)
    testbench_file += entity_vunit_tb(module_name)
    testbench_file += lib.blank_lines(1)
    testbench_file += assamble_architecture_vunit_tb(module_name, generics, entity_in, entity_out)
    testbench_file += doxygen_end_tb()
    return testbench_file

def assamble_architecture_vunit_tb (module_name, generics, entity_in, entity_out):
    architecture_list = architecture_start_tb(module_name)
    architecture_list += signals_out(entity_in)
    architecture_list += lib.blank_lines(1)
    architecture_list += signals_in_tb(entity_out)
    architecture_list += lib.blank_lines(1)
    architecture_list += testbench_signals()
    architecture_list += lib.blank_lines(1)
    architecture_list += architecture_begin_tb()
    architecture_list += dut_instantiation_tb(module_name, generics, entity_in, entity_out)
    architecture_list += lib.blank_lines(1)
    architecture_list += main_process_vunit_tb(module_name)
    architecture_list += lib.blank_lines(1)
    architecture_list += variables_vunit_tb(module_name)
    architecture_list += lib.blank_lines(1)
    architecture_list += lib.include_procedures(module_name)
    architecture_list += lib.blank_lines(1)
    architecture_list += main_process_begin_tb()
    architecture_list += open_report_file_vunit_tb()
    architecture_list += lib.blank_lines(1)
    architecture_list += vunit_start_tb()
    architecture_list += lib.blank_lines(1)
    architecture_list += testbench_vunit_while_tb()
    architecture_list += vunit_testcase_one_tb(module_name)
    architecture_list += lib.blank_lines(1)
    architecture_list += vunit_testcase_two_tb(module_name)
    architecture_list += lib.blank_lines(1)
    architecture_list += report_vhdl_footer_tb(module_name)
    architecture_list += lib.blank_lines(1)
    architecture_list += close_loops_tb()
    architecture_list += main_process_end_tb()
    architecture_list += lib.blank_lines(1)
    architecture_list += lib.clock_process()
    architecture_list += lib.blank_lines(1)
    architecture_list += architecture_end_tb(module_name)
    return architecture_list

def assemble_testbench_basic_file (module_name, author, software_version, generics, entity_in, entity_out):
    testbench_file =  header_gen_tb(module_name, author, software_version)
    testbench_file += lib.blank_lines(1)
    testbench_file += include_libs_tb()
    testbench_file += lib.blank_lines(1)
    testbench_file += doxygen_start_tb(module_name)
    testbench_file += lib.blank_lines(1)
    testbench_file += entity_tb(module_name)
    testbench_file += lib.blank_lines(1)
    testbench_file += architecture_start_tb(module_name)
    testbench_file += signals_out(entity_in)
    testbench_file += lib.blank_lines(1)
    testbench_file += signals_in_tb(entity_out)
    testbench_file += lib.blank_lines(1)
    testbench_file += testbench_signals()
    testbench_file += lib.blank_lines(1)
    testbench_file += architecture_begin_tb()
    testbench_file += dut_instantiation_tb(module_name, generics, entity_in, entity_out)
    testbench_file += lib.blank_lines(2)
    testbench_file += basic_testcase()
    testbench_file += lib.blank_lines(1)
    testbench_file += lib.clock_process()
    testbench_file += lib.blank_lines(1)
    testbench_file += architecture_end_tb(module_name)
    testbench_file += doxygen_end_tb()
    return testbench_file

def header_gen_tb (module_name,author,quartus_version): # Creation of the header for the implementation file
    header_text ="-----------------------------------------------------------------\n"
    header_text +="--! @file	"+ module_name +".vhd\n"
    header_text +="--! @brief	Testbench for the module "+ module_name +".vhd\n"
    header_text +="\n"
    header_text +="--! @copyright 2021 Avionik Straubing Entwicklungs GmbH\n"
    header_text +="--! @version Version 1.0, Platform: Quartus "+ quartus_version +"\n"
    header_text +="\n"
    header_text +="--! | Attribute | Value |\n"
    header_text +="--! | :-- | :-- |\n"
    header_text +="--! | Subversion revision | $Rev:$ |\n"
    header_text +="--! | Time of last change | $Date:$ |\n"
    header_text +="--! | Author(s) | @author "+ author +" |\n"
    header_text +="-----------------------------------------------------------------\n"
    return header_text

def doxygen_start_tb (module_name): # Doxygen groups definition
    doxygen_groups = "--! \\addtogroup "+ module_name +"_Module\n"
    doxygen_groups += "--! @{\n"
    doxygen_groups += "--! \\addtogroup "+ module_name +"_Testbench\n"
    doxygen_groups += "--! @{\n"
    return doxygen_groups

def doxygen_end_tb (): # Close the doxygen groups
    doxygen_close_grp = "--! @}\n"
    doxygen_close_grp += "--! @}\n"
    return doxygen_close_grp

def include_libs_vunit_tb (): # Default list of libraries to include - VUNIT
    lib_list = "-- Import vunit lib\n"
    lib_list += "library vunit_lib;\n"
    lib_list += "use vunit_lib.print_pkg.all;\n"
    lib_list += "use vunit_lib.log_levels_pkg.all;\n"
    lib_list += "use vunit_lib.logger_pkg.all;\n"
    lib_list += "use vunit_lib.log_handler_pkg.all;\n"
    lib_list += "use vunit_lib.run_pkg.all;\n"
    lib_list += "--! \cond\n"
    lib_list += "context vunit_lib.vunit_context;\n"
    lib_list += "--! \endcond\n"
    return lib_list

def include_libs_tb (): # Default list of libraries to include
    lib_list = "library ieee;\n"
    lib_list += "use ieee.std_logic_1164.all;\n"
    lib_list += "use ieee.std_logic_arith.all;\n"
    lib_list += "use ieee.numeric_std.all;\n"
    lib_list += "use ieee.std_logic_unsigned.ALL;\n"
    lib_list += "use std.textio.all;\n"
    return lib_list

def entity_vunit_tb (module_name): # Entity generation with inputs, outputs and generics - VUNIT version
    entity_list = "--! @brief Test of the "+ module_name +" logic module.\n"
    entity_list += "--! @details All test signal generation and result analysis is done here.\n"
    entity_list += "entity e_"+ module_name +"Qualification_TB is\n"
    entity_list += "    generic (runner_cfg : string := runner_cfg_default);\n"
    entity_list += "    port(\n"
    entity_list += "        trigger : out std_logic := '0' --! Trigger is set when test evaluation timing is required\n"
    entity_list += "        );\n"
    entity_list += "end entity e_"+ module_name +"Qualification_TB;\n"
    return entity_list

def entity_tb (module_name): # Entity generation with inputs, outputs and generics
    entity_list = "--! @brief Test of the "+ module_name +" logic module.\n"
    entity_list += "--! @details All test signal generation and result analysis is done here.\n"
    entity_list += "entity e_"+ module_name +"Qualification_TB is\n"
    entity_list += "    port(\n"
    entity_list += "        trigger : out std_logic := '0' --! Trigger is set when test evaluation timing is required\n"
    entity_list += "        );\n"
    entity_list += "end entity e_"+ module_name +"Qualification_TB;\n"
    return entity_list
    
def assamble_architecture_tb ():
    architecture_list = ""
    return architecture_list

def architecture_start_tb (module_name):
    return "architecture a_"+ module_name +"Qualification_TB of e_"+ module_name +"Qualification_TB is\n"

def architecture_begin_tb ():
    return "begin\n"

def architecture_end_tb (module_name):
    return "end architecture a_"+ module_name +"Qualification_TB;\n"

def signals_out (entity_in):
    if entity_in:
        signals_list = "    -- Testbench Outputs\n"
        for input in entity_in:
            signals_list += "    signal "+ input[0] +" : "
            if input[1] == 1:
                 signals_list += "std_logic;\n"
            else:
                signals_list += "std_logic_vector ("+ str(input[1]) +" downto 0);\n"
    else:
        entity_in = "There was no input specified.\n"
    return signals_list

def signals_in_tb (entity_out):
    if entity_out:
        signals_list = "    -- Testbench Inputs\n"
        for output in entity_out:
            signals_list += "    signal "+ output[0] +" : "
            if output[1] == 1:
                 signals_list += "std_logic;\n"
            else:
                signals_list += "std_logic_vector ("+ str(output[1]) +" downto 0);\n"
    else:
        entity_out = "There was no output specified.\n"
    return signals_list

def testbench_signals():
    tb_signals_list =  "    -- Testbench signals\n"
    tb_signals_list += "    signal clock_go     : std_logic := '0';     --! Enables the clock generation\n"
    tb_signals_list += "    signal clock_period : time := 125 ns;       --! Clock periode\n"
    return tb_signals_list

def dut_instantiation_tb (module_name, generics, signals_out, signals_in):
    portmap_list = "   --! @brief DUT instantiation\n"
    portmap_list += "   --! @details Instantiation of the DUT\n"
    portmap_list += "   i_DUT : entity work.e_"+ module_name +"(a_"+ module_name +")\n"
    if generics:
        portmap_list += "    generic map(\n"
        for generic in generics:
            portmap_list += "    "+ generic[0] +" => "+ str(generic[2])
            if generics[len(generics) - 1] == generic:
                portmap_list += "\n"
            else:
                portmap_list += ",\n"
        portmap_list += "    )\n"
    
    if signals_out and signals_in:
        portmap_list += "    -- To DUT aka TB Outputs\n"
        portmap_list += "    port map(\n"
        for signal in signals_out:
            portmap_list += "    "+ signal[0] + " => " + signal[0] + ",\n"
        portmap_list += "    -- From DUT aka TB Inputs\n"
        for signal in signals_in:
            portmap_list += "    "+ signal[0] + " => " + signal[0]
            if signals_in[len(signals_in) - 1] == signal:
                portmap_list += "\n"
            else:
                portmap_list += ",\n"
        portmap_list += "    );\n"
    else:
        portmap_list = "There was no in- or output specified."
    return portmap_list

def main_process_vunit_tb (module_name):
    main_process_list =  "    --! @brief Main process of the "+ module_name +" testbench\n"
    main_process_list += "    --! @details Vunit loops through all the test cases present in the if statement inside the while loop\n"
    main_process_list += "    main : process\n"
    return main_process_list

def variables_vunit_tb (module_name):
    variables_list =  """        variable qtb_logger   : logger_t := get_logger("logging_timer_QTB:qtb_logger");   --! A logger framework provided by vunit\n"""
    variables_list += """        constant file_name    : string   := output_path(runner_cfg) & "../../../Testbench/results/"""+ module_name +"""Result.vhd"; --! Output path for the testbench results\n"""
    variables_list +=   "        file fptr             : text;             --! File variable to store text passed to the logger\n"
    variables_list +=   "        variable status       : file_open_status; --! Provides feedback to the logger if a file is open\n"
    return variables_list

def main_process_begin_tb():
    return "    begin\n"

def main_process_end_tb():
    process_end_list =  "        wait for 10 us;\n"
    process_end_list += "        file_close(fptr); -- Close the file\n"
    process_end_list += "        test_runner_cleanup(runner); -- End vunit script\n"
    process_end_list += "        wait;\n"
    process_end_list += "    end process;\n"
    return process_end_list

def open_report_file_vunit_tb():
    report_list =    "        -- Open the file and check if open\n"
    report_list +=   "        file_open(status, fptr, file_name, append_mode);\n"
    report_list += """        assert status = open_ok report "Failed to open file " & file_name severity failure;\n"""
    return report_list

def vunit_start_tb ():
    return "        test_runner_setup(runner, runner_cfg);  -- Entry point for the vunit application\n"

def testbench_vunit_while_tb ():
    return "        while test_suite loop --! Testbench loop\n"

def vunit_testcase_one_tb (module_name):
    test_one_list =    '            if run("'+ module_name +"""_test_one") then\n"""
    test_one_list +=   "                -- Create the result file header\n"
    test_one_list +=   "                --! \cond\n"
    test_one_list += """                print("--! \\addtogroup """+ module_name +"""_Module", fptr);\n"""
    test_one_list += """                print("--! @{" ,fptr);\n"""
    test_one_list += """                print("--! \\addtogroup """+ module_name +"""_Result",fptr);\n"""
    test_one_list += """                print("--! @{",fptr);\n"""
    test_one_list += """                print("--! @brief Testbench for the """+ module_name +""" module",fptr);\n"""
    test_one_list += """                print("--! @page """+ module_name +"""" ,fptr);\n"""
    test_one_list += """                print("--! @section HornControl Result of tests",fptr);\n"""
    test_one_list +=   "                --! \endcond\n"
    test_one_list += lib.blank_lines(1)
    test_one_list +=   "                wait for 1 us;\n"
    test_one_list += """                info("Test "& running_test_case &" - START");\n"""
    test_one_list += """                test_header(running_test_case,\n"""
    test_one_list += """                            "Lorem ipsum dolor sit amet.",\n""" 
    test_one_list += """                            "Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris.",\n"""
    test_one_list += """                            "DHHLR_TBD","", "", "", "");\n"""
    test_one_list += lib.blank_lines(1)
    test_one_list +=   "                clock_go <= '1';\n"
    test_one_list +=   "                wait until rising_edge(Clock);\n"
    test_one_list += lib.blank_lines(3)
    test_one_list +=   "                wait for 1 sec;\n"
    test_one_list += """                info("Test "& running_test_case &" - DONE");\n"""
    return test_one_list

def vunit_testcase_two_tb (module_name):
    test_two_list =    '            elsif run("'+ module_name +"""_test_two") then\n"""
    test_two_list +=   "                wait for 1 us;\n"
    test_two_list += """                info("Test "& running_test_case &" - START");\n"""
    test_two_list += """                test_header(running_test_case,\n"""
    test_two_list += """                            "Lorem ipsum dolor sit amet.",\n""" 
    test_two_list += """                            "Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris.",\n"""
    test_two_list += """                            "DHHLR_TBD","", "", "", "");\n"""
    test_two_list += lib.blank_lines(1)
    test_two_list +=   "                clock_go <= '1';\n"
    test_two_list +=   "                wait until rising_edge(Clock);\n"
    test_two_list += lib.blank_lines(3)
    test_two_list +=   "                wait for 1 sec;\n"
    test_two_list += """                info("Test "& running_test_case &" - DONE");\n"""
    return test_two_list

def report_vhdl_footer_tb (module_name):
    footer_list =    "                -- Create the result file footer\n"
    footer_list += """                print("--! \\n \\n", fptr);\n"""
    footer_list += """                print("entity e_HornControlLog is ", fptr);\n"""
    footer_list += """                print("end e_HornControlLog;",fptr);\n"""
    footer_list += """                print("architecture a_HornControlLog of e_HornControlLog is",fptr);\n"""
    footer_list += """                print("begin",fptr);\n"""
    footer_list += """                print("end a_HornControlLog;",fptr);\n"""
    footer_list += """                print("--! @}",fptr);\n"""
    footer_list += """                print("--! @}",fptr);\n"""
    return footer_list

def close_loops_tb():
    close_list =  "            end if;\n"
    close_list += "            clock_go <= '0';\n"
    close_list += "        end loop;\n"
    return close_list

def basic_testcase():
    basic_test_list =  "    -- Start writing tests here!\n"
    basic_test_list += "    wait until rising_edge(Clock);\n"
    basic_test_list += "\n"
    basic_test_list =  "    testbench: process\n"
    basic_test_list += "    begin\n"
    basic_test_list += "        wait for 1 sec;\n"
    basic_test_list += "    end process;\n"
    return basic_test_list