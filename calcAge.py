import time
import datetime

actualTime = datetime.datetime.now()
#actualTime = 2018

year = int(input("please input the year when you born: "))

def calculateAge(year):

    calculated = actualTime.year - year
    print("Your age is: ", calculated)

calculateAge(year)
