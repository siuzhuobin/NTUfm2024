from flask import Flask, render_template, request

app = Flask(__name__) # erm apparently this is some signing thingy, e.g. for  apps to access like video camera or whatever 

@app.route("/", methods=["GET","POST"])  # that @ is a deocrator - which makes the app.route run before the index function 

def index():
    return(render_template("index.html"))

if __name__ == "__main__": # apparently, this checks if the thingy is being run onto the cloud? 
    app.run()
