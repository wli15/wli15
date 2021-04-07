#Team EmptyCup - William Li, Pak Lau
#Soft Dev
#K19 -- A RESTful Journey Skyward - using API keys to display image from another site
#2021-04-06

from flask import Flask, render_template
import urllib
import json
app = Flask(__name__)

key = open("key_nasa.txt", "r")
fullLink= "https://api.nasa.gov/planetary/apod?api_key=" + key.read()
key.close()

@app.route("/",  methods=["GET"])
def root():
	u = urllib.urlopen(fullLink)
	response = u.read()
	data = json.loads(response)
	return render_template("main.html", pic = data['url'])

if __name__ == "__main__": #false if this file imported as module
    #enable debugging, auto-restarting of server when this file is modified
    app.debug = True
    app.run()