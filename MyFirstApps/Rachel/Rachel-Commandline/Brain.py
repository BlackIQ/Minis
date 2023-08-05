# Libraries
from time import *
from math import *
import random
import requests
import datetime
from jdatetime import *

# Functions
def start():
    start_list = ['Welcome back Amir !', 'Hi Amir !', 'Hello Amir ! I missed U :)']
    print(start_list[random.randint(1, 2)])
    print('Today is : (', datetime.now().date().strftime("%Y , %m , %d"), ') Amir')

def hello():
    hello_list = ['Hello Amir !', 'Hi Darline !' , 'Hello my love !']
    print(hello_list[random.randint(1, 2)])

def bye():
    print('Goodbye Amir !')

def Goodnight():
    print('Have Good night Amir .')
    print('I hope you sleep good !')

def Sleep():
    print('Oh , OK !')
    print('Goodbye Pal !')

def problem():
    print('Oh sorry , Some thing went wrog :-(')
    print('Please try again !')

def About():
    print('Hi ! I Am Rachel your Assistant .')
    print('Now you are using Version 1.5.0 .')
    print('My developer is Amirhossein Mohammadi :)')
    print('But the main Idea is for Erfan Saberi .')
    print('OK , For see Command list Enter (help) <3 .')

def Help():
    print(' ----- { Commands List } -----')
    print(' ')
    print('List 1 - Start Commands')
    print('hello')
    print('hi')
    print('how are you ?')
    print('------------------------------')
    print('List - Doing Commands')
    print('stardate')
    print('date')
    print('what date is today ?')
    print('today ?')
    print('time')
    print('what time is it ?')
    print('now ?')
    print('------------------------------')
    print('List - End Commands')
    print('close')
    print('sleep')
    print('good night')
    print('bye')
    print('------------------------------')
    print('List - Information Commands')
    print('about')
    print('help')

def H_A_Y():
    print('At first you tell me how are you !')
    a = input('how are you today ? [ Give me a number between 1 , 10 ] ')
    if a == '1':
        a1 = input('Oh no why body ? ')
        print('OK , But I became upset man :( ')
    if a == '2':
        a2 = input('Really ? ')
        print('OK , I am sad too :( ')
    if a == '3':
        a3 = input('Why Pal ? ')
        print('Every time you are under 7 , I became sad .')
        print('Be happy :)')
    if a == '4':
        a4 = input('Did you had bad sleep ? ')
        print('I think that it is not a good reason !')
    if a == '5':
        a5 = input('Oh fuck ! why man ? ')
        print('it is not my business but I am a kind of Detective !')
    if a == '5':
        a6 = input('That is good ! But not soo good ! why ? ')
        print('When you are more than 5 , I feel good .')
    if a == '7':
        a7 = input('Hey body ! I am good to .')
    if a == '8':
        a8 = input()
    if a == '9':
        a9 = input('So So Good ! I dont know why should I do that but , Why ? ')
        print('That is perfectly good reason .')
    if a == '10':
        a10 = input('Awesome !!!! , Why ? ')
        print('I love number 10 , because you are 10 !')

def StarDate():
    YY = int(strftime("%Y", localtime())) - 1900
    MM = strftime("%m", localtime())
    DD = strftime("%d", localtime())
    print("Rachels Log , Stardate (", YY, MM, ".", DD, ") !")

def Date():
    ask_date = input('Stardate Or National Or Iran ? ')

    if 'stardate' in ask_date:
        StarDate()
    if 'national' in ask_date:
        n_date = strftime("%Y-%m-%d" , localtime())
        print('Today is : (' , n_date ,') Amir')
    if 'iran' in ask_date:
        i_date = datetime.now().date().strftime("%Y , %m , %d")
        print('Today is : (' , i_date ,') Amir')

def Time():
    ask_time = input('GMT Or Iran ? ')

    if 'gmt' in ask_time:
        gmt = strftime("%H : %M : %S" , gmtime())
        print('Now is : (' , gmt ,') Amir')
    if 'iran' in ask_time:
        i_time = datetime.now().time().strftime("%H : %M : %S")
        print('Now is : (' , i_time ,') Amir')