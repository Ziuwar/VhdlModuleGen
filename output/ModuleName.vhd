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
    generic (target_time : integer := 5);
    generic (target_aquired : std_logic := 1);
    port(
        Clock : in std_logic;
        Reset_n : in std_logic;
        TimingPulse : in std_logic_vector [15 downto 0];
        WarningEnable_n : in std_logic_vector [11 downto 0];

        SirenOn : out std_logic;
        HornControl : out std_logic_vector [9 downto 0];
        MuteActive : out std_logic_vector [3 downto 0]
    );
end entity e_ModuleName;

architecture a_ModuleName of e_ModuleName is
begin










end architecture a_ModuleName;
--! @}
--! @}
