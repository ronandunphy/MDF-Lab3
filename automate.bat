@echo off

set /p UserInput= Enter File Name:

start python "C:\Users\Administrator\Desktop\Lab3Final\office2john.py" %UserInput%

timeout /t 3

if exist C:\Users\Administrator\Desktop\Lab3Final\output.txt 

start 

cd C:\Users\Administrator\Desktop\Lab3Final\ 
oclHashcat64.exe -a 0 -m 9600 --username -o output.txt "C:\Users\Administrator\Desktop\Lab3Final\rockyou.txt"