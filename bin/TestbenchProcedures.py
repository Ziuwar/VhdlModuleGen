##################################################################################
# File: 		TestbenchProcedures.py
# Author: 		Ziuwar
# Date: 		04.10.2021
#
# Description: 	Testbench procedures, mostly for VUNIT  
# Revision: 	R0.0.0 Not Tested
##################################################################################

import bin as lib

def include_procedures (module_name):
    procedures_list =  check_equal_bit()
    procedures_list += lib.blank_lines(1)
    procedures_list += check_equal_time()
    procedures_list += lib.blank_lines(1)
    procedures_list += check_equal_vector()
    procedures_list += lib.blank_lines(1)
    procedures_list += check_equal_integer()
    procedures_list += lib.blank_lines(1)
    procedures_list += wait_clock_plus_time()
    procedures_list += lib.blank_lines(1)
    procedures_list += time_diff_calc()
    procedures_list += lib.blank_lines(1)
    procedures_list += test_header(module_name)
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

def wait_clock_plus_time():
    wait_clock_plus_time_list =  "        --! Waits for a number of clocks (>= 1) and an additional time (>= 0 ns)\n"
    wait_clock_plus_time_list += "        procedure wait_clock_plus_time(\n"
    wait_clock_plus_time_list += "            constant number_of_clocks : integer;\n"
    wait_clock_plus_time_list += "            constant additional_time : time\n"
    wait_clock_plus_time_list += "        ) is\n"
    wait_clock_plus_time_list += "        begin\n"
    wait_clock_plus_time_list += "            for clocks in 1 to number_of_clocks loop\n"
    wait_clock_plus_time_list += "                wait until rising_edge(Clock);\n"
    wait_clock_plus_time_list += "            end loop;\n"
    wait_clock_plus_time_list += "            wait for additional_time;\n"
    wait_clock_plus_time_list += "        end procedure wait_clock_plus_time;\n"
    return wait_clock_plus_time_list

def time_diff_calc():
    time_diff_calc_list =  "        --! Time calculations\n"
    time_diff_calc_list += "        function time_diff_calc(\n"
    time_diff_calc_list += "            constant p_time_one : time;\n"
    time_diff_calc_list += "            constant p_time_two : time\n"
    time_diff_calc_list += "        ) return time is\n"
    time_diff_calc_list += "            variable time_difference : time;\n"
    time_diff_calc_list += "        begin\n"
    time_diff_calc_list += "            time_difference := p_time_two - p_time_one;\n"
    time_diff_calc_list += "        return time_difference;\n"
    time_diff_calc_list += "        end function time_diff_calc;\n"
    return time_diff_calc_list

def test_header(module_name):
    test_header_list =    "        --! Created the header for the tests\n"
    test_header_list +=   "        procedure test_header (\n"
    test_header_list +=   "            constant test_name      : string;\n"
    test_header_list +=   "            constant short_desc     : string;\n"
    test_header_list +=   "            constant test_desc      : string;\n"
    test_header_list +=   '            constant req_id_one     : string := "";\n'
    test_header_list +=   '            constant req_id_two     : string := "";\n'
    test_header_list +=   '            constant req_id_three   : string := "";\n'
    test_header_list +=   '            constant req_id_four    : string := "";\n'
    test_header_list +=   '            constant req_id_five    : string := ""\n'
    test_header_list +=   "        ) is\n"
    test_header_list +=   "        begin\n"
    test_header_list += """            print("--! <b>"& short_desc &" Test Name: "& test_name &"</b> \\n", fptr);\n"""
    test_header_list += """            print("--! "& test_desc &" \\n", fptr);\n"""
    test_header_list += """            print("--! \\n", fptr);\n"""
    test_header_list += """            if (req_id_one'length > 0) then\n"""
    test_header_list += """                print("--! | Requirement(s) Covered |", fptr);\n"""
    test_header_list += """                print("--! | :-: |", fptr);\n"""
    test_header_list += """                if(req_id_one'length > 0) then\n"""
    test_header_list += """                    print("--! | Tests "& req_id_one &" |", fptr);\n"""
    test_header_list += """                    if (req_id_two'length > 0) then\n"""
    test_header_list += """                        print("--! | Tests "& req_id_two &" |", fptr);      end if;\n"""
    test_header_list += """                    if (req_id_three'length > 0) then\n"""
    test_header_list += """                        print("--! | Tests "& req_id_three &" |", fptr);    end if;\n"""
    test_header_list += """                    if (req_id_four'length > 0) then\n"""
    test_header_list += """                        print("--! | Tests "& req_id_four &" |", fptr);     end if;\n"""
    test_header_list += """                    if (req_id_five'length > 0) then\n"""
    test_header_list += """                        print("--! | Tests "& req_id_five &" |", fptr);     end if;\n"""
    test_header_list += """                end if;\n"""
    test_header_list += """            end if;\n"""
    test_header_list += """            print("--! \\n", fptr);\n"""
    test_header_list += """            print("--! @image html  lib.e_"""+ module_name +"""qualification."& test_name &"_1.png "& test_name &"_1 width=1000", fptr);\n"""
    test_header_list += """            print("--! @image latex lib.e_"""+ module_name +"""qualification."& test_name &"_1.png "& test_name &"_1 width=16cm", fptr);\n"""
    test_header_list += """            print("--! \\n", fptr);\n"""
    test_header_list +=   "        end procedure test_header;\n"
    return test_header_list

def clock_process():
    clock_process_list =  "clk: process\n"
    clock_process_list += "begin\n"
    clock_process_list += "    Clock <= '1';\n"
    clock_process_list += "    wait for (clock_period / 2);\n"
    clock_process_list += "    Clock <= '0';\n"
    clock_process_list += "    wait for (clock_period / 2);\n"
    clock_process_list += "end process;\n"
    return clock_process_list