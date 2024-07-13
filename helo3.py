from flask import Flask
app = Flask(__name__)

@app.route('/b')
def home():
    books = ["The kill", "1984", "Mockingbird", "The Catcher", "The Last Hunter"]
    return books

if __name__ == '__main__':
    app.run(debug=True)
