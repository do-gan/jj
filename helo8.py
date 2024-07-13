from flask import Flask,jsonify
app=Flask(__name__)
@app.route('/s')
def sort():
    a=[2,3,45,67,90]
    a.sort()
    return jsonify(sorted_numbers=a)
if __name__=='__main__':
    app.run(debug=True)