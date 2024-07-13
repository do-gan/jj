from flask import Flask


app=Flask(__name__)
@app.route("/gen/<n>/<t>/<g>")
def call(n,t,g):
    if g=="male":
        return"MR "+n+" "+t+" you are "+g
    else:
        return"MRS "+n+" "+t+" you are "+g
    


if __name__=='__main__':
    app.run(debug=True)