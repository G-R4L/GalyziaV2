@echo off 
title Galyzia
chcp 65001 >nul
color 
:start
call :banner

:menu
for /f %%A in ('"prompt $H &echo on &for %%B in (1) do rem"') do set BS=%%A
echo.
echo [38;2;0;255;0m       ╔════════════════════════════════════════════════════╗[0m
echo [38;2;0;255;0m       ║                     MAIN MENU                     ║[0m
echo [38;2;0;255;0m       ║    Select an option to proceed:                   ║[0m
echo [38;2;0;255;0m       ╚════════════════════════════════════════════════════╝[0m
echo [38;2;0;255;0m       ╭──────────────────────────────────────────────────╮[0m
echo [38;2;0;255;0m       │  ① Tools                                       │[0m  
echo [38;2;0;255;0m       │  ② Putty                                       │[0m  
echo [38;2;0;255;0m       │  ③ Wireshark                                   │[0m  
echo [38;2;0;255;0m       │  ④ Metasploit                                  │[0m  
echo [38;2;0;255;0m       │  ⑤ Join My Discord                             │[0m  
echo [38;2;0;255;0m       ╰──────────────────────────────────────────────────╯[0m
echo.
set /p input=.%BS% [38;2;0;255;0m       Select an option [1-5]: [0m  
if /I %input% EQU 1 start Menu2 Tools
if /I %input% EQU 2 start Putty
if /I %input% EQU 3 start Wireshark
if /I %input% EQU 4 start https://www.metasploit.com/download Metasploit
if /I %input% EQU 5 start https://discord.com/invite/bEEFxSYxM2 Join Discord
cls
goto start

:banner
echo.
echo.
echo             [38;2;0;0;255m ██████╗  █████╗ ██╗  ██╗   ██╗[0m[38;2;128;0;128m███████╗██╗ █████╗ [0m
echo            [38;2;0;0;255m ██╔════╝ ██╔══██╗██║  ╚██╗ ██╔╝[0m[38;2;128;0;128m╚══███╔╝██║██╔══██╗[0m
echo            [38;2;0;0;255m ██║  ███╗███████║██║   ╚████╔╝[0m[38;2;128;0;128m   ███╔╝ ██║███████║[0m
echo            [38;2;0;0;255m ██║   ██║██╔══██║██║    ╚██╔╝[0m[38;2;128;0;128m   ███╔╝  ██║██╔══██║[0m
echo            [38;2;0;0;255m ╚██████╔╝██║  ██║███████╗██║   [0m[38;2;128;0;128m███████╗██║██║  ██║[0m
echo            [38;2;0;0;255m  ╚═════╝ ╚═╝  ╚═╝╚══════╝╚═╝   [0m[38;2;128;0;128m╚══════╝╚═╝╚═╝  ╚═╝[0m
echo.
echo [38;2;0;255;255m───────────────────────────────────────────────────────────────[0m
echo [38;2;0;255;255m  Tools ini merupakan uji coba saja.                         [0m
echo [38;2;0;255;255m  Made By: Elc                                               [0m
echo [38;2;0;255;255m───────────────────────────────────────────────────────────────[0m
echo.
