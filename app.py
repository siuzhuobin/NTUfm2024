from flask import Flask, render_template, request
import google.generativeai as genai
import os
import markdown


model = genai.GenerativeModel('gemini-1.5-flash')

genai.configure(api_key=os.getenv("MAKERSUITE"))



app = Flask(__name__) # erm apparently this is some signing thingy, e.g. for  apps to access like video camera or whatever 

@app.route("/", methods=["GET","POST"])  # that @ is a deocrator - which makes the app.route run before the index function 
def index():
    return(render_template("index.html"))

@app.route("/prediction_DBS", methods=["GET","POST"])  
def prediction_DBS():
    return(render_template("prediction_DBS.html"))

'''
@app.route("/q1", methods=["GET","POST"])  
def q1():
    r = model.generate_content("How should i diversify my investment portfolio?")
    return(render_template("q1_reply.html",r=r.text))
'''

@app.route("/q<int:qn_no>", methods=["GET","POST"])  
def ans_qn(qn_no):
    if (qn_no == 2):
        q = request.form.get('q')
    elif (qn_no == 1):
        q = "How should I diversify my investment portfolio?"
    else:
        return
    
    r = model.generate_content(q)    
    r_html = markdown.markdown(r.text)
    return(render_template("q1_reply.html",r=r_html))


@app.route("/faq", methods=["GET","POST"])  
def faq():
    return(render_template("faq.html"))

if __name__ == "__main__": # apparently, this checks if the thingy is being run onto the cloud? 
    app.run()

# okiedokie lemme see if it's possible to deliberately break a GIT thingy haha
