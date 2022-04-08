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
def default():
    return {"Default Test Urll": "Jivans software and engineering"}


@app.route('/placeorder', methods=['GET','POST'])
def index():
    if request.method == 'POST':
        if "firstName" in request.form and "lastname" in request.form and "country" in request.form and "city" in request.form and "state" in request.form:
            firstName = request.form['firstName']
            lasttName = request.form['lastName']
            country = request.form['country']
            streetAddress = request.form['streetAddress']
            city = request.form['city']
            state = request.form['state']
            postal = request.form['postal']
            phone = request.form['phone']
            emailid = request.form['email']
            cursor = db.connection.cursor(MySQLdb.cursors.DictCursor)
            cursor.execute("INSERT INTO orderHistory(firstName, lastName, country, street, state, postal, phone, email, status) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s)",(firstName,lasttName,country,streetAddress,city,state,postal,phone,emailid))
            info = cursor.fetchone()
            return {"info":info}
    return render_template("product.html")


@app.route("/product/addproduct", methods=['GET','POST'])
def update():
    if request.method == 'POST':
        if "name" in request.form and "description" in request.form and "category" in request.form and "brand" in request.form and "maxprice" in request.form and "minprice" in request.form and "offer" in request.form and "offerduration" in request.form and "specification" in request.form:
            name = request.form['name']
            description = request.form['description']
            category = request.form['category']
            brand = request.form['brand']
            maxprice = request.form['maxprice']
            minprice = request.form['minprice']
            offer = request.form['offer']
            offerduration = request.form['offerduration']
            specification = request.form['specification']
            cursor = db.connection.cursor(MySQLdb.cursors.DictCursor)
            cursor.execute("INSERT INTO product(name, description, category, brand, maxprice, minprice, offer, offerduration, specification) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s)", (name, description, category, brand, maxprice, minprice, offer, offerduration, specification))
            info = cursor.fetchone()
            return {"info": info}

    return render_template("AddProduct.html")


@app.route("/product/getallproducts", methods=['GET', 'POST'])
def GetProduct():
    if request.method == 'GET':
        cursor = db.connection.cursor(MySQLdb.cursors.DictCursor)
        # cursor.execute("SELECT * FROM product WHERE productId=56")
        cursor.execute("SELECT * FROM product")
        info = cursor.fetchone()
        if info is not None:
            return {"name": info['name'],
                    "description": info['description'],
                    "brand": info['brand'],
                    "maxprice": info['maxprice'],
                    "minprice": info['minprice'],
                    "offer": info['offer'],
                    "offerduration": info['offerduration'],
                    "specification": info['specification']}
        else:
            return {"Status": "Data Not Find"}


@app.route("/product/getproduct", methods=['GET', 'POST'])
def GetProductbyid():
    if request.method == 'GET':
        name = request.form['name']
        cursor = db.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute("SELECT * FROM product WHERE name=%s", (name))
        # cursor.execute("SELECT * FROM product")
        info = cursor.fetchone()
        if info is not None:
            # return info
            return {"name": info['name'],
                    "description": info['description'],
                    "brand": info['brand'],
                    "maxprice": info['maxprice'],
                    "minprice": info['minprice'],
                    "offer": info['offer'],
                    "offerduration": info['offerduration'],
                    "specification": info['specification']}
        else:
            return {"Status": "Data Not Find"}


@app.route("/deleteproduct", methods=['POST', 'GET'])
def delete():
    if request.method == 'GET':
        if "name" in request.form:
            name = request.form['name']
            cursor = db.connection.cursor(MySQLdb.cursors.DictCursor)
            cursor.execute("DELETE FROM product WHERE 'name=%s'", name)
            info = cursor.fetchone()
            if info is not None:
                return {"process":"Success"}
            else:
                return {"process": "failed"}
    return render_template("deleteproduct.html")


if __name__ == '__main__':
    app.run(debug=True)