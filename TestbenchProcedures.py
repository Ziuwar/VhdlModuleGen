##################################################################################
# Company: 	    AS Eng / AVSR
# File: 		TestbenchProcedures.py
# Author: 		Andreas Schroeder
# Date: 		04.10.2021
#
# Description: 	Testbench procedures, mostly for VUNIT  
# Revision: 	R0.0.0 Not Tested
##################################################################################

import SourceText

def include_procedures ():
    procedures_list = check_equal_bit()
    return procedures_list

def check_equal_bit ():
    check_equal_bit_list = "        --! Bit checker customization to write pass/fail message in the logfile\n"
    check_equal_bit_list += "        procedure check_equal_bit (\n"
    check_equal_bit_list += "            constant got         : std_logic;\n"
    check_equal_bit_list += "            constant expected    : std_logic;\n"
    check_equal_bit_list += "            constant message     : string \n"
    check_equal_bit_list += "        ) is\n"
    check_equal_bit_list += "        begin\n"
    check_equal_bit_list += "            if (got = expected) then\n"
    check_equal_bit_list += "                check_equal(got,expected,message);\n"
    check_equal_bit_list += '                print("--! "& message &": \\b PASS \\n", fptr);\n'
    check_equal_bit_list += "            else\n"
    check_equal_bit_list += '                print("--! The check reported \\b FAIL! \\n", fptr);\n'
    check_equal_bit_list += "                check_equal(got,expected,message);\n"
    check_equal_bit_list += "            end if;\n"
    check_equal_bit_list += "        end procedure check_equal_bit;\n"
    return check_equal_bit_list

def clock_process():
    clock_process_list =  "clk: process\n"
    clock_process_list += "begin\n"
    clock_process_list += "    Clock <= '1';\n"
    clock_process_list += "    wait for (clock_period / 2);\n"
    clock_process_list += "    Clock <= '0';\n"
    clock_process_list += "    wait for (clock_period / 2);\n"
    clock_process_list += "end process;\n"
    return clock_process_list