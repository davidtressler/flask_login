#!flask/bin/python
from flask import Flask
from flask import request

from flask import Flask, request, render_template
app = Flask(__name__)

import json
import sqlite3
import dataset


from tinydb import TinyDB, Query
db = TinyDB('db/db.json', indent=4)
table = db.table('userdata')
User = Query()
#db.insert_multiple([{'int': 1, 'char': 'a'}, {'Free Docs':'[1,2,3],[122]'}])



@app.route('/newuser')
def my_form_send():
    return render_template('newuser.html')

@app.route('/newuser', methods=['POST'])
def my_form_post_send():

    processed_text = ""
    user_name = request.form['user_name']
    user_email = request.form['email']
    html_age = request.form['age']
    password = request.form['password']
    #processed_text = text

    # // Tiny DB

    #user_input = processed_text

    user_output = db.search(User.name == user_email)

    #print("user_output",user_output)

    try:
        if user_output[0] != None:
            print("User already exists")
            processed_text = "User already exists"
        else:
            pass
    except:
            db.insert({'email':user_email, 'name': user_name,'password':password,'age':html_age})
            #print("New User Added ", user_input)
            processed_text = "New User Created", user_email

    return processed_text







@app.route('/')
def my_form():
    return render_template('login.html')


@app.route('/', methods=['POST'])
def my_form_post():
    processed_text = ""
    user_email = request.form['user_email']
    password = request.form['user_password']

    #user_email = "bob@bob.com"
    print(user_email)

    user_output = db.search(User.email == user_email)

    print("user_output",user_output)

    try:
        if user_output[0] != None:
            print("User email found ")

            #if user email is found then find if password is correct
            processed_text = user_output[0]['password']
            print(processed_text)
            #print("User Password ", user_output)

        else:
            pass
            #print("NO User email found ")
            #processed_text = "No User Found"
    except:
        print("No User Email Found ")
        processed_text = "No User Found"





    return processed_text






if __name__ == '__main__':
    app.run(debug=True)
