from flask import Flask, render_template, request
import datetime
import socket
import mysql.connector

app = Flask(__name__)

@app.route('/')
def form():
  return render_template("forms.html")

@app.route('/resultat',methods = ['POST'])
def resultat():
  hostname=socket.gethostname()
  ip_addr=socket.gethostbyname(hostname)
  
  result = request.form
  p = result['post']
  
  now = datetime.datetime.now()
  formatted_date = now.strftime('%Y-%m-%d %H:%M:%S')
  
  # Insertion into the database
  mydb=insertPostDatabase(p,ip_addr, formatted_date)
  
  # Retrieve the tuples
  liste = displayDatabase(mydb)
  return render_template("resultat.html", post=p, ip=ip_addr, date=formatted_date, posts=liste)


def insertPostDatabase(post, ip, date):
    # host value is not localhost but the mysql service name which is "database" in the yaml file
    mydb=mysql.connector.connect(host="database",user="root",password="julie")
    mycursor = mydb.cursor()

    mycursor.execute("CREATE DATABASE IF NOT EXISTS cloud_pw5")

    mydb=mysql.connector.connect(host="database",user="root",password="julie", database="cloud_pw5")

    mycursor = mydb.cursor()
    mycursor.execute("CREATE TABLE IF NOT EXISTS posts (id INT AUTO_INCREMENT PRIMARY KEY, "+
                                                    "post VARCHAR(255), ip VARCHAR(20), date DATETIME)")
    
    mycursor = mydb.cursor()

    sql = "INSERT INTO posts (post, ip, date) VALUES (%s, %s, %s)"
    val = (post, ip,date)
    mycursor.execute(sql, val)

    mydb.commit()
    
    # returns the connection
    return mydb

def displayDatabase(mydb):
    mycursor = mydb.cursor()

    sql = "SELECT * FROM posts"
    mycursor.execute(sql)
    result=mycursor.fetchall()
    
    return result

app.run(debug=True)