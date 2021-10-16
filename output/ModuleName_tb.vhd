-----------------------------------------------------------------
--! @file	ModuleName.vhd
--! @brief	Testbench for the module ModuleName.vhd

--! @copyright 2021 Avionik Straubing Entwicklungs GmbH
--! @version Version 1.0, Platform: Quartus 20.8.0

--! | Attribute | Value |
--! | :-- | :-- |
--! | Subversion revision | $Rev:$ |
--! | Time of last change | $Date:$ |
--! | Author(s) | @author Andreas Schroeder |
-----------------------------------------------------------------

-- Import vunit lib
library vunit_lib;
use vunit_lib.print_pkg.all;
use vunit_lib.log_levels_pkg.all;
use vunit_lib.logger_pkg.all;
use vunit_lib.log_handler_pkg.all;
use vunit_lib.run_pkg.all;
--! \cond
context vunit_lib.vunit_context;
--! \endcond
library ieee;
use ieee.std_logic_1164.all;
use ieee.std_logic_arith.all;
use ieee.numeric_std.all;
use ieee.std_logic_unsigned.ALL;
use std.textio.all;

--! \addtogroup ModuleName_Module
--! @{
--! \addtogroup ModuleName_Testbench
--! @{

--! @brief Test of the ModuleName logic module.
--! @details All test signal generation and result analysis is done here.
entity e_ModuleNameQualification_TB is
    generic (runner_cfg : string := runner_cfg_default);
    port(
        trigger : out std_logic := '0' --! Trigger is set when test evaluation timing is required
        );
end entity e_ModuleNameQualification_TB;

architecture a_ModuleNameQualification_TB of e_ModuleNameQualification_TB is
     -- Testbench Outputs
    signal Clock : in std_logic;
    signal Reset_n : in std_logic;
    signal TimingPulse : in std_logic_vector (15 downto 0);
    signal WarningEnable_n : in std_logic_vector (11 downto 0);

     -- Testbench Inputs
    signal SirenOn : std_logic;
    signal HornControl : std_logic_vector (9 downto 0);
    signal MuteActive : std_logic_vector (3 downto 0);

begin
   --! @brief DUT instantiation
   --! @details Instantiation of the DUT
   i_DUT : entity work.e_ModuleName(a_ModuleName)
    generic map(
    target_time => 5,
    target_aquired => 1
    )
    -- To DUT aka TB Outputs
    port map(
    Clock => Clock,
    Reset_n => Reset_n,
    TimingPulse => TimingPulse,
    WarningEnable_n => WarningEnable_n,
    -- From DUT aka TB Inputs
    SirenOn => SirenOn,
    HornControl => HornControl,
    MuteActive => MuteActive
    );

    --! @brief Main process of the ModuleName testbench
    --! @details Vunit loops through all the test cases present in the if statement inside the while loop
    main : process

        variable qtb_logger : logger_t := get_logger("logging_timer_QTB:qtb_logger");   --! A logger framework provided by vunit
        constant file_name  : string   := output_path(runner_cfg) & "../../../results/ModuleNameResult.vhd"; --! Output path for the testbench results
        file fptr           : text;             --! File variable to store text passed to the logger
        variable status     : file_open_status; --! Provides feedback to the logger if a file is open

        --! Bit checker customization to write pass/fail message in the logfile
        procedure check_equal_bit (
            constant got         : std_logic;
            constant expected    : std_logic;
            constant message     : string 
        ) is
        begin
            if (got = expected) then
                check_equal(got,expected,message);
                print("--! "& message &": \b PASS \n", fptr);
            else
                print("--! The check reported \b FAIL! \n", fptr);
                check_equal(got,expected,message);
            end if;
        end procedure check_equal_bit;

        --! Time checker customization to write pass/fail message in the logfile
        procedure check_equal_time (
            constant got         : time;
            constant expected    : time;
            constant message     : string 
        ) is
        begin
            if (got = expected) then
                check_equal(got,expected,message);
                print("--! "& message &": \b PASS \n", fptr);
            else
                print("--! The check reported \b FAIL! \n", fptr);
                check_equal(got,expected,message);
            end if;
        end procedure check_equal_time;

        --! Vector checker customization to write pass/fail message in the logfile
        procedure check_equal_vector (
            constant got         : std_logic_vector;
            constant expected    : std_logic_vector;
            constant message     : string 
        ) is
        begin
            if (got = expected) then
                check_equal(got,expected,message);
                print("--! "& message &": \b PASS \n", fptr);
            else
                print("--! The check reported \b FAIL! \n", fptr);
                check_equal(got,expected,message);
            end if;
        end procedure check_equal_vector;

        --! Integer checker customization to write pass/fail message in the logfile
        procedure check_equal_integer (
            constant got         : integer;
            constant expected    : integer;
            constant message     : string 
        ) is
        begin
            if (got = expected) then
                check_equal(got,expected,message);
                print("--! "& message &": \b PASS \n", fptr);
            else
                print("--! The check reported \b FAIL! \n", fptr);
                check_equal(got,expected,message);
            end if;
        end procedure check_equal_integer;

        --! Waits for a number of clocks (>= 1) and an additional time (>= 0 ns)
        procedure wait_clock_plus_time(
            constant number_of_clocks : integer;
            constant additional_time : time
        ) is
        begin
            for clocks in 1 to number_of_clocks loop
                wait until rising_edge(Clock);
            end loop;
            wait for additional_time;
        end procedure wait_clock_plus_time;

        --! Time calculations
        function time_diff_calc(
            constant p_time_one : time;
            constant p_time_two : time
        ) return time is
            variable time_difference : time;
        begin
            time_difference := p_time_two - p_time_one;
        return time_difference;
        end function time_diff_calc;

        --! Created the header for the tests
        procedure test_header (
            constant test_name      : string;
            constant short_desc     : string;
            constant test_desc      : string;
            constant req_id_one     : string := "";
            constant req_id_two     : string := "";
            constant req_id_three   : string := "";
            constant req_id_four    : string := "";
            constant req_id_five    : string := ""
        ) is
        begin
            print("--! <b>"& short_desc &" Test Name: "& test_name &"</b> \n", fptr);
            print("--! "& test_desc &" \n", fptr);
            print("--! \n", fptr);
            if (req_id_one'length > 0) then
                print("--! | Requirement(s) Covered |", fptr);
                print("--! | :-: |", fptr);
                if(req_id_one'length > 0) then
                    print("--! | Tests "& req_id_one &" |", fptr);
                    if (req_id_two'length > 0) then
                        print("--! | Tests "& req_id_two &" |", fptr);      end if;
                    if (req_id_three'length > 0) then
                        print("--! | Tests "& req_id_three &" |", fptr);    end if;
                    if (req_id_four'length > 0) then
                        print("--! | Tests "& req_id_four &" |", fptr);     end if;
                    if (req_id_five'length > 0) then
                        print("--! | Tests "& req_id_five &" |", fptr);     end if;
                end if;
            end if;
            print("--! \n", fptr);
            print("--! @image html  lib.e_ModuleNamequalification."& test_name &"_1.png "& test_name &"_1 width=1000", fptr);
            print("--! @image latex lib.e_ModuleNamequalification."& test_name &"_1.png "& test_name &"_1 width=16cm", fptr);
            print("--! \n", fptr);
        end procedure test_header;

    begin
        -- Open the file and check if open
        file_open(status, fptr, file_name, append_mode);
        assert status = open_ok report "Failed to open file " & file_name severity failure;

        test_runner_setup(runner, runner_cfg);  -- Entry point for the vunit application

        while test_suite loop --! Testbench loop
            if run("ModuleName_test_one") then
                -- Create the result file header
                --! \cond
                print("--! \addtogroup ModuleName_Module", fptr);
                print("--! @{" ,fptr);
                print("--! \addtogroup ModuleName_Result",fptr);
                print("--! @{",fptr);
                print("--! @brief Testbench for the ModuleName module",fptr);
                print("--! @page ModuleName" ,fptr);
                print("--! @section HornControl Result of tests",fptr);
                --! \endcond

                wait for 1 us;
                info("Test "& running_test_case &" - START");
                test_header(running_test_case,
                            "Lorem ipsum dolor sit amet.",
                            "Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris.",
                            "DHHLR_TBD","", "", "", "");

                wait until rising_edge(Clock);



                wait for 1 sec;
                info("Test "& running_test_case &" - DONE");

            elsif run("ModuleName_test_two") then
                wait for 1 us;
                info("Test "& running_test_case &" - START");
                test_header(running_test_case,
                            "Lorem ipsum dolor sit amet.",
                            "Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris.",
                            "DHHLR_TBD","", "", "", "");

                wait until rising_edge(Clock);



                wait for 1 sec;
                info("Test "& running_test_case &" - DONE");

                -- Create the result file footer
                print("--! \n \n", fptr);
                print("entity e_HornControlLog is ", fptr);
                print("end e_HornControlLog;",fptr);
                print("architecture a_HornControlLog of e_HornControlLog is",fptr);
                print("begin",fptr);
                print("end a_HornControlLog;",fptr);
                print("--! @}",fptr);
                print("--! @}",fptr);

            end if;
            clock_go <= '0';
        end loop;
        wait for 10 us;
        file_close(fptr); -- Close the file
        test_runner_cleanup(runner); -- End vunit script
        wait;
    end process;

clk: process
begin
    Clock <= '1';
    wait for (clock_period / 2);
    Clock <= '0';
    wait for (clock_period / 2);
end process;

end architecture a_ModuleNameQualification_TB;
--! @}
--! @}
