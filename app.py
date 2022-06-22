from flask import Flask, redirect, url_for

app = Flask(__name__)

#app.route(rule, options)
@app.route('/')
def index():
    return "<h1> Hi Nikhil Pidiparthy, you are on day1 of your Flask Revision <h1/>"

@app.route('/home')
def home():
    #return redirect('/')
    return redirect(url_for('index'))

@app.route('/names')
def names():
    return  "<h2> You are on Names page <h2/> " 

   
@app.route('/names/<name>')
def name_func(name):
    #return f'<h2> Hi {name} </h2>'
    return "Hi %s" %name

  
if __name__=='__main__':
    app.run(debug=True)
    ##app.run(host, port, debug, options)