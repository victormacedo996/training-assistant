import time
import json


class Training:
    def __init__(self, training):
        self.training = training
        
    def define_activity(activity, hours, minutes, seconds):## Function to set the steps the the training and to set the time of each step
        global total_time
        time_activity =  (hours*3600) + (minutes * 60) + seconds ## Convertion in seconds because Python's sleep function works only with seconds
        activities[activity]= time_activity ## Add activities to a dictionary
        total_time += time_activity ## Add the training step to the total time

    def start_training():
        global activities, x, y
        dic_value = list(activities.values())[x] ## Dictionary operations
        dic_key = list(activities.keys())[y]
        input('Press Enter to start\n')
        
        print('Prepare to start training in')
        print(5)
        time.sleep(1)
        print(4)
        time.sleep(1)
        print(3)
        time.sleep(1)
        print(2)
        time.sleep(1)
        print(1)
        time.sleep(1)
        print('Start '+dic_key+' now!!!')
        x+=1
        y+=1

    def start_activity():
        global activities, x, y
        dic_value = list(activities.values())[x] ## Dictionary operations
        dic_key = list(activities.keys())[y]
        count_down = 5
        time.sleep(dic_value-count_down)
        print(5)
        time.sleep(1)
        print(4)
        time.sleep(1)
        print(3)
        time.sleep(1)
        print(2)
        time.sleep(1)
        print(1)
        time.sleep(1)
        print('Start '+dic_key+' now!!!')
        x+=1
        y+=1

## Variables
activities = {}
total_time = 0
x = 0
y = 0
gama= 0

print('Welcome to the training assistent v0.1\n')


## Inputs and loop
valid_repeat = True
while valid_repeat == True:
    activity = input ('What kind of training is this? ')

    valid_hour = False ## Validation of users input for hours
    while valid_hour == False:
        time_hours = input('How many hours this step will have? ')
        try:
            time_hours = float(time_hours)
            if time_hours < 0:
                print('The number of hours canot be less than 0')
            valid_hour = True
        except:
            print('Wrong format. Use just numbers and separete decimals with dot')

    valid_minutes = False## Validation of users input for minutes
    while valid_minutes == False:
        time_minutes = input('How many minutes this step will have? ')
        try:
            time_minutes = float(time_minutes)
            if time_minutes < 0:
                print('The number of minutes canot be less than 0')
            valid_minutes = True
        except:
            print('Wrong format. Use just numbers and separete decimals with dot')

    valid_seconds = False ## Validation of users input for seconds
    while valid_seconds == False:
        time_seconds = input('How many seconds this step will have? ')
        try:
            time_seconds = float(time_seconds)
            if time_seconds < 0:
                print('The number of seconds canot be less than 0')
            valid_seconds = True
        except:
            print('Wrong format. Use just numbers and separete decimals with dot')

    
    training = Training(gama) ## Just because without this the class wouldn't work 
    Training.define_activity(activity, time_hours, time_minutes, time_seconds)
    repeat = input('Want to add another activity? (Y/N)' ).lower()
    if repeat == 'n':
        valid_repeat = False
    else:
        pass





print(json.dumps(activities, indent=1)) ## Print a legible dict with all training steps and times
print('\n')
print('The training will have: '+ time.strftime('%H hours, %M minutes, %S seconds', time.gmtime(total_time))) ## Print the total time of the training

Training.start_training()

for key in activities:
    try:
        Training.start_activity()
    except:
        print('You finished the training! May the force be with you')
