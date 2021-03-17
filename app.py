from flask import Flask, render_template, request, url_for, redirect, session

app=Flask(__name__)
app.secret_key = "hello"

@app.route("/") 
def homepage():
    return render_template("homepage.html")

@app.route("/signin",methods=["POST"]) #功能頁(登入)
def login(): #login
    account = request.form["account"]
    code = request.form["code"]
    if(account=="test" and code=="test"):
        session["account"]=account
        session.permanent=True
        return redirect("/member")
    else:
        return redirect("/error")

@app.route("/member")
def memberPage():
    if "account" in session:
        return render_template("/member.html")
    else:
        return redirect("/")

@app.route("/error")
def errorPage():
    return render_template("error.html")

@app.route("/logout") #功能頁(登出)
def logout():
    session.pop("account", None)
    return redirect("/")

app.run(port=3000)