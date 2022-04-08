from flask import  Flask, render_template, redirect, url_for, request
from flask_mysqldb import MySQL
import MySQLdb

app = Flask(__name__)
app.secret_key = "123456"

app.config["MYSQL_HOST"] = "localhost"
app.config["MYSQL_USER"] = 'root'
app.config["MYSQL_PASSWORD"] = ''
app.config["MYSQL_DB"] = "login"
session = {}
db = MySQL(app)

@app.route('/', methods=['GET','POST'])
def index():
    if request.method == 'POST':
        if 'username' in request.form and 'password' in request.form:
            username = request.form['username']
            password = request.form['password']
            cursor = db.connection.cursor(MySQLdb.cursors.DictCursor)
            cursor.execute("SELECT * FROM user WHERE userid=%s AND password=%s",(username,password))
            info = cursor.fetchone()
            if info is not None:
                if info['userid'] == username and info['password'] == password:
                    session['loginsuccess'] = True
                    return redirect(url_for("profile"))

            else:
                session['loginsuccess'] = False
                return render_template("incorrect.html")
    return render_template("login.html")


@app.route('/register', methods=['GET','POST'])
def new_user():
    if request.method == 'POST':
        if 'hello' in request.form and 'two' in request.form and 'Three' in request.form:
            name = request.form['hello']
            email = request.form['two']
            password = request.form['Three']
            conformPasword = request.form['four']
            if password == conformPasword:
                cursor = db.connection.cursor(MySQLdb.cursors.DictCursor)
                cursor.execute("INSERT INTO login.user(name, userid, password, conformPassword) VALUES (%s,%s,%s,%s)", (name, email, password, password))
                db.connection.commit()
                return redirect(url_for("index"))

    return render_template("register.html")

@app.route('/profile')
def profile():
    if session['loginsuccess'] == True:
        return render_template("profile.html")
    else:
        pass

    return render_template("profile.html")


@app.route('/logout', methods=['GET','POST'])
def logout():
    session['loginsuccess'] = False


@app.route('/forgot', methods=['POST','GET'])
def forgot():
    if request.method == 'POST':
        if "newPass" in request.form and "email" in request.form:
            newPass = request.form['newPass']
            emailid = request.form['email']
            cursor = db.connection.cursor(MySQLdb.cursors.DictCursor)
            cursor.execute("SELECT * FROM user WHERE userid=%s", (emailid))
            info = cursor.fetchone()
            if info is not None:
                if info['userid'] == emailid:
                    session['loginsuccess'] = True
                    cursor = db.connection.cursor(MySQLdb.cursors.DictCursor)
                    cursor.execute("UPDATE login.user SET userid=%s password=%s,conformPassword=%s WHERE 1",(emailid, newPass,newPass))
                    cursor.connection.commit()
                    return redirect(url_for("profile"))

            return "failed"
    return render_template("forgot.html")


if __name__ == '__main__':
    app.run(debug=True)

# INSERT INTO 'user'('email', 'userid', 'password', 'conformPassword') VALUES ("-","-","-","-")