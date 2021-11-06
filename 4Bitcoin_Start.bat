@Echo Off
@title Mizogg 4Bitcoin.py
@SET var=%cd%
@cd %var%
@cls
@SETLOCAL EnableDelayedExpansion
@for /F "tokens=1,2 delims=#" %%a in ('"prompt #$H#$E# & echo on & for %%b in (1) do     rem"') do (
@  set "DEL=%%a"
)
color 0A
@echo         .                                                                                .
@echo          .yNNms`                                                                  .ymNmy.
@echo          NMMMMMh                                                                  dMMMMMm
@echo          sMMMMMo                                                                  sMMMMMo
@echo           ./+:-yh:                          ``````````                          :hy-:+/` 
@echo                 :dm+`                      dMMMMMMMMMMh                      `+md-       
@echo                   +NNs.                   -MMMMMMMMMMMM.                   -sNm/         
@echo                    `sMMh-    `.`          oMMMMMMMMMMMM/          `.     -dMNo           
@echo                      .y/   `sMMNy-     `-/dMMMMMMMMMMMMd/-      :yMMNo`   /s.            
@echo                          .sMMMMMMMm+/sdMMMMMMMMMMMMMMMMMMMMds:omMMMMMMNs`                
@echo                        .sMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMNs`              
@echo                       .MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMN`             
@echo                        +NMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMN/              
@echo                         `yMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMy`               
@echo                           yMMMMMMMNhhmMMMMMMMMMMMMMMMMMMMMMMmhhNMMMMMMMs                 
@echo                          +MMMMNosh/  -hy+mMMMMMMMMMMMMMMd+hh-  +dssNMMMM/                
@echo                         -MMMMM+   :++:`  :MMMMMMMMMMMMMN-  `/++-   oMMMMN.               
@echo                   --:/+omMMMNy/ -mMMMMN/ -ymMMMMMMMMMMmy- +MMMMMm. +yNMMMdo+/:-.         
@echo                 `NMMMMMMMMMMh   sMMMMMMh   oMMMMMMMMMM+   mMMMMMM+   dMMMMMMMMMMm`       
@echo                 .MMMMMMMMMMMMNs `yMMMMd. +NMMMMMMMMMMMMN/ -dMMMMy` yNMMMMMMMMMMMM`       
@echo                 .MMMMMMMMMMMMM/   `--`   -MMMMMMMMMMMMMN.   `-.    oMMMMMMMMMMMMM`       
@echo                 .MMMMMMMMMMMMMMdmMs  /NNhMMMMMMMMMMMMMMMMhNN:  yMddMMMMMMMMMMMMMM`       
@echo                 .MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM`       
@echo                  ohdmNNMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMNNmdh+        
@echo                         ``````````````````````````````````````````````````               
@echo                           :hhhhhhho                            shhhhhhh-                 
@echo                            oMMMMMMMm:                        /mMMMMMMM+                  
@echo                            /NMMMMMMMMd+`                  `+mMMMMMMMMN:                  
@echo                          .hMMMMMMMMMMMMMdo:`          .:odMMMMMMMMMMMMMh.                
@echo                         oMMMMMMMMMMMMMMMMMMMNmhhyyhdmNMMMMMMMMMMMMMMMMMMN+               
@echo                         -hMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMh-               
@echo                           -hMMMMMNs-.+ymMMMMMMMMMMMMMMMMMMmy/.-yNMMMMMy-                 
@echo                             -hMh/       `-/hMMMMMMMMMMy/-`      `+dMy.                   
@echo                                            :MMMMMMMMMM-                                  
@echo                                            `MMMMMMMMMN                                   
@echo                                             dMMMMMMMMh                                   
@echo . 
@call :colorEcho 07 ~~~~~~~~~~~~~~~~~~Bitcoin~Address~List~Loading~Please~Wait~~~~~~~~~~~~~~~~~~
@echo.
@call :colorEcho 03 ~~~~~~~~~Mizogg~~~~~~~~~~~~Mizogg~~~~~~~~~~~~Mizogg~~~~~~~~~~~~Mizogg~~~~~~~~~Mizogg~~~~~~
@echo.
@call :colorEcho 04 Mizogg~~~~~~~~~~~~Mizogg~~~~~~~~~~~~Mizogg~~~~~~~~~~~~Mizogg~~~~~~~~~~~~Mizogg~~~~~~~~~~~~
@echo.
@call :colorEcho 07 ~~~~~~~~~~~~~~~~~~Bitcoin~Address~List~Loading~Please~Wait~~~~~~~~~~~~~~~~~~
@echo.
@call :colorEcho 05 ~~~~~~~~~Mizogg~~~~~~~~~~~~Mizogg~~~~~~~~~~~~Mizogg~~~~~~~~~~~~Mizogg~~~~~~~~~Mizogg~~~~~~
@echo.
@call :colorEcho 06 Mizogg~~~~~~~~~~~~Mizogg~~~~~~~~~~~~Mizogg~~~~~~~~~~~~Mizogg~~~~~~~~~~~~Mizogg~~~~~~~~~~~~
@echo.
@call :colorEcho 01 ~~~~~~~~~Mizogg~~~~~~~~~~~~Mizogg~~~~~~~~~~~~Mizogg~~~~~~~~~~~~Mizogg~~~~~~~~~Mizogg~~~~~~
@echo.
@call :colorEcho 07 ~~~~~~~~~~~~~~~~~~Bitcoin~Address~List~Loading~Please~Wait~~~~~~~~~~~~~~~~~~
@echo.
python3 4Bitcoin.py

goto :eof
:colorEcho
@echo off
<nul set /p ".=%DEL%" > "%~2"
findstr /v /a:%1 /R "^$" "%~2" nul
del "%~2" > nul 2>&1i
goto :eof