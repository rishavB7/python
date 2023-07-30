
# CONNECTING MYSQL DATABSE TO PYTHON
import mysql.connector as a

# Establishing a connection to the MySQL database
con = a.connect(
    host="localhost", user="root", password="golaghat@123"
)
c = con.cursor()

# DATABASE CREATION
sql1 = "create database LDMS"
c.execute(sql1)
sql2 = "use LDMS"
c.execute(sql2)

# CREATING TABLES TO THE DATABASE
sql3 = """create table books(bname varchar(100),
          bcode integer(100), total integer(100),
          subject varchar(100))"""
c.execute(sql3)

sql4 = """create table issued(sname varchar(100), regno varchar(50),
          bcode integer(100), issue_date varchar(50))"""
c.execute(sql4)

sql5 = """create table submit(sname varchar(50),regno varchar(10),
          bcode integer(100), submit_date varchar(50))"""
c.execute(sql5)

con.commit()