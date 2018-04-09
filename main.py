from flask import Flask, request, render_template

app = Flask(__name__)

app.config['DEBUG'] = True

@app.route("/signup", methods=['POST'])
def signup():
    username = request.form['username']
    email = request.form['email']
    password = request.form['password']
    retype_password = request.form['retype_password']

    if len(username) < 3 or len(username) > 20 or ' ' in username:
        username_error = "Not a valid username"
        return render_template('signup.html', username=username, username_error = username_error, email = email)
    if email and (len(email) < 3 or len(email) > 20 or ' ' in email or email.count('@') != 1 or email.count('.') != 1):
        email_error = "Not a valid email"
        return render_template('signup.html', email = email, username = username, email_error = email_error)
    if len(password) < 3 or len(password) > 20 or ' ' in password:
        password_error = "Not a valid password"
        return render_template('signup.html', email = email, username = username, password_error = password_error)
    if retype_password != password:
        retype_password_error = "Passwords do not match"
        return render_template('signup.html', email = email, username = username, retype_password_error = retype_password_error)
        
    return render_template('signup-confirmation.html', username = username)

@app.route("/")
def index():
    return render_template('signup.html')

app.run()