-----------------------------------------------------------------
--! @file	Eval.vhd
--! @brief	Implementation of the VHDL module Eval.vhd

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
use ieee.std_logic_unsigned.all;
use ieee.math_real.all;

--! \addtogroup Eval_Module
--! @{
--! \addtogroup Eval_Implementation
--! @{

--! @brief Entity of the Eval logic module.
--! @details All test signal generation and result analysis is done here.
entity e_Eval is
    generic(
        max_level : integer := 42
    );
    port(
        input_level : in std_logic_vector (8 downto 0);

        output_level : out std_logic_vector (8 downto 0)
    );
end entity e_Eval;

architecture a_Eval of e_Eval is
begin










end architecture a_Eval;
--! @}
--! @}
