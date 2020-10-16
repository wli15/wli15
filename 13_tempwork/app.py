# Team Goofy Gorillas - *William Li, Ryan Ma
# SoftDev
#K13 -- Template for Success - more template work
#2020-10-19

import random
from flask import Flask, render_template
app = Flask(__name__)


@app.route("/")
def home():
    return "head to /occupyflaskst!"

heading1 = "Team Goofy Gorillas"
heading2 = "featuring: Ryan Ma and William Li"

@app.route("/occupyflaskst")
def occupy():
    occupations = open("data/occupations.csv", "r")
    data = occupations.readlines()
    occupations.close()
    current_total = 0
    percent_dict = {}
    for i in range(1, len(data)-1):
        if data[i][0] == '"':
            data_set = data[i].split('",')
            title = data_set[0][1:]
        else:
            data_set = data[i].split(",")
            title = data_set[0]
        percent = float(data_set[1])
        percent_dict[round(percent + current_total, 1)] = title
        current_total = current_total + percent

    rand_num = random.randrange(0,998) / 10
    chosen = "Chosen Occupation: "
    for percent in percent_dict:
        if rand_num < percent:
            chosen += percent_dict[percent]
            break
    return render_template('tablified.html', title = "Occupations", heading1 = heading1, heading2 = heading2, chosen_occupation = chosen, dictionary = percent_dict)

if __name__ == "__main__":
    app.debug = True
    app.run()