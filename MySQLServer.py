#!/usr/bin/env python3
"""
MySQLServer.py
A simple Python script that creates the 'alx_book_store' database.
"""

import mysql.connector

def create_database():
    try:
        # Connect to MySQL Server (update user/password as needed)
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

    except mysql.connector.Error as err:
        print(f"Error while connecting to MySQL: {err}")

    finally:
        # Ensure connection is properly closed
        if 'connection' in locals() and connection.is_connected():
            cursor.close()
            connection.close()
            print("MySQL connection closed.")

if __name__ == "__main__":
    create_database()
