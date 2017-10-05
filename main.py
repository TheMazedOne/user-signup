from flask import Flask, request, redirect, render_template,flash
import cgi

app = Flask(__name__)
app.config['DEBUD'] = True

@app.route("/login" , methods=['GET','POST'])
def login():
    username = request.form['username']
    password = request.form['password']
    verify = request.form['verify']
    email = request.form['email']
    check = int(0)
    error1=""
    error2=""
    error3=""
    error4=""
    special = 2
    if len(username) < 3 or len(username) > 20:
        error1 = "Invalid Username"  
        check +=1
    for letters in username:
        if letters == " ":
            error1 = "Invalid Username"
            check +=1 

                    
    if len(password) < 3:
        error2 = "Invalid Password"   
        check +=1   
    if verify != password:
        error3 = "Passwords do not match"
        check +=1
    if len(email)>0:
        for char in email:
            if char == " ":
                error4="Invalid Email"
                check+=1
            if char == "@":
                special -=1
            if char == ".":
                special -=1
            elif special > 2:
                error4="Invalid Email"
                check +=1
        if len(email) < 3 or len(email) > 20:
                error4="Invalid Email"
                check +=1
    if check >= 1:
        return render_template('edit.html',error1=error1, error2=error2,error3=error3,error4=error4, 
    username=username, email=email)
    else:
        return render_template('welcome.html' , username = username)

@app.route("/")
def index():
    encoded_error = request.args.get("error")
    return render_template('edit.html',error=encoded_error and cgi.escape(encoded_error, quote=True))
app.run()