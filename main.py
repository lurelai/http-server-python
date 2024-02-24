from flask import Flask, request
app = Flask(__name__)

@app.get('/')
def root():
    return "Welcome, admin. To sign-in send a json request to /admin"

@app.post('/admin')
def admin_login():
    form = dict(request.form)

    if not {'name', 'password'}.issubset( set(form.keys()) ):
        return 'You are missing some field, pls, try again with more slow'

    if form['name'] != 'addmin':
        return 'Invalid name'

    if form['password'] != 'myppa':
        return 'Invalid password'

    return 'Admin logged'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5050)

