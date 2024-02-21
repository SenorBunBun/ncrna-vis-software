import mysql.connector, getpass
print("Starting Connection")

# TODO: Modify with my own credentials
cnx = mysql.connector.connect(user='asuri', password="Ribosome_2023", host='130.207.36.76', database='lncRNA_RBP_DB')
cursor = cnx.cursor()

print("Connected")
print(cursor.execute("SHOW TABLES;"))
tables = cursor.fetchall()
print(tables)

cnx.commit()
cursor.close()
cnx.close()
print("Success!")