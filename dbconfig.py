import mysql.connector as myconn
def connect():
    return myconn.connect(
        host="localhost",
        user="root",
        password="Rik@12345",
        database="bank_management_system"

    )