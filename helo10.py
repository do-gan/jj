from flask import Flask

app=Flask(__name__)
@app.route('/m/<int:e>/<int:f>/<int:g>/<int:h>')
def userlist(e,f,g,h):
    mm=max([e,f,g,h])
    return str(mm)+" is the max number"


if __name__=='__main__':
    app.run(debug=True)