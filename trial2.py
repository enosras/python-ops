import mysql.connector
import mysql

try:
    connection = (mysql.connector.connect
        (
        host='localhost',
        user='enos',
        password='2025@Redmond',
        database='trial_1'
    )
    )

    if connection.is_connected():
        print("Successfully connected to MySQL database.")
        # You can now create a cursor and execute SQL queries
        # cursor = connection.cursor()
        # cursor.execute("SELECT * FROM your_table")
        # results = cursor.fetchall()
        # print(results)

except mysql.connector.Error as err:
    print(f"Error connecting to MySQL: {err}")

finally:
    if 'connection' in locals() and connection.is_connected():
        connection.close()
        print("MySQL connection closed.")