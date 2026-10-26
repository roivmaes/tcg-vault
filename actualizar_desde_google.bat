@echo off
title Sincronizar Galeria TCG con Google Sheets
echo ========================================================
echo   SINCRONIZANDO CON GOOGLE SHEETS Y YGOPRODECK...
echo ========================================================
echo.
python "%~dp0sync.py"
echo.
echo Sincronizacion finalizada.
echo Puedes recargar tu navegador para ver los cambios.
pause
