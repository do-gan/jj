from flask import Flask,jsonify
app=Flask(__name__)
a=[3,4,5,6]
b=[5,6,7,8]
c=[7,8,9,10]
d=[a,b,c,3]
@app.route('/userlist/<int:e>/<int:f>/<int:g>/<int:h>')
def userlist(e,f,g,h):
    return jsonify({'userlist':[e,f,g,h]})
if __name__=='__main__':
    app.run(debug=True)
