from flask import Flask, render_template
import pymysql

app = Flask (__name__)

class Database:
	def __init__(self):
		host = "127.0.0.1"
		user = "flask_user"
		password= "jibu007"
		db = "flask_app"
		self.con = pymysql.connect(host=host, user=user, password=password, db=db,
			     cursorclass=pymysql.cursors.DictCursor)
		self.cur = self.con.cursor()

	def list_products(self):
		self.cur.execute("select pid, name, price from product")
		result = self.cur.fetchall()
		return result
		


@app.route('/') 
def home ():
	return render_template("home.html")

@app.route('/product')
def product ():
	def db_query():
		db = Database()
		products = db.list_products()
		return products
	res = db_query()
		

	return render_template("product.html", result=res)
