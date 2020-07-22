from flask import Flask,redirect,url_for,request,flash
from flask import render_template
from forms import ContactForm

app = Flask(__name__)
app.secret_key = 'any random string'  #使用session要设置的

@app.route('/contact',methods = ['GET','POST'])
def contact():
    form = ContactForm()
    if request.method =='POST':
        if form.validate() == False:
            flash('All fields are required.')
            return render_template('login.html',form = form)
        else:
            return render_template('index.html')
    elif request.method == 'GET':
        return render_template('login.html',form = form)

@app.route('/success/<name>')
def success(name):
    return 'welcome %s'%name
@app.route('/login/')
def login():
    return render_template('login.html')
@app.route('/verfication/',methods=['POST','GET'])
def verfication():
    if request.method == 'POST':
        user = request.form['name']
        return redirect(url_for('success',name = user))
    else:
        user  = request.args.get('name')
        return redirect(url_for('success',name = user))
@app.route('/hello/<score>')
def hello_name(score):
   return render_template('login.html', marks = score)
if __name__ == '__main__':
    app.run(debug = True)
