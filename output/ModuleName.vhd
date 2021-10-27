-----------------------------------------------------------------
--! @file	ModuleName.vhd
--! @brief	Implementation of the VHDL module ModuleName.vhd

--! @copyright 2021 Avionik Straubing Entwicklungs GmbH
--! @version Version 1.0, Platform: Quartus 20.8.0

--! | Attribute | Value |
--! | :-- | :-- |
--! | Subversion revision | $Rev:$ |
--! | Time of last change | $Date:$ |
--! | Author(s) | @author Andreas Schroeder |
-----------------------------------------------------------------

library ieee;
use ieee.std_logic_1164.all;
use ieee.std_logic_arith.all;
use ieee.numeric_std.all;
use ieee.std_logic_unsigned.all;
use ieee.math_real.all;

--! \addtogroup ModuleName_Module
--! @{
--! \addtogroup ModuleName_Implementation
--! @{

--! @brief Entity of the ModuleName logic module.
--! @details All test signal generation and result analysis is done here.
entity e_ModuleName is
    generic(
        max_level : integer := 42
    );
    port(
        input_level : in std_logic_vector (8 downto 0);

        output_level : out std_logic_vector (8 downto 0)
    );
end entity e_ModuleName;

architecture a_ModuleName of e_ModuleName is
begin










end architecture a_ModuleName;
--! @}
--! @}
