from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello():
   return "Hello World!"

@app.route("/about")
def info():
    return "Hello ! here we are creating an output."


if __name__=="__main__":
    app.run(port=5000, debug=True)
    # app.run(host="0.0.0.0", port=5001,debug=True)
    

