@echo off
title PASSWORD UPD
@REM :back
set /p name=Update Password of : 
python upd.py %name% %*
echo %name% >> passwords.txt