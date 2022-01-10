# Import Brain
from Brain import *

# Start
start()

while True:

    q = input('What can I do for you Amir ? ')

    # { ----- Start ----- } Commands
    if 'hello' in q:
        hello()
    elif 'hi' in q:
        hello()

    # { How are you ? } Command
    elif 'how are you' in q:
        H_A_Y()

    # { ----- Doing ----- } Commands
    # { StarDate } Command
    elif 'stardate' in q:
        StarDate()
    # { Date } Command
    elif 'date'in q:
        Date()
    elif 'what date is today' in q:
        Date()
    elif 'today' in q:
        Date()
    # { Time } Command
    elif 'time' in q:
        Time()
    elif 'what time is it' in q:
        Time()
    elif 'now' in q:
        Time()

    # { ----- Information ----- } Commands
    elif 'about' in q:
        About()
    elif 'help' in q:
        Help()

    # { ----- End  ----- } Commands
    # { Close } Command
    elif 'close' in q:
        bye()
        break
    # { Sleep ) Command
    elif 'sleep' in q:
        Sleep()
        break
    # { Good night } Command
    elif 'good night' in q:
        Goodnight()
        break
    # { Bye } Command
    elif 'bye' in q:
        bye()
        break

    # { ----- Problem ----- } Command
    else:
        problem()
        pass
input()
