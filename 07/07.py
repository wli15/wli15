# Liam Kronman, William Li (Team WinLose)
# SoftDev
# K07 - Stl/O: Divine your Destiny (Occupation getter)
# 2020-10-01
import random, csv

def jobGetter(dict):
    x=random.uniform(0,float(dict["Total"]))
    for key, value in dict.items():
        x=x-float(value)
        if x<=0:
            return key
    return "Invalid"

if __name__ == "__main__":
    JobClass = {}
    with open("occupations.csv") as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        for row in csv_reader:
            JobClass[row[0]] = row[1]
    JobClass.pop("Job Class")
    print(jobGetter(JobClass))

