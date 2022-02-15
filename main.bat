:END_NORMAL
taskkill /IM FortniteClient-Win64-Shipping.exe /F

:ENDD_NORMAL
echo here

TASKLIST /NH | FIND /I "fortnite"
IF %ERRORLEVEL% equ 0 (
  GOTO END_NORMAL
) ELSE GOTO ENDD_NORMAL

goto ENDD_NORMAL