import mysql.connector
conn = mysql.connector.connect(host = "localhost",user = "Nonhlanhla",password = "Mbube123@", database ="learners")
c = conn.cursor()
c.execute("CREATE TABLE students(student_id primary key AUTO_INCREMENT,first_name varchar(20) NOT NULL, last_name varchar(20) not null ,grade int, )")
conn.commit()