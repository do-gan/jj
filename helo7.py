from flask import Flask

app=Flask(__name__)
@app.route("/add/<int:a>/<int:b>")
def call(a,b):
    c=a+b
    return str(c)+" is the sum "

if __name__=='__main__':
    app.run(debug=True)