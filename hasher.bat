@echo off 
title PASSWORD GEN
set /p name=Set password for : 
echo %name% >> passwords.txt
@REM set "chars=ABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!@#$%^&*(),./;[]\-<>?:"{}+_"
@REM call :count chars sz
@REM set sz=%sz%
@REM :count
@REM setlocal enabledelayedexpansion

@REM :count_Loop
@REM    if not "!%1:~%len%!"=="" set /A len+=1 & goto :count_Loop
@REM (endlocal & set %2=%len%)

@REM set "pass="
@REM for /L %%j in (1,1,32) do (
@REM call :make_pass 
@REM )
@REM echo your new password for %name% is %pass%
@REM setx %name% "%pass%"
@REM exit /b
@REM :make_pass
@REM setlocal enabledelayedexpansion
@REM set /a i=%random% %%sz
@REM set b=!chars:~%i%,1!
@REM (endlocal & if "%pass%"=="" (set "pass=%b%") else (set "pass=%pass%%b%"))


