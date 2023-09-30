from flask import Flask, flash, render_template, request,redirect,url_for
app= Flask(__name__)
app.secret_key= 'some_secret'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login',methods=['GET','POST'])
def login():
    username= request.form['username']
    password= request.form['password']
    if username == 'admin' or password == 'secret':
        flash('You were successfully logged in')
        return redirect(url_for('dashboard'))
    else:
        flash('Invalid username/password combination')
        return redirect(url_for('index'))

@app.route('/dashboard')
def dashboard():
    return render_template('dashboard.html')

if __name__ == '__main__':
    app.run(debug=True)

