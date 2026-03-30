import time
days = ["Sun", "Mon", "Tue", "Wed", "Thur", "Fri", "Sat"]

#Analyze screen time based on summary (total time, avg. time), max/min, 
#and screen time rating mode (low, moderate, high) 

def screentime_analyzer(screen_times, mode):
#calc total and average screentime based on user's inputs
    total = 0
    for i in screen_times:
        total += i
    average = round(total / len(screen_times))
    
    max_time = max(screen_times)
    min_time = min(screen_times)

    if mode == "synopsis" or mode == "Synopsis": 
        print(" ")
        print("Stats:- ")
        print("Total Time: " + str(total) + " hours")
        print("Avg Time: " + str(average) + " hours")
        print("Max Time Spent: " + str(max_time))
        print("Min Time Spent: " + str(min_time))
    elif mode == "me" or mode == "Me": 
        print(" ")
        print("What does your screentime say about you?:- ")
        print(" ")
        print("Avg Time: " + str(average))
        if average > 5:
            print("Your average is very high!")
            print("Digital Detox might be very benenficial for you.") 
            print("Consider spending some time away from your screens or even setting app limits.")
        elif average < 3:
            print("Your average is quite low.") 
            print("Make sure to follow the 20-20-20 rule every once in a while.")
            print("For every 20 mins of screentime, look 20 feet away for 20 seconds.")
        else:
            print("Your average is moderate.")
            print("Take a few breaks throughout the day that doesn't require using screens.")
            print("Set time limits of apps that takes up most of your screentime.")
    else:
        print("Invalid Choice. Please choose between 'synopsis' or 'me' ")
            
            
print("Hello and Welcome to the Screentime Analyzer!")
print(" ")
time.sleep(.7)
print("Enter you screentime for each day through the week.")
print("Make sure to round it to the nearest hour.")
print(" ")
screen_times = []
for day in days:
    time_input = int(input(day + ": "))
    screen_times.append(time_input)
print("Synopsis")
mode = input("Chose a mode between 'synopsis' or 'me': ")
screentime_analyzer(screen_times, mode)

ppr:
---
import time
days = ["Sun", "Mon", "Tue", "Wed", "Thur", "Fri", "Sat"]

def screentime_analyzer(screen_times, mode):
    total = 0
    for i in screen_times:
        total += i
    average = round(total / len(screen_times))
    
    max_time = max(screen_times)
    min_time = min(screen_times)

    if mode == "synopsis" or mode == "Synopsis": 
        print(" ")
        print("Stats:- ")
        print("Total Time: " + str(total) + " hours")
        print("Avg Time: " + str(average) + " hours")
        print("Max Time Spent: " + str(max_time))
        print("Min Time Spent: " + str(min_time))
    elif mode == "me" or mode == "Me": 
        print(" ")
        print("What does your screentime say about you?:- ")
        print(" ")
        print("Avg Time: " + str(average))
        if average > 5:
            print("Your average is very high!")
            print("Digital Detox might be very benenficial for you.") 
            print("Consider spending some time away from your screens or even setting app limits.")
        elif average < 3:
            print("Your average is quite low.") 
            print("Make sure to follow the 20-20-20 rule every once in a while.")
            print("For every 20 mins of screentime, look 20 feet away for 20 seconds.")
        else:
            print("Your average is moderate.")
            print("Take a few breaks throughout the day that doesn't require using screens.")
            print("Set time limits of apps that takes up most of your screentime.")
    else:
        print("Invalid Choice. Please choose between 'synopsis' or 'me' ")
            
            
print("Hello and Welcome to the Screentime Analyzer!")
print(" ")
time.sleep(.7)
print("Enter you screentime for each day through the week.")
print("Make sure to round it to the nearest hour.")
print(" ")
screen_times = []
for day in days:
    time_input = int(input(day + ": "))
    screen_times.append(time_input)
print("Synopsis")
mode = input("Chose a mode between 'synopsis' or 'me': ")

screentime_analyzer(screen_times, mode)

