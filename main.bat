@echo off
cls
title PASSWORD 
:start
echo 1 to generate password
echo 2 to retrieve password
echo 3 to delete an existing password
echo 4 to update an existing password
echo anything else to exit
set /p choice=Your choice:
if %choice%==2 call retriever.bat & goto :start
if %choice%==1 call hasher.bat & goto :start
if %choice%==3 call deleter.bat & goto :start
if %choice%==4 call updater.bat & goto :start
if %choice% NEQ "2" exit /b
if %choice% NEQ "1" exit /b
if %choice% NEQ "3" exit /b
if %choice% NEQ "4" exit /b


