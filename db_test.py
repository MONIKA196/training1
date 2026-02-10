import mysql.connector
from mysql.connector import Error

db_config = {
    'host': '127.0.0.1',
    'user': 'root',
    'password': 'moni@@naga17N5',
    'database': 'ai_trainer_db'
}

def test_connection():
    print(f"Attempting to connect to MySQL at {db_config['host']}...")
    try:
        connection = mysql.connector.connect(**db_config)
        if connection.is_connected():
            db_info = connection.get_server_info()
            print(f"Successfully connected to MySQL Server version {db_info}")
            cursor = connection.cursor()
            cursor.execute("SELECT DATABASE();")
            record = cursor.fetchone()
            print(f"Connected to database: {record[0]}")
            
            # Check if users table exists
            cursor.execute("SHOW TABLES LIKE 'users';")
            table = cursor.fetchone()
            if table:
                print("Table 'users' exists.")
            else:
                print("Table 'users' does NOT exist. Please run schema.sql in MySQL Workbench.")
            
            cursor.close()
            connection.close()
            print("Connection closed.")
    except Error as e:
        print(f"\n--- ERROR DETECTED ---")
        print(f"Error Code: {e.errno}")
        print(f"SQL State: {e.sqlstate}")
        print(f"Message: {e.msg}")
        print(f"Full Error: {e}")
        print(f"----------------------\n")
        
        if e.errno == 1049:
            print("HINT: The database 'ai_trainer_db' does not exist. Please create it first.")
        elif e.errno == 1045:
            print("HINT: Access denied. Your password or username might be wrong.")
        elif e.errno == 2003:
            print("HINT: Can't connect to MySQL server. Is it running?")

if __name__ == "__main__":
    test_connection()
