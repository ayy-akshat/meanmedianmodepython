from collections import Counter
import csv
import math


def mmm():
    with open("sampledata.csv", newline="") as file:
        d = csv.reader(file)
        data = list(d)[1::]

        mean = 0
        for i in data:
            mean += float(i[1])
        mean /= len(data)
        print("Mean height: " + str(mean))

        def check(a):
            return a[1]
        data.sort(key=check)
        median = 0
        if (len(data) % 2 == 1):
            index = math.floor(len(data) / 2)
            median = data[index]
        else:
            # l = len(data)
            median = (float(data[int(len(data) // 2)][1]) +
                      float(data[int(1 + (len(data) / 2))][1])) / 2
        print("Median height: " + str(median))

        meanDiffs = []
        for i in data:
            meanDiffs.append((mean - float(i[1]))**2)

        sd = sum(meanDiffs)
        sd /= len(meanDiffs) - 1
        sd = math.sqrt(sd)
        print("Standard deviation of height: " + str(sd))

        ranges = {}
        for i in data:
            r = math.floor(float(i[1])/10)*10
            if r in ranges.keys():
                ranges[r] += 1
            else:
                ranges[r] = 1
        
        mode = 0
        for i in ranges:
            if (i > mode):
                mode = i
        print("Mode range: " + str(mode) + "-" + str(mode + 10))
    


mmm()
