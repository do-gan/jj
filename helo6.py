from flask import Flask
app=Flask(__name__)
@app.route('/reverse/<name>')
def reverse(name):
    return name[::-1]
if __name__=='__main__':
    app.run(debug=True)