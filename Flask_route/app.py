

from flask import Flask

app = Flask(__name__)

## This is the home page
@app.route('/')
@app.route('/home')
def hello_internet():
    return "Hello Internet! HaHaHa my first Web!!!!" "\nThis feels good. "

## This will be the about page, routing between webpage home and about

@app.route('/about')
def about():
    return "This is the about page, It shows that the Flask_route is working"

## I will now add and extra page (contact us section)

@app.route('/contact')
def contact_us():
    return "You can contact us on 555 555 555 localhost: 5000"

## Exercise about QA creating dynamic url taking a number from url and squaring it

@app.route('/square/<num>')
def square(num):
    num = int(num)
    answer = num*num
    return str(answer)


if __name__=='__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)