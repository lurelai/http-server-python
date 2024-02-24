from flask import Flask, request
app = Flask(__name__)

@app.get('/')
def root():
    return "Welcome, admin. To sign-in send a json request to /admin"

@app.post('/admin')
def admin_login():
    data = request.get_json()

    if not {'name', 'password'}.issubset( set(data.keys()) ):
        return 'You are missing some field, pls, try again, but more slow'

    if data['name'] != 'addmin':
        return 'Invalid name'

    if data['password'] != 'myppa':
        return 'Invalid password'

    return 'Admin logged'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5050)

