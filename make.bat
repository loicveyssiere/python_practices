@echo off
:: =============================================================================
:: Python environment creation on Windows
:: =============================================================================

:: Variables to modify ---------------------------------------------------------
set VIRTUALENV=.env
set PYTHON=D:\UsersPrograms\loicveyssiere\AppData\Local\Programs\Python\Python36\python.exe

:: Force workspace location
cd %~dp0

:: Main switch case by arguments -----------------------------------------------
set CMD=%~1

echo %~dp0

IF "%CMD%"=="" goto message
IF "%CMD%"=="env" goto env
IF "%CMD%"=="lint" goto lint
IF "%CMD%"=="test" goto test
goto message

:: Methods ---------------------------------------------------------------------
:message
    echo "Please run this script using env, lint or test"
goto :eof

:env
    :: Check if env already exists
    if exist %VIRTUALENV% (
        echo Environment already exist
    ) else (
        echo Start environment creation
        :: env creation
        %PYTHON% -m venv %VIRTUALENV%
    )

    :: Source environment before install
    CALL .\%VIRTUALENV%\Scripts\activate.bat

    :: Install packages
    pip install --default-timeout=100 -r requirements.txt
    
    echo please run .\%VIRTUALENV%\Scripts\activate
goto :eof

:lint
echo "Not Implemented"
goto :eof

:test
echo "Not Implemented"
goto :eof

