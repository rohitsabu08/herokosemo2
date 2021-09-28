from flask import Flask 

app = Flask(__name__)
@app.route('/',methods = ['GET'])
def welcome():
    return("Swagger building")
@app.route('/name/<your_name>')
def names(your_name):
    return f"Welcome to praxis {your_name}"

    
if __name__ == '__main__':
    app.run()
