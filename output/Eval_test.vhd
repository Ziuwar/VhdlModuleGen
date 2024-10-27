-----------------------------------------------------------------
--! @file	Eval.vhd
--! @brief	Testbench for the module Eval.vhd

--! @copyright 2021 
--! @version Version 1.0, Platform: Quartus 20.8.0

--! | Attribute | Value |
--! | :-- | :-- |
--! | Subversion revision | $Rev:$ |
--! | Time of last change | $Date:$ |
--! | Author(s) | @author Ziuwar |
-----------------------------------------------------------------

library ieee;
use ieee.std_logic_1164.all;
use ieee.std_logic_arith.all;
use ieee.numeric_std.all;
use ieee.std_logic_unsigned.ALL;
use std.textio.all;

--! \addtogroup Eval_Module
--! @{
--! \addtogroup Eval_Testbench
--! @{

--! @brief Test of the Eval logic module.
--! @details All test signal generation and result analysis is done here.
entity e_EvalQualification_TB is
    port(
        trigger : out std_logic := '0' --! Trigger is set when test evaluation timing is required
        );
end entity e_EvalQualification_TB;

architecture a_EvalQualification_TB of e_EvalQualification_TB is
    -- Testbench Outputs
    signal input_level : std_logic_vector (8 downto 0);

    -- Testbench Inputs
    signal output_level : std_logic_vector (8 downto 0);

    -- Testbench signals
    signal clock_go     : std_logic := '0';     --! Enables the clock generation
    signal clock_period : time := 125 ns;       --! Clock periode

begin
   --! @brief DUT instantiation
   --! @details Instantiation of the DUT
   i_DUT : entity work.e_Eval(a_Eval)
    generic map(
    max_level => 42
    )
    -- To DUT aka TB Outputs
    port map(
    input_level => input_level,
    -- From DUT aka TB Inputs
    output_level => output_level
    );


    testbench: process
    begin
        wait for 1 sec;
    end process;

clk: process
begin
    Clock <= '1';
    wait for (clock_period / 2);
    Clock <= '0';
    wait for (clock_period / 2);
end process;

end architecture a_EvalQualification_TB;
--! @}
--! @}
