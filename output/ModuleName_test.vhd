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
    port(
        trigger : out std_logic := '0' --! Trigger is set when test evaluation timing is required
        );
end entity e_ModuleNameQualification_TB;

architecture a_ModuleNameQualification_TB of e_ModuleNameQualification_TB is
     -- Testbench Outputs
    signal Clock : in std_logic;
    signal Reset_n : in std_logic;
    signal TimingPulse : in std_logic_vector [15 downto 0];
    signal WarningEnable_n : in std_logic_vector [11 downto 0];

     -- Testbench Inputs
    signal SirenOn : std_logic;
    signal HornControl : std_logic_vector [9 downto 0];
    signal MuteActive : std_logic_vector [3 downto 0];

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


    -- Start writing tests here!
    wait until rising_edge(Clock);

    wait for 1 sec;

clk: process
begin
    Clock <= '1';
    wait for (clock_period / 2);
    Clock <= '0';
    wait for (clock_period / 2);
end process;

end architecture a_ModuleNameQualification_tb;
--! @}
--! @}
