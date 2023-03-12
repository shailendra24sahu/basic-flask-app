from flask import Flask,request,jsonify

app=Flask(__name__)


@app.route("/")

def homepage():
    return "<h1>Welcome to the home page<h1>"

@app.route("/add",methods=['POST'])    #this will run over postman, as the request is json file
def addition():
    if request.method=="POST":
        result=int(request.json['num1']) + int(request.json['num2'])
        return jsonify(" The summation is {}".format(result))

if __name__=="__main__":
    app.run(port=5000)