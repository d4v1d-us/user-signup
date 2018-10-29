from flask import Flask, request, redirect, render_template
import cgi

app = Flask(__name__)

app.config['DEBUG'] = True      # displays runtime errors in the browser, too

@app.route("/add", methods=['POST'])
def add_user():
    # get the form values
    Username = request.form.get('Username')
    if Username == None:
        Username = ''

    Password = request.form.get('Password')
    Verify_Password = request.form.get('Verify_Password')

    Email = request.form.get('Email')
    if Email == None:
        Email = ''

    #check username
    if Username == '': 
        error = "Please enter a Username"
        return redirect("/?Username_error=" + error + "&Username=" + Username + "&Email=" + Email)

    if len(Username) > 20 or len(Username) < 3:
        error = "Username Length must be 3 to 20"
        return redirect("/?Username_error=" + error + "&Username=" + Username + "&Email=" + Email)

    if ' ' in Username: 
        error = "Username Cannot Contain a space "
        return redirect("/?Username_error=" + error + "&Username=" + Username + "&Email=" + Email)

    #check Password
    if Password == '': 
        error = "Please enter a Password"
        return redirect("/?Password_error=" + error + "&Username=" + Username + "&Email=" + Email)

    if len(Password) > 20 or len(Password) < 3:
        error = "Password Length must be 3 to 20"
        return redirect("/?Password_error=" + error + "&Username=" + Username + "&Email=" + Email)    

    if ' ' in Password: 
        error = "Password Cannot Contain a space "
        return redirect("/?Password_error=" + error + "&Username=" + Username + "&Email=" + Email)

    #check Verify_Password
    if Verify_Password != Password: 
        error = "Passwords do not Match!"
        return redirect("/?Password_error=" + error + "&Username=" + Username + "&Email=" + Email)    

    #check Email
    if Email != '':
        if len(Email) > 20 or len(Email) < 3:
            error = "Email Length must be 3 to 20"
            return redirect("/?Email_error=" + error + "&Username=" + Username + "&Email=" + Email)  

        if ' ' in Email: 
            error = "Email Cannot Contain a space "
            return redirect("/?Email_error=" + error + "&Username=" + Username + "&Email=" + Email) 

        check = '@'
        if Email.count(check) != 1 : 
            error = "Invalid Email Address "
            return redirect("/?Email_error=" + error + "&Username=" + Username + "&Email=" + Email)

        check = '.'
        if Email.count(check) != 1 : 
            error = "Invalid Email Address "
            return redirect("/?Email_error=" + error + "&Username=" + Username + "&Email=" + Email)

    return render_template('welcome.html', Username=Username)

@app.route("/")
def index():
    Username_error = request.args.get("Username_error")
    Username = request.args.get("Username")

    Password_error = request.args.get("Password_error")

    Email_error = request.args.get("Email_error")
    Email = request.args.get("Email")
    
    return render_template('index.html', \
    Username_error=Username_error and cgi.escape(Username_error, quote=True), \
    Username=Username and cgi.escape(Username, quote=True), \
    Password_error=Password_error and cgi.escape(Password_error, quote=True), \
    Email_error=Email_error and cgi.escape(Email_error, quote=True), \
    Email=Email and cgi.escape(Email, quote=True), \
    )
    
app.run()
