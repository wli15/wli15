# Clyde 'Thluffy' Sinclair
# SoftDev -- Rona Ed.
# Oct 2020 

from flask import Flask
app = Flask(__name__) #create instance of class Flask

@app.route("/")       #assign fxn to route
def hello_world():
    print("about to print __name__...")
    print(__name__)   #where will this go?
    return "No hablo queso!"

app.debug = True
app.run()

# debug mode was on and debugger was activated. There was a restart but we don't know what "stat" is. There is also a pin number. 
# In debugger mode, when there is a change in the script, the local host refreshes and the console says "detected change"