## This is my first web application using Flask. This app runs on local host port 5000.

from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_internet():
    return "Hello Internet! HaHaHa my first Web!!!!" "\nThis feels good. "
    
## All the application syntax should end with the following Syntax;

if __name__=='__main__':
    app.run(debug=True, host='0.0.0.0', port=5000) #you need this line at the end of all applicaitons.