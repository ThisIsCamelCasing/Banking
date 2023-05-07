import mysql.connector

connection = mysql.connector.connect(user = "root", database = "elite102", password="saif2007-")

import tkinter as tk
import sqlite3

# Connect to the database
conn = sqlite3.connect('bank.db')
cursor = conn.cursor()

# Create a table if it doesn't exist
cursor.execute('''CREATE TABLE IF NOT EXISTS users (
                    id TEXT PRIMARY KEY,
                    username TEXT,
                    password TEXT,
                    balance INTEGER,
                    is_admin INTEGER)''')

