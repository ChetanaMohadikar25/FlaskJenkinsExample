from flask import Flask

app = Flask(__name__)  # Create an instance of the Flask class

@app.route('/wish')
def Wish():
    return "Hello, JENKINS!"

if __name__ == "__main__":
    app.run(host = "0.0.0.0") # Start the Flask app
