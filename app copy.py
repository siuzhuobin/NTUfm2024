from flask import Flask, render_template, request
import google.generativeai as genai
import os
import markdown
import textblob

model = genai.GenerativeModel('gemini-1.5-flash')

genai.configure(api_key=os.getenv("MAKERSUITE"))



app = Flask(__name__) # erm apparently this is some signing thingy, e.g. for  apps to access like video camera or whatever 

@app.route("/", methods=["GET","POST"])  # that @ is a deocrator - which makes the app.route run before the index function 
def index():
    return(render_template("index.html"))

@app.route("/prediction_DBS", methods=["GET","POST"])  
def prediction_DBS():
    return(render_template("common_input.html", title='Share price prediction', p='Enter exchange rate', resp_page='/prediction_result_DBS'))


@app.route("/prediction_creditability", methods=["GET","POST"])
def pred_cred(): 
   return(render_template("common_input.html", title='Creditability prediction', p='Enter credit amount', resp_page='/prediction_cred_result'))


@app.route("/sentiment_analysis", methods=["GET","POST"]) 
def sentiment_analysis():
    return(render_template("sentiment_analysis.html"))

@app.route("/sentiment_analysis_result", methods=["GET","POST"]) 
def sentiment_analysis_result():
    q = request.form.get("q")
    return(render_template("common_result.html",r="The sentiment is " + str(textblob.TextBlob(q).sentiment)))



@app.route("/prediction_result_DBS", methods=["GET","POST"])  
def prediction_result_DBS():
    q = float(request.form.get("q"))
    r = (-50.6 * q) + 90.2
    return(render_template("common_result.html",r=f"The predicted share price is {r:.2f}"))

@app.route("/prediction_cred_result", methods=["GET","POST"])  
def pred_cred_results():
    q = float(request.form.get("q"))
    r = 1.21012822 + -0.0001053*q
    s = "creditable"
    if (r < 0.5):
        s = "not "+s
    
    return(render_template("common_result.html",r=f"This dude  " + s + " siah."))



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

