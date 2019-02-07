from flask import Flask, render_template, request
import sqlite3 as sql

app = Flask('__main__')

@app.route('/')
def main():
    return render_template('index.html')

@app.route('/index',methods = ['POST', 'GET'])
def aftersignup():
	if request.method == 'POST':
		try:
			fnm = request.form['firstname']
			lnm = request.form['lastname']
			email = request.form['email']
			unm = request.form['username']
			pwd = request.form['password']
			with sql.connect("da2.db") as con:
				cur = con.cursor()
				cur.execute("INSERT INTO users (fname,lname,email,uname,password)VALUES (?,?,?,?,?)",(fnm,lnm,email,unm,pwd))
				#cur.execute("CREATE TABLE unme (name TEXT, age INT, email TEXT, teacher TEXT)")
				con.commit()
				msg = "Record successfully added"
				print("hello")
		except:
			sql.connect("da2.db").rollback()
			msg = "error in insert operation"
			  
		return render_template("index.html",msg=msg)
		con.close()

@app.route('/profile',methods=['POST', 'GET'])
def profile():
		if request.method == 'POST':
			email = request.form['email']
			pwd = request.form['password']
			unm = request.form['username']
			con = sql.connect("da2.db")
			cursor=con.execute("SELECT password FROM users WHERE email = ?",(email,))
			for row in cursor:
				if(row[0]==pwd):
					msg="login succcessfully"
					#flash('login successfully.')
					conn = sql.connect("da2.db")
					res = conn.execute("SELECT * FROM un WHERE teacher = ?",(unm,))
					return render_template("profile.html", info = res.fetchall())
				else:
					msg="login unsuccessful"
					return render_template("index.html",msg=msg)

@app.route('/profile/add',methods=['POST', 'GET'])
def add():
		if request.method == 'POST':
			name = request.form['name']
			age = request.form['age']
			email = request.form['email']
			unm = request.form['tname']
			con = sql.connect("da2.db")
			cur = con.cursor()
			cur.execute("INSERT INTO un (name,age,email,teacher)VALUES (?,?,?,?)",(name,age,email,unm))
			res = cur.execute("SELECT * FROM un WHERE teacher = ?",(unm,))
			con.commit()
			return render_template("profile.html",info = res.fetchall())

@app.route('/profile/delete',methods=['POST', 'GET'])
def delete():
		if request.method == 'POST':
			name = request.form['name']
			unm = request.form['tname']
			con = sql.connect("da2.db")
			cur = con.cursor()
			cur.execute("DELETE FROM un WHERE name = ? AND teacher = ?",[name,unm,])
			res = cur.execute("SELECT * FROM un WHERE teacher = ?",(unm,)) 
			return render_template("profile.html",info = res.fetchall())


if __name__ == '__main__':
	app.run(debug = True)
