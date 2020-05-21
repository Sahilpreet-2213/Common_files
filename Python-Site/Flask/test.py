from flask import Flask,render_template,request,session
import json 
from flask_mail import Mail 
from flask_sqlalchemy import SQLAlchemy
import pandas as pd
app = Flask(__name__)
app.secret_key = 'waheguru'

mail = Mail(app)

with open('conf.json','r') as file:
    param = json.load(file)['data']

app.config.update(
    Mail_SERVER = 'smtp.gmail.com',
    MAIL_PORT =   '465',
    MAIL_USE_SSL = True,
    MAIL_USERNAME = param['user'],
    MAIL_PASSWORD = param['pass'] 
)

local_server = True 
if local_server:
    app.config['SQLALCHEMY_DATABASE_URI'] = param['uri']
# print(param['uri'])

db = SQLAlchemy(app)

class Mains(db.Model):
    sno = db.Column(db.Integer, primary_key=True)
    Name = db.Column(db.String(120), unique=True, nullable=False)
    Phone_num = db.Column(db.String(120), unique=True, nullable=False)
    message = db.Column(db.String(120), unique=True, nullable=False)
    mails = db.Column(db.String(120), unique=False, nullable=False)
    
@app.route('/')
def home():
    return render_template('first.html',param=param)


@app.route('/second',methods=['POST','GET'])
def mains():
    if request.method == "POST":
        name = request.form.get('name')
        phone = request.form.get('phone')
        msg = request.form.get('message')
        mails = request.form.get('mails')
        entry = Mains(Name = name, Phone_num = phone, message = msg, mails=mails)
        db.session.add(entry)
        db.session.commit()
        mail.send_message('New message from' + name,
                        sender=mails,
                        recipients=param['user'],
                        body=f""" User_name: {name}
                                  Message: {msg},
                                  Phone Number: {phone}""")

    return render_template('second.html',param=param)


class Content(db.Model):
    sno = db.Column(db.Integer, primary_key=True)
    img = db.Column(db.String(30), nullable=False)

# @app.route('/insta')
# def insta():
# 	return render_template('instagram.html')

@app.route('/to_post',methods=["GET","POST"])
def to_post():
    # forms = PostForm(request.POST or None)
    
    if (request.method == 'POST') and (request.form.get('posts') != ''):
        print('....',request.form.get('posts'))
        imgs = request.form.get('posts')
        entry = Content(img=imgs)
        db.session.add(entry)
        db.session.commit()
    # return render_template("fourth.html",param=param)

    elif request.method == 'POST':
        dele = request.form.get('post_del')
        # print('...',dele)
        try:
            dl=Content.query.filter_by(img=dele).first()
            db.session.delete(dl)
            db.session.commit()
        except Exception:
            return render_template("fourth.html",param=param)
    return render_template("fourth.html",param=param)

    

@app.route('/third')
def content():
    
    main_content=Content.query.all()
    for x in main_content:
        image=x
    return render_template("third.html",param=param,main_content=main_content,image=image)    

@app.route('/insta')
def insta():
    return render_template('first.html',param=param)

@app.route('/sign_in',methods=['GET','POST'])
def sign_in():

    # if ('user' in session and session['user'] == param['admin_user']):
    #     return render_template('second.html',param=param)

    if request.method == 'POST':
        username=request.form.get('user')
        password=request.form.get('pass')
        if (username == param['admin_user']) and (password == param['admin_pass']):
            session['user'] = username
            return render_template('second.html',param=param)
        else:
            return render_template('sign_in.html',param=param)
    else:
        return render_template('sign_in.html',param=param)

app.run(debug=True) 