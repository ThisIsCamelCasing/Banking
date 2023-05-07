import mysql.connector

connection = mysql.connector.connect(user = "root", database = "elite102", password="saif2007-")

import tkinter as tk
import sqlite3

# Connect to the database
conn = sqlite3.connect('bank.db')
cursor = conn.cursor()

# Function to retrieve user information
def get_user_info(user_id):
    cursor.execute("SELECT * FROM users WHERE id=?", (user_id,))
    user_info = cursor.fetchone()
    return user_info

# Function to update user balance
def update_balance(user_id, new_balance):
    cursor.execute("UPDATE users SET balance=? WHERE id=?", (new_balance, user_id))
    conn.commit()

# Function to handle ID submit button click
def submit_button_click():
    user_id = user_id_entry.get()
    
    user_info = get_user_info(user_id)
    if user_info:
        balance = user_info[3]
        balance_label["text"] = f"Balance: {balance}"
        deposit_button["state"] = "normal"
        withdraw_button["state"] = "normal"
    else:
        balance_label["text"] = "User not found"
        deposit_button["state"] = "disabled"
        withdraw_button["state"] = "disabled"

# Function to handle deposit button click
def deposit_button_click():
    user_id = user_id_entry.get()
    amount = int(amount_entry.get())
    
    user_info = get_user_info(user_id)
    if user_info:
        current_balance = user_info[3]
        new_balance = current_balance + amount
        update_balance(user_id, new_balance)
        
        balance_label["text"] = f"Balance: {new_balance}"
    else:
        balance_label["text"] = "User not found"

# Function to handle withdraw button click
def withdraw_button_click():
    user_id = user_id_entry.get()
    amount = int(amount_entry.get())
    
    user_info = get_user_info(user_id)
    if user_info:
        current_balance = user_info[3]
        if current_balance >= amount:
            new_balance = current_balance - amount
            update_balance(user_id, new_balance)
            
            balance_label["text"] = f"Balance: {new_balance}"
        else:
            balance_label["text"] = "Insufficient funds"
    else:
        balance_label["text"] = "User not found"


