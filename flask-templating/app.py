from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def hello():
    return render_template('hello.html')

@app.route('/ben')
def ben():
     return render_template('ben.html')

@app.route('/harry')
def harry():
     return render_template('harry.html')



if __name__ == "__main__":
     app.run(debug=True, host='0.0.0.0', port=5000)