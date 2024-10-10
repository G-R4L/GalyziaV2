@echo off
title Tools Menu
chcp 65001 >nul
color 0A

:main_menu
cls
echo.
echo ╔════════════════════════════════════════════════════╗
echo ║                     TOOLS MENU                     ║
echo ╚════════════════════════════════════════════════════╝
echo.
echo  ╭──────────────────────────────────────────────────╮
echo  │  1. PyHammer                                    │
echo  │  2. IP Tracker                                  │
echo  │  3. Port Scanner                                │
echo  │  4. Website Pinger                              │
echo  │  5. Back to Main Menu                           │
echo  ╰──────────────────────────────────────────────────╯
echo.
set /p input="Select a tool [1-5]: "

if /I %input% EQU 1 start pyhammer pyhammer
if /I %input% EQU 2 start lacakip IP Tracker
              echo Starting 
if /I %input% EQU 3 start portscanner Port Scanner
if /I %input% EQU 4 start websitepinger Website Pinger
if /I %input% EQU 5 start Galyzia Back to Main Menu

echo Menjalankan
pause
goto main_menu
