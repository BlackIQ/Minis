# Libraries
from time import *
from math import *
import random
import os
import requests
import datetime
from jdatetime import *

# Functions
def start(self):
    start_list = ['Welcome back Amir !', 'Hi Amir !', 'Hello Amir ! I missed U :)']
    self.outputs.append(start_list[random.randint(0, 3)])
    self.outputs.append('Today is : (', datetime.now().date().strftime("%Y , %m , %d"), ') Amir')

def hello(self):
    hello_list = ['Hello Amir !', 'Hi Darlin\' !' , 'Hello my love !']
    self.outputs.append(hello_list[random.randint(0, 2)])

def bye(self):
    self.outputs.append('Goodbye Amir !')
    MainWindow.close()

def Goodnight(self):
    self.outputs.append('Have Good night Amir .')
    self.outputs.append('I hope you sleep well !')
    MainWindow.close()

def Sleep(self):
    self.outputs.append('Oh , OK !')
    self.outputs.append('Goodbye Pal !')
    MainWindow.close()

def problem(self):
    self.outputs.append('Oh sorry , Some thing went wrog :-(')
    self.outputs.append('Please try again !')

def About(self):
    self.outputs.append('          Hi ! I Am Rachel your Assistant')
    self.outputs.append('          Now you are using Version 1.5.0')
    self.outputs.append('       My developer is Amirhossein Mohammadi :)')
    self.outputs.append('        OK , For see Command list Enter (help)')

def Help(self):
    self.outputs.append('Commands List')
    self.outputs.append('List 1 - Start Commands')
    self.outputs.append('hello')
    self.outputs.append('hi')
    self.outputs.append('how are you ?')
    self.outputs.append('------------------------------')
    self.outputs.append('List - Doing Commands')
    self.outputs.append('stardate')
    self.outputs.append('date')
    self.outputs.append('what date is today ?')
    self.outputs.append('today ?')
    self.outputs.append('time')
    self.outputs.append('what time is it ?')
    self.outputs.append('now ?')
    self.outputs.append('------------------------------')
    self.outputs.append('List - End Commands')
    self.outputs.append('close')
    self.outputs.append('sleep')
    self.outputs.append('good night')
    self.outputs.append('bye')
    self.outputs.append('------------------------------')
    self.outputs.append('List - Information Commands')
    self.outputs.append('about')
    self.outputs.append('help')

def H_A_Y(self):
    self.outputs.append('At first you tell me how are you !')
    a = input('how are you today ? [ Give me a number between 1 , 10 ] ')
    if a == '1':
        a1 = input('Oh no why body ? ')
        self.outputs.append('OK , But I became upset man :( ')
    if a == '2':
        a2 = input('Really ? ')
        self.outputs.append('OK , I am sad too :( ')
    if a == '3':
        a3 = input('Why Pal ? ')
        self.outputs.append('Every time you are under 7 , I became sad .')
        self.outputs.append('Be happy :)')
    if a == '4':
        a4 = input('Did you had bad sleep ? ')
        self.outputs.append('I think that it is not a good reason !')
    if a == '5':
        a5 = input('Oh fuck ! why man ? ')
        self.outputs.append('it is not my business but I am a kind of Detective !')
    if a == '5':
        a6 = input('That is good ! But not soo good ! why ? ')
        self.outputs.append('When you are more than 5 , I feel good .')
    if a == '7':
        a7 = input('Hey body ! I am good to .')
    if a == '8':
        a8 = input()
    if a == '9':
        a9 = input('So So Good ! I dont know why should I do that but , Why ? ')
        self.outputs.append('That is perfectly good reason .')
    if a == '10':
        a10 = input('Awesome !!!! , Why ? ')
        self.outputs.append('I love number 10 , because you are 10 !')

def StarDate(self):
    YY = int(strftime("%Y", localtime())) - 1900
    MM = strftime("%m", localtime())
    DD = strftime("%d", localtime())
    self.outputs.append("Rachels Log , Stardate (", YY, MM, ".", DD, ") !")

def Date(self):
    ask_date = input('Stardate Or National Or Iran ? ')

    if 'stardate' in ask_date:
        StarDate()
    if 'national' in ask_date:
        n_date = strftime("%Y-%m-%d" , localtime())
        self.outputs.append('Today is : (' , n_date ,') Amir')
    if 'iran' in ask_date:
        i_date = datetime.now().date().strftime("%Y , %m , %d")
        self.outputs.append('Today is : (' , i_date ,') Amir')

def Time(self):
    ask_time = input('GMT Or Iran ? ')

    if 'gmt' in ask_time:
        gmt = strftime("%H : %M : %S" , gmtime())
        self.outputs.append('Now is : (' , gmt ,') Amir')
    if 'iran' in ask_time:
        i_time = datetime.now().time().strftime("%H : %M : %S")
        self.outputs.append('Now is : (' , i_time ,') Amir')

def shutdown(self):
    os.system("shutdown /s /t 0")
def reboot(self):
    os.system("shutdown /r /t 0")