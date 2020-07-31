import time
import json


class Training:
    def __init__(self, training):
        self.training = training

    def define_activity(activity, minutes, seconds):## Function to set the steps the the training and to set the time of each step
        global total_time
        valid_time = True
        while valid_time == True:
            time_activity = (minutes*60)+seconds ## Convertion in seconds because Python's sleep function works only with seconds
            try:
                time_activity = float(time_activity)
                if time_activity <=0:
                    print('Enter with a number greater than zero')
                valid_time = False
            except:
                print('Wrong format. Use just numbers and separete decimals with dot')
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
    time_min = input('For how many minutes? ')
    time_sec = input('For how many seconds? ')
    training = Training(gama)
    Training.define_activity(activity, time_min, time_sec)
    repeat = input('Want to add another activity? (Y/N)' ).lower()
    if repeat == 'n':
        valid_repeat = False
    else:
        pass

print(json.dumps(activities, indent=1)) ## Print a legible dict with all training steps and times
print('\n')
print('The training will have: '+str(total_time)+' seconds\n') ## Print the total time of the training

Training.start_training()

for key in activities:
    try:
        Training.start_activity()
    except:
        print('You finished the training! May the force be with you')















    
