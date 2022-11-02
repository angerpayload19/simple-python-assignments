
#author BERNABAS MELES
#PING AUTHOMATOION TOOL
import subprocess
import platform


def ping(host):
    param = '-n' if platform.system().lower() == 'windiws' else '-c'
    command = ['ping',param, '5', host]
    return subprocess.call(command)

host = input('Enter any site: ')
print(ping(host))    
