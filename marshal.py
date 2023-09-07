import marshal
import requests
import os
import platform
import os
import webbrowser,pyfiglet
from sys import stdout
from time import sleep
os.system("clear")
black = f"""\033[1;33m[\033[1;36m ✷‿✷  \033[1;33m]\033[1;36m HELLO IN MY TOOL"""        
for char in black:
         stdout.write(char)
         stdout.flush()
         sleep(0.001/0.02)    
print("")
print("")   
zombie = f"""\033[1;33m[\033[1;36m ✷‿✷  \033[1;33m]\033[1;32m THIS IS MY CHANNEL »»» : https://t.me/black_code_22"""    
for char in zombie:
         stdout.write(char)
         stdout.flush()
         sleep(0.001/0.02)               
webbrowser.open('https://t.me/black_code_22')
print('')
def banner():
    print ('\033[1;31m          ▇▇▇◤▔▔▔▔▔▔▔◥▇▇▇         ')
    print('\033[1;31m          ▇▇▇▏◥▇◣┊◢▇◤▕▇▇▇       ')
    print ('\033[1;31m          ▇▇▇▏▃▆▅▎▅▆▃▕▇▇▇          ')
    print ('\033[1;31m          ▇▇▇▏╱▔▕▎▔▔╲▕▇▇▇           ')
    print ('\033[1;31m          ▇▇▇◣◣▃▅▎▅▃◢◢▇▇▇   \033[1;33m  CODE BY »»»» : \033[1;34mB̶L̶A̶C̶K̶ Z̶O̶M̶B̶I̶E̶')
    print ('\033[1;31m          ▇▇▇▇◣◥▅▅▅◤◢▇▇▇▇             ')
    print ('\033[1;31m          ▇▇▇▇▇◣╲▇╱◢▇▇▇▇▇      ')
    print ('\033[1;31m          ▇▇▇▇▇▇◣▇◢▇▇▇▇▇▇            ')
print("")
banner()
print("")
file=input("\033[1;32m\033[1;33m[\033[1;36m ◕‿◕ \033[1;33m] \033[1;35mENTER NAME SCRIPT »»» : \033[1;34m")
openfile=open(file,'r').read()
com=compile(openfile,' ','exec')
encrypt=marshal.dumps(com)
enc=open('enc_'+str(file),'w')
enc.write('import marshal\n')
enc.write('exec(marshal.loads('+repr(encrypt)+'))')
print('success encrypt | file save as enc_' + str(file))