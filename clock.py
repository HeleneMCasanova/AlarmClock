import datetime;
import time;
import webbrowser;

#get the set alarm time
def getAlarmTime():

    hour = input("Enter Hour: ");
    minute = input("Enter Minute: ");

    time = [hour, minute];

    return time;

#checking if the alarm time is equal to actual time
def isAlarmTimeEqual(alarmHour, alarmMinute, hour, minute):

    if((alarmHour == hour) & (alarmMinute == minute)):

        #print "\nyes";
        url = 'https://www.youtube.com/watch?v=3SFf1CLrGeI';
        webbrowser.get('chrome').open(url, new = 0);
        alarmHour = "";
        alarmMinute = "";
        exit(1);
    else:
        print "\nno";

    newTime = [alarmHour, alarmMinute];
    return newTime;

time = getAlarmTime();
while(1):
    curTime = datetime.datetime.now();
    print time;
    time = isAlarmTimeEqual(time[0], time[1], curTime.hour, curTime.minute);
