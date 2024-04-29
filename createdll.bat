@echo off
SET main_dir=%~dp0
SET code=%main_dir%/advanced_input

gcc -shared -o %code%/inputExtention.dll -fPIC %code%/inputExtention.c
