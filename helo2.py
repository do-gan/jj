from flask import Flask
app=Flask(__name__)
@app.route('/password/<usname>/<passwd>')
def password (usname,passwd):
    if usname.strip() == "python" and passwd.strip() == "flask":
        return "Welcome to the python flask app"
    else:
        return "Invalid username or password"
if __name__=='__main__':
    app.run(debug=True)