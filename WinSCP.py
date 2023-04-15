# Define variables for reuse
setlocal

set "username=your_username"
set "password=your_password"
set "remote_server=remote-server.com"
set "remote_path=/remote/server/path/"
set "local_path=C:\path\to\local\file.txt"
set "log_path=C:\path\to\log.txt"

# Check if the file exists
if not exist "%local_path%" (
    echo Error: File "%local_path%" not found. >> "%log_path%"
    exit /b 1
)

# Connect to remote server
winscp.com /log="%log_path%" /command ^
    "open sftp://%username%:%password%@%remote_server%" ^
    "option transfer binary" ^
    "put ""%local_path%"" ""%remote_path%"";" ^
    "exit"

# Check if the transfer was successful
if %errorlevel% neq 0 (
    echo Error: Failed to transfer file "%local_path%" to "%remote_path%". >> "%log_path%"
    exit /b 1
)

# Disconnect from remote server
exit /b 0
