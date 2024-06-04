from flask import Flask, render_template, redirect, url_for, request, session

app = Flask(__name__)
app.secret_key = 'your_secret_key'

# Dummy user data for illustration purposes
users = {
    "mathayo77": {
        "password": "salamanzisa1985",
        "email": "mathayo77@example.com"
    }
}

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        user = users.get(username)
        if user and user['password'] == password:
            session['username'] = username
            return redirect(url_for('docker_view'))
        else:
            return render_template('login.html', error="Invalid credentials")
    return render_template('login.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        email = request.form['email']
        password = request.form['password']
        if username in users:
            return render_template('register.html', error="Username already exists")
        users[username] = {"password": password, "email": email}
        return redirect(url_for('login'))
    return render_template('register.html')

@app.route('/docker_view')
def docker_view():
    if 'username' not in session:
        return redirect(url_for('login'))
    return render_template('docker_view.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/logout')
def logout():
    session.pop('username', None)
    return redirect(url_for('home'))

@app.route('/privacy')
def privacy():
    return render_template('privacy.html')

@app.route('/terms')
def terms():
    return render_template('terms.html')


if __name__ == '__main__':
    app.run(debug=True)

