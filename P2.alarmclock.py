'''
PROJECT 2 : Alarm Clock

An alarm clock is a clock with a function that can be activated 
to ring at a time set in advance, used to wake someone up. 
'''

#  C  O  D  E

from playsound import playsound
import datetime

alarm_time = input("Kindly, enter the alarm time in HH\MM\SS: ")

alarm_hour = alarm_time[0:2]
alarm_min = alarm_time[3:5]
alarm_sec = alarm_time[6:8]

print("Setting up alarm..")

while(True):
    now = datetime.datetime.now()
    current_hour = now.strftime("%H")
    current_min = now.strftime("%M")
    current_sec = now.strftime("%S")

    if (alarm_hour == current_hour):
        if (alarm_min == current_min):
            if (alarm_sec == current_sec):
                print("Time to wake up")
                playsound('Hen Sound.mp3')
                break
