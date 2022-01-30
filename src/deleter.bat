@echo off
title PASSWORD DELETE
@REM :back
set /p name=Delete Password of : 
python del.py %name% %*