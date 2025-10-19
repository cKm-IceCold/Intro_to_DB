#!/usr/bin/env python3
"""
MySQLServer.py
A simple Python script that creates the 'alx_book_store' database.
"""

import mysql.connector
from mysql.connector import Error

def create_database():
    try:
        # Connect to MySQL Server (adjust host, user, password as needed)
        connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="your_password_here"  # 🔹 Replace with your MySQL password
        )

        if connection.is_connected():
            cursor = connection.cursor()
            # Create the database if it doesn’t already exist
            cursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store")
            print("Database 'alx_book_store' created successfully!")

    except Error as e:
        print(f"Error while connecting to MySQL: {e}")

    finally:
        # Properly close the connection
        if connection.is_connected():
            cursor.close()
            connection.close()
            print("MySQL connection closed.")

if __name__ == "__main__":
    create_database()
