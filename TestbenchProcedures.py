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
    procedures_list += SourceText.blank_lines(1)
    procedures_list += check_equal_time()
    procedures_list += SourceText.blank_lines(1)
    procedures_list += check_equal_vector()
    procedures_list += SourceText.blank_lines(1)
    procedures_list += check_equal_integer()
    return procedures_list

def check_equal_bit ():
    check_equal_bit_list =  "        --! Bit checker customization to write pass/fail message in the logfile\n"
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

def check_equal_time ():
    check_equal_time_list =  "        --! Time checker customization to write pass/fail message in the logfile\n"
    check_equal_time_list += "        procedure check_equal_time (\n"
    check_equal_time_list += "            constant got         : time;\n"
    check_equal_time_list += "            constant expected    : time;\n"
    check_equal_time_list += "            constant message     : string \n"
    check_equal_time_list += "        ) is\n"
    check_equal_time_list += "        begin\n"
    check_equal_time_list += "            if (got = expected) then\n"
    check_equal_time_list += "                check_equal(got,expected,message);\n"
    check_equal_time_list += '                print("--! "& message &": \\b PASS \\n", fptr);\n'
    check_equal_time_list += "            else\n"
    check_equal_time_list += '                print("--! The check reported \\b FAIL! \\n", fptr);\n'
    check_equal_time_list += "                check_equal(got,expected,message);\n"
    check_equal_time_list += "            end if;\n"
    check_equal_time_list += "        end procedure check_equal_time;\n"
    return check_equal_time_list

def check_equal_vector ():
    check_equal_vector_list =  "        --! Vector checker customization to write pass/fail message in the logfile\n"
    check_equal_vector_list += "        procedure check_equal_vector (\n"
    check_equal_vector_list += "            constant got         : std_logic_vector;\n"
    check_equal_vector_list += "            constant expected    : std_logic_vector;\n"
    check_equal_vector_list += "            constant message     : string \n"
    check_equal_vector_list += "        ) is\n"
    check_equal_vector_list += "        begin\n"
    check_equal_vector_list += "            if (got = expected) then\n"
    check_equal_vector_list += "                check_equal(got,expected,message);\n"
    check_equal_vector_list += '                print("--! "& message &": \\b PASS \\n", fptr);\n'
    check_equal_vector_list += "            else\n"
    check_equal_vector_list += '                print("--! The check reported \\b FAIL! \\n", fptr);\n'
    check_equal_vector_list += "                check_equal(got,expected,message);\n"
    check_equal_vector_list += "            end if;\n"
    check_equal_vector_list += "        end procedure check_equal_vector;\n"
    return check_equal_vector_list

def check_equal_integer ():
    check_equal_integer_list =  "        --! Integer checker customization to write pass/fail message in the logfile\n"
    check_equal_integer_list += "        procedure check_equal_integer (\n"
    check_equal_integer_list += "            constant got         : integer;\n"
    check_equal_integer_list += "            constant expected    : integer;\n"
    check_equal_integer_list += "            constant message     : string \n"
    check_equal_integer_list += "        ) is\n"
    check_equal_integer_list += "        begin\n"
    check_equal_integer_list += "            if (got = expected) then\n"
    check_equal_integer_list += "                check_equal(got,expected,message);\n"
    check_equal_integer_list += '                print("--! "& message &": \\b PASS \\n", fptr);\n'
    check_equal_integer_list += "            else\n"
    check_equal_integer_list += '                print("--! The check reported \\b FAIL! \\n", fptr);\n'
    check_equal_integer_list += "                check_equal(got,expected,message);\n"
    check_equal_integer_list += "            end if;\n"
    check_equal_integer_list += "        end procedure check_equal_integer;\n"
    return check_equal_integer_list







def clock_process():
    clock_process_list =  "clk: process\n"
    clock_process_list += "begin\n"
    clock_process_list += "    Clock <= '1';\n"
    clock_process_list += "    wait for (clock_period / 2);\n"
    clock_process_list += "    Clock <= '0';\n"
    clock_process_list += "    wait for (clock_period / 2);\n"
    clock_process_list += "end process;\n"
    return clock_process_list