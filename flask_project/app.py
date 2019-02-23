from flask import Flask, render_template, request, redirect, session, flash
from flask_bootstrap import Bootstrap
from flask_moment import Moment
from flask_pymongo import PyMongo
from datetime import datetime

app = Flask(__name__)
Bootstrap(app)
moment = Moment(app)
app.config['SECRET_KEY'] = 'Blah'
app.config['MONGO_URI'] = 'mongodb://localhost:27017/UserAccounts'
mongo = PyMongo(app)

# users = {}

@app.route('/', methods = ['POST', 'GET'])
def index():
    return render_template('registration.html', current_time = datetime.utcnow())

@app.route('/home', methods = ['POST', 'GET'])
def home():
    if request.method == 'GET':    
        if 'user' not in session:
            return redirect('/login')
    email = session['user']
    collection = mongo.db.AccountInformation
    a = collection.find_one({'email':email})
    first_name = a['first_name']
    flash('Successfully logged you in.')
    return render_template('home.html', current_time = datetime.utcnow(), first_name = first_name)

@app.route('/userprofile', methods = ['POST', 'GET'])
def profile_page():
    if request.method == 'GET':    
        if 'user' not in session:
            return redirect('/login')
    email = session['user']
    collection = mongo.db.AccountInformation
    a = collection.find_one({'email':email})
    first_name = a['first_name']
    flash('Contact us at blahblahblah@gmail.com!')
    return render_template('profile_page.html', current_time = datetime.utcnow(), first_name = first_name)

@app.route('/registeruser', methods = ['POST', 'GET'])
def register_user():
    first_name = request.form['first_name']
    last_name = request.form['last_name']
    email = request.form['email']
    password = request.form['password']
    create_time = datetime.utcnow()
    collection = mongo.db.AccountInformation
    a = collection.find_one({'email':email})
    if a != None and a["email"] == email:
        flash('You have already registered this email.')
        return redirect('/')
    # users[email] = {'first_name':first_name,'last_name':last_name,'email':email,'password':password, 'create_time' : create_time}
    collection = mongo.db.AccountInformation
    usersDetails = {'first_name' : first_name,'last_name':last_name,'email':email,'password':password, 'create_time' : create_time}
    collection.insert(usersDetails)
    return redirect('/login')
    
@app.route('/login', methods = ['POST', 'GET'])
def login():
    return render_template('login.html', current_time = datetime.utcnow())

@app.route('/loginuser', methods = ['POST', 'GET'])
def login_user():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        collection = mongo.db.AccountInformation
        a = collection.find_one({'email': email})
        if a == None:
            flash('Sorry, but your entries are incorrect.')
            return redirect('/login')
        elif a['password'] == password:
            session['user'] = email
            login_time = datetime.utcnow()
            # users[email]['login_time'] = login_time
            collection = mongo.db.AccountInformation
            a = collection.find_one({'email' : email})
            a['login_time'] = login_time
            collection.save(a)
            return redirect('/home')
        else:
            flash('Sorry, but your entries are incorrect.')
            return redirect('/login')
    else:
        return redirect('/login')

@app.route('/logout', methods = ['POST', 'GET'])
def logout():
    flash('Succesfully logged you out.')
    del session['user']
    return redirect("/login")

def error_page(e):
    return render_template('error.html', error=e)

app.register_error_handler(404, error_page)
app.register_error_handler(500, error_page)
app.register_error_handler(400, error_page)

if __name__ == '__main__':
    # app.run(host = '0.0.0.0', port = 5000, debug = True)
    app.run(port = 5001, debug = True, )
