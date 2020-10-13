# Team Glasses -- *William Li, Benjamin Gallai, Jason Chan
# SoftDev -- Rona Ed.
# K10 -- Putting Little Pieces Together/Flask Intro/Send output of occupation chooser to webpage
# 2020-10-13

import random, csv

from flask import Flask
app = Flask(__name__) #create instance of class Flask

JobClass = {}
occupations = ""
with open("occupations.csv") as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    for row in csv_reader:
        JobClass[row[0]] = row[1]
        occupations += row[0] + "<br>"
JobClass.pop("Job Class")
occupations = occupations[13:-10]

@app.route("/")       #assign fxn to route
def jobGetter():
    retStr = """Team Glasses -- *Benjamin Gallai, Jason Chan, William Li <br>
SoftDev -- Rona Ed. <br>
K10 -- Putting Little Pieces Together/Flask Intro/Send output of occupation chooser to webpage <br>
2020-10-13"""

    retStr += "<br><br> Your Occupation: "

    x=random.uniform(0,float(JobClass["Total"]))
    for key, value in JobClass.items():
        x=x-float(value)
        if x<=0:
            retStr += key
            break
    retStr += "Invalid"

    retStr += "<br><br> All Occupations: "

    retStr += "<br><br>" + occupations

    return retStr

if __name__ == "__main__":  # true if this file NOT imported
    app.debug = True        # enable auto-reload upon code change
    app.run()
