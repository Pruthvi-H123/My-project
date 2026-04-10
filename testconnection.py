import mysql.connector

try:
    db = mysql.connector.connect(
        host="127.0.0.1",
        user="root",
        password="",
        database="gadag_water_supply"
    )
    print("Connected to MySQL!")
except Exception as e:
    print("Error:", e)