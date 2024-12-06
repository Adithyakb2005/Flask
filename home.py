from flask import Flask,render_template
app=Flask(__name__)

@app.route('/')
def fun1():
    return "Welcome"
@app.route('/fun2')
def fun2():
    return "Sample fun"

@app.route('/index')
def fun3():
    return render_template('index.html')

app.run()
