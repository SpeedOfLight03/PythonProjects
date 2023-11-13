from datetime import datetime
from playsound import playsound

alarm_time = input("Enter the time of alarm to be set:HH:MM:SS\n")  #12:15:30 am
alarm_hour = alarm_time[0:2]
alarm_minute = alarm_time[3:5]
alarm_second = alarm_time[6:8]
alarm_period = alarm_time[9:11].lower()

while True:
    now = datetime.now()
    curr_hour = now.strftime("%I")
    curr_minute = now.strftime("%M")
    curr_second = now.strftime("%S")
    curr_period = now.strftime("%P").lower()

    if curr_hour == alarm_hour and curr_minute == alarm_minute and curr_second == alarm_second and curr_period == alarm_period:
        playsound('Python Projects/Alarm Clock/alarm.mp3')
        break



