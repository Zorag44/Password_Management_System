@echo off
title PASSWORD RET
@REM :back
set /p name=Password of : 
python hmm.py %name% %*
@REM call ok.bat
@REM if not defined %name% (
@REM echo check again
@REM goto :back) else (
@REM setlocal enableDelayedExpansion
@REM echo password for %name% is 
@REM echo !%name%!|clip
@REM exit /b
@REM )
