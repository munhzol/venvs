#!/usr/local/bin/python3

import sys
import subprocess
import os
import json

import applescript


# get current working path
current_path = os.getcwd()
script_path = os.path.dirname(__file__)

#get terminal parameters
arguments = sys.argv

def saveFile():
    f = open(f"{script_path}/venvs.txt", "w")
    f.write(json.dumps(venvs))
    f.close()

# try to load file data to json
try:
    with open(f'{script_path}/venvs.txt') as f:
        strJson = f.read()
        if strJson !='':
            venvs = json.loads(strJson)
        else:
            venvs = []
except IOError:
    venvs = []

# print(venvs[0]['path'])

# ***********************************
# $ venvs

# display list of your venvs
if len(arguments) == 1:
    if len(venvs)>0:
        for i in range(len(venvs)):
            print(f"{i}: {venvs[i]['name']}")
    else:
        print('- You have no venv. Create or add one. For help "$ venvs help".')
    quit()

cmd = arguments[1]

# ***********************************
# Create venv
# $ venvs create venvName

if cmd == 'create':
    if len(arguments)<3:
        print('- Error: Please insert name of your new venv. For help "$ venvs help".')
    else:
        new_venv = {
            'name': arguments[2],
            'path': current_path
        }

        venvs.append(new_venv)

        print('Please wait a minute...')
        subprocess.call(["python3","-m","venv",arguments[2]]) 

        saveFile()
        print('DONE!')
        quit()


# ***********************************
# Activate venv
# $ venvs activate venvID
#
# To get venvID run venvs

if cmd == 'activate':
    if len(arguments)<3:
        print('- Error: Please insert id of your venv to activate. For help "$ venvs help".')
    else:
        venvID = int(arguments[2])

        if venvID not in range(len(venvs)):
            print('- Error: Please check your venvID.')
            quit()

        script=f"""tell application "Terminal"
                    do script "source {venvs[venvID]['path']}/{venvs[venvID]['name']}/bin/activate"
                    activate
                end tell"""

        applescript.run(script)
        print('DONE!')
        quit()


# ***********************************
# Remove venv
# $ venvs remove venvID
#
# To get venvID run venvs

if cmd == 'remove':
    if len(arguments)<3:
        print('- Error: Please insert id of your venv to remove. For help "$ venvs help".')
    else:
        venvID = int(arguments[2])

        if venvID not in range(len(venvs)):
            print('- Error: Please check your venvID. For help "$ venvs help".')
            quit()

        del venvs[venvID]

        saveFile()
        print('DONE!')
    quit()


# ***********************************
# Add existing venv
# $ venvs add venvName venvPath
#   - in case venvPath empthy venvPath will set by current directory
#
# To get venvID run venvs

if cmd == 'add':
    if len(arguments)<3:
        print('- Error: Please insert name of your venv to add. For help "$ venvs help".')
    else:

        new_venv = {
            'name': arguments[2],
            'path': current_path
        }
        
        if len(arguments)>3:
            new_venv['path'] = arguments[3]

        # Checking your venv exists
        if os.path.isfile(f"{new_venv['path']}/{new_venv['name']}/pyvenv.cfg") == False:
            print('- Error: Please check your venv name to add. For help "$ venvs help".')
            quit()

        venvs.append(new_venv)
        saveFile() 
        print('Done!')

    quit()



# ***********************************
# Help
# $ venvs help or ?
#
# To get venvID run venvs

if cmd == 'help':
    print('- Python VenvS organaizer v0')
    print()
    print('---- List of VenvS')
    print('---- $ venvs')
    print('---- returns:')
    print('---- venvID venvName')
    print()
    
    print('---- Create a new Venv')
    print('---- $ venvs create venvName ')
    print()
    
    print('---- Add existing venv to your list')
    print('---- $ venvs add venvName')
    print('---- $ venvs add venvName venvPath ')
    print()

    print('---- Remove venv from your list')
    print('---- $ venvs remove venvID')
    print()

    print('---- Activate venv from your list')
    print('---- $ venvs activate venvID')
    print()

    quit()

    # Create shortcut in terminal
    # alias venvs="python3 /Users/*****/python_stack/python/venvs.py"

    # To make permament alias
    # vi ~/.bash_profile