from flask import Flask, request, redirect, render_template
import cgi

app = Flask(__name__)

app.config['DEBUG'] = True      # displays runtime errors in the browser, too

@app.route("/crossoff", methods=['POST'])
def crossoff_movie():
    crossed_off_movie = request.form['crossed-off-movie']

    if crossed_off_movie not in get_current_watchlist():
        # the user tried to cross off a movie that isn't in their list,
        # so we redirect back to the front page and tell them what went wrong
        error = "'{0}' is not in your Watchlist, so you can't cross it off!".format(crossed_off_movie)

        # redirect to homepage, and include error as a query parameter in the URL
        return redirect("/?error=" + error)

    # if we didn't redirect by now, then all is well
    return render_template('crossoff.html', crossed_off_movie=crossed_off_movie)

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
        if Email.count(check) > 1 : 
            error = "Invalid Email Address "
            return redirect("/?Email_error=" + error + "&Username=" + Username + "&Email=" + Email)

        check = '.'
        if Email.count(check) > 1 : 
            error = "Invalid Email Address "
            return redirect("/?Email_error=" + error + "&Username=" + Username + "&Email=" + Email)

    return render_template('welcome.html', Username=Username)


    # if (Username == '') or (new_movie.strip() == ""):
    #     error = "Please specify the movie you want to add."
    #     return redirect("/?error=" + error)

    # if the user wants to add a terrible movie, redirect and tell them the error
    # if new_movie in terrible_movies:
    #     error = "Trust me, you don't want to add '{0}' to your Watchlist".format(new_movie)
    #     return redirect("/?error=" + error)

    # 'escape' the user's input so that if they typed HTML, it doesn't mess up our site
    #new_movie_escaped = cgi.escape(new_movie, quote=True)

    # TODO:
    # Create a template called add-confirmation.html inside your /templates directory
    # Use that template to render the confirmation message instead of this temporary message below

    # return render_template('add-confirmation.html', new_movie=new_movie)

   # return "Confirmation Message Under Construction..."

# TODO:
# Modify the edit.html file to display the watchlist in an unordered list with bullets in front of each movie.
# Put the list between "Flicklist" and "Edit My Watchlist" under this heading: <h2>My Watchlist</h2>

# TODO:
# Change get_current_watchlist to return []. This simulates a user with an empty watchlist.
# Modify edit.html to make sense in such a situation:
#  First: Hide the <h2>My Watchlist</h2> and it's unordered list.
#  Second: Hide the crossoff form, since there are no movies to cross off. 
# Then you can change get_current_watchlist back to the list of hard-coded movies.

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
