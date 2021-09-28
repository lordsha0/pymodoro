#! /bin/python3
import time
import datetime as date
import subprocess

amountSeconds = 60
#amountTimeBreak = 10 * amountSeconds
#amountTimeWork = 20 * amountSeconds
amountTimeWork = amountSeconds
amountTimeBreak = amountSeconds

def setTimer(amountTime):
    global timeCurrent
    global timeBreak

    timeCurrent = date.datetime.now()
    timeBreak = timeCurrent + date.timedelta(0, amountTime)


def countTimer(amountTime):
    setTimer(amountTime)
    print("It is " + timeCurrent.strftime("%H:%M"))
    print("Next timer at " + timeBreak.strftime("%H:%M"))
    amountTimeLeft = amountTime
    while(amountTimeLeft != 0):
        minuteLeft = amountTimeLeft / 60
        print(str(minuteLeft) + " minutes left")
        amountTimeLeft = amountTimeLeft - 60
        time.sleep(60)


timeTracker = -1
while(True):
    if(timeTracker == -1):
        timeTracker = timeTracker * -1
        subprocess.call('notify-send "Time for a break!"', shell=True)
        countTimer(amountTimeBreak)
    else:
        timeTracker = timeTracker * -1
        subprocess.run('notify-send "Time to work!"', shell=True)
        countTimer(amountTimeWork)
