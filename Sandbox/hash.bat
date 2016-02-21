@echo off
set /p UserInput= Enter File Name:
start python "C:\Users\Administrator\Desktop\Lab3Final\office2john.py" %UserInput%
timeout /t 3
for /f "delims=" %%x in (output.txt) do set Build=%%x
if exist C:\Users\Administrator\Desktop\Lab3Final\output.txt start "C:\Users\Administrator\Desktop\Lab3Final\oclHashcat64.exe"  -a 0 -m 9600 --username %Build% "D:\password_lists\skullsecurity-lists\skullsecurity-lists\rockyou.txt"