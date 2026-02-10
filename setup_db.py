import mysql.connector
from mysql.connector import Error

# Config without the database name to initially connect
db_base_config = {
    'host': '127.0.0.1',
    'user': 'root',
    'password': 'moni@@naga17N5'
}

def setup_database():
    try:
        connection = mysql.connector.connect(**db_base_config)
        cursor = connection.cursor()
        
        print("Creating database if it doesn't exist...")
        cursor.execute("CREATE DATABASE IF NOT EXISTS ai_trainer_db;")
        
        print("Using ai_trainer_db...")
        cursor.execute("USE ai_trainer_db;")
        
        print("Creating users table...")
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS users (
                id INT AUTO_INCREMENT PRIMARY KEY,
                username VARCHAR(50) NOT NULL UNIQUE,
                email VARCHAR(100) NOT NULL UNIQUE,
                password VARCHAR(255) NOT NULL,
                role VARCHAR(20) NOT NULL,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            );
        """)
        
        connection.commit()
        print("Database and Table setup COMPLETE!")
        
        cursor.close()
        connection.close()
    except Error as e:
        print(f"Error during setup: {e}")

if __name__ == "__main__":
    setup_database()
