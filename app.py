from flask import Flask, render_template, request

app = Flask(__name__) # erm apparently this is some signing thingy, e.g. for  apps to access like video camera or whatever 

@app.route("/", methods=["GET","POST"])  # that @ is a deocrator - which makes the app.route run before the index function 
def index():
    return(render_template("index.html"))

@app.route("/prediction_DBS", methods=["GET","POST"])  
def prediction_DBS():
    return(render_template("prediction_DBS.html"))

@app.route("/prediction_result_DBS", methods=["GET","POST"])  
def prediction_result_DBS():
    q = float(request.form.get("q"))
    r0 = -50.6*q+90.2
    r =f"{r0:.2f}"
    return(render_template("prediction_result_DBS.html",r=r))


if __name__ == "__main__": # apparently, this checks if the thingy is being run onto the cloud? 
    app.run()
