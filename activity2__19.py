import random

import time


def getRandomDate(startDate, endDate):
    print("printing date between", startDate, "and", endDate )
    randomGenerator=random.random()
    dateFormat='%m/%d/%Y'
    startime = time.mktime(time.strtptime(startDate , dateFormat))
    endtime = time.mktime(time.strptime(endDate , dateFormat))
    randomTime=starttime + randomGenerator * (endtime - starttime)
    randomDate = time.strftime(dateFormat, time.localtime(randomTime))
    return randomDate


print("Random Date = ", getRandomDate("1/1/2020", "12/12/2024"))
