@echo off
SET mypath=%~dp0

set PATH=C:\Windows\system32
set PATH=%PATH%;C:\MinGW\bin
set PATH=%PATH%;C:\MinGW\libexec\gcc\mingw32\5.3.0
set PATH=%PATH%;D:\ProgramFiles\Vivado\2015.4\bin\unwrapped\win64.o
set PATH=%PATH%;D:\ProgramsFiles\Octave\Octave-4.0.3\bin
set PATH=%PATH%;C:\Users\Praca\AppData\Local\Programs\Git
set PATH=%PATH%;D:\Program Files\Vim\vim80
set PATH=%PATH%;D:\Program Files\JetBrains\PyCharm Community Edition 2016.2.3\bin
set PATH=%PATH%;D:\Program Files\MiKTeX 2.9\miktex\bin\x64\
set PATH=%PATH%;D:\Program Files\Python\Python27-64
set PATH=%PATH%;D:\Program Files\Python\Python27-64\Scripts
set PATH=%PATH%;D:\Program Files\Python\Python27-64\Lib\site-packages\PyQt4
set PATH=%PATH%;D:\Program Files\Python\Python27-64\Lib\site-packages\PyQt4\plugins\sqldrivers
set PATH=%PATH%;D:\Program Files\Python\Python35-64
set PATH=%PATH%;D:\Program Files\Python\Python35-64\Scripts
set PATH=%PATH%;C:\Program Files\MySQL\MySQL Server 5.6\bin
cd %mypath
cmd