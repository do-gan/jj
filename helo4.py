from flask import Flask
import math
app=Flask(__name__)
@app.route('/f/<int:a>')
def fact(a):
    fac=math.factorial(a)
    return str(fac)
if __name__=='__main__':
    app.run(debug=True)