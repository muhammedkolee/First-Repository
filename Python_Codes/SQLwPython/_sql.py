import datetime
import mysql.connector

db = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "muhammed18",
    database = "okul"
)


cursor = db.cursor()

# cursor.execute("SELECT * FROM okul.sinif")
# result = cursor.fetchall()
# print(result)

# cursor.execute("SELECT no, name, surname FROM okul.sinif")
# result = cursor.fetchall()
# print(result)

# cursor.execute("SELECT name, surname FROM okul.sinif where gender = 'K'")
# result = cursor.fetchall()
# print(result)

# cursor.execute("SELECT * FROM okul.sinif where year(birthdate) = 2003")
# result = cursor.fetchall()
# print(result)

# cursor.execute("SELECT * FROM okul.sinif where name = 'Ali' and birthdate = 2005")
# result = cursor.fetchall()
# print(result)

# cursor.execute("select * from okul.sinif where name like '%an%'")
# result = cursor.fetchall()
# print(result)

# cursor.execute("select count(*) from okul.sinif where gender = 'K'")
# result = cursor.fetchone()
# print(result[0])

# cursor.execute("select * from okul.sinif where gender = 'K' order by name")
# result = cursor.fetchall()
# print(result)

# cursor.execute("update okul.sinif set name = 'Narin', surname = 'Kara', birthdate = '2007-08-30', gender = 'K' where name = 'Ayşe'")
# db.commit()
# cursor.execute("select * from okul.sinif where name = 'Narin'")
# result = cursor.fetchall()
# print(result)

# cursor.execute("update okul.sinif set gender = 'M' where name = 'Narin'")
# db.commit()
# cursor.execute("select * from okul.sinif where name = 'Narin'")
# result = cursor.fetchall()
# print(result)

# cursor.execute("delete from okul.sinif where name = 'Ali'")
# db.commit()
# cursor.execute("select * from okul.sinif")
# result = cursor.fetchall()
# print(result)

# cursor.close()
# db.close()