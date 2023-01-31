import subprocess

command = 'cd /d "C:\Program Files (x86)\Microsoft Visual Studio\Shared" & mklink /H trl my_file.py'
subprocess.call(command, shell=True)