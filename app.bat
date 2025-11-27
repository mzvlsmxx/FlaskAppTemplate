@echo off
setlocal

set "CONFIG_FILE=batch-config.ini"
if not exist "%CONFIG_FILE%" (
    echo APP_COMPOSE_FILE_PATH=>>batch-config.ini
    echo APP_CONTAINER_NAME=>>batch-config.ini
    echo DB_COMPOSE_FILE_PATH=>>batch-config.ini
    echo MYSQL_CONTAINER_NAME=>>batch-config.ini
    echo MYSQL_HOST=>>batch-config.ini
    echo MYSQL_PORT=>>batch-config.ini
    echo MYSQL_USER=>>batch-config.ini
    echo REDIS_CONTAINER_NAME=>>batch-config.ini
    echo Created new config file: batch-config.ini
    echo Fullfill the config file with values for the correct script execution
    pause
    exit /b
) else (
    for /f "tokens=1* delims==" %%a in ('findstr /v /b /c:"#" /c:" " "%CONFIG_FILE%"') do (
        set "%%a=%%b"
    )
)


echo 

:menu
echo.
echo +--------^< Whole App ^>---------+--------^< Database ^>----------+
echo ^| 1. Up detached and rebuild   ^| 9. Up detached               ^|
echo ^| 2. Up detached               ^| 10. ^Start                    ^|
echo ^| 3. ^Start                     ^| 11. Stop                     ^|
echo ^| 4. Stop                      ^| 12. Down                     ^|
echo ^| 5. Down                      ^| 13. Enter MySQL Shell        ^|
echo ^| 6. Enter App Bash            ^| 14. Enter Redis Shell        ^|
echo ^| 7. Show App Logs             ^| 15. Show MySQL Logs          ^|
echo ^| 8. Show All Logs             ^| 16. Show Redis Logs          ^|
echo +------------------------------+------------------------------+
echo ^|                                                             ^|
echo +--------------------^< 17. ^Status All ^>-----------------------+
echo ^|                                                             ^|
echo +-----------------------^< 0. ^Exit ^>---------------------------+
echo.
set /p choice="Choice (0-17) >> "

cls
if "%choice%"=="1" goto app_up_detached_rebuild
if "%choice%"=="2" goto app_up_detached
if "%choice%"=="3" goto app_start
if "%choice%"=="4" goto app_stop
if "%choice%"=="5" goto app_down
if "%choice%"=="6" goto app_shell
if "%choice%"=="7" goto app_logs
if "%choice%"=="8" goto app_logs_all
if "%choice%"=="9" goto db_up_detached
if "%choice%"=="10" goto db_start
if "%choice%"=="11" goto db_stop
if "%choice%"=="12" goto db_down
if "%choice%"=="13" goto mysql_shell
if "%choice%"=="14" goto redis_shell
if "%choice%"=="15" goto mysql_logs
if "%choice%"=="16" goto redis_logs
if "%choice%"=="17" goto status_all
if "%choice%"=="0" exit /b
goto menu

:app_up_detached
docker compose -f %APP_COMPOSE_FILE_PATH% up -d
pause
cls
goto status_all

:app_up_detached_rebuild
docker compose -f %APP_COMPOSE_FILE_PATH% up -d --build
docker image prune -f >nul
pause
cls
goto status_all

:app_start
docker compose -f %APP_COMPOSE_FILE_PATH% ^start
pause
cls
goto status_all

:app_stop
docker compose -f %APP_COMPOSE_FILE_PATH% stop
pause
cls
goto status_all

:app_down
docker compose -f %APP_COMPOSE_FILE_PATH% down
pause
cls
goto status_all

:app_shell
cls
docker exec -it %APP_CONTAINER_NAME% sh
exit /b

:app_logs
echo.
echo -------------------^< APP LOGS ^>-----------------------
docker logs %APP_CONTAINER_NAME% 2>nul
echo.
pause
cls
goto menu

:app_logs_all
echo.
echo -------------------^< APP LOGS ^>-----------------------
docker logs %APP_CONTAINER_NAME% 2>nul
echo.
pause
cls
echo.
echo ------------------^< REDIS LOGS ^>----------------------
docker logs %REDIS_CONTAINER_NAME% 2>nul
docker logs %REDIS_DETACHED_CONTAINER_NAME% 2>nul
echo.
pause
cls
echo.
echo ------------------^< MYSQL LOGS ^>----------------------
docker logs %MYSQL_CONTAINER_NAME% 2>nul
docker logs %MYSQL_DETACHED_CONTAINER_NAME% 2>nul
echo.
pause
cls
goto menu

:db_up_detached
docker compose -f %DB_COMPOSE_FILE_PATH% up -d
pause
cls
goto status_all

:db_start
docker compose -f %DB_COMPOSE_FILE_PATH% ^start
pause
cls
goto status_all

:db_stop
docker compose -f %DB_COMPOSE_FILE_PATH% stop
pause
cls
goto status_all

:db_down
docker compose -f %DB_COMPOSE_FILE_PATH% down
pause
cls
goto status_all

:mysql_shell
cls
docker exec -it %MYSQL_CONTAINER_NAME% mysql -h %MYSQL_HOST% -u %MYSQL_USER% --port %MYSQL_PORT% -p
exit /b

:redis_shell
cls
docker exec -it %REDIS_CONTAINER_NAME% redis-cli
exit /b

:mysql_logs
echo.
echo ------------------^< MYSQL LOGS ^>----------------------
docker logs %MYSQL_CONTAINER_NAME% 2>nul
docker logs %MYSQL_DETACHED_CONTAINER_NAME% 2>nul
echo.
pause
cls
goto menu

:redis_logs
echo.
echo ------------------^< REDIS LOGS ^>----------------------
docker logs %REDIS_CONTAINER_NAME% 2>nul
docker logs %REDIS_DETACHED_CONTAINER_NAME% 2>nul
echo.
pause
cls
goto menu

:status_all
echo.
echo --------------------^< IMAGES ^>------------------------
docker images
echo.
echo ------------------^< CONTAINERS ^>----------------------
docker ps -a
echo.
echo -------------------^< NETWORKS ^>-----------------------
docker network ls
echo.
pause
cls
goto menu

endlocal