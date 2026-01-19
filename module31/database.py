import sqlite3

def get_db_connection():
    conn = sqlite3.connect('books.db')
    conn.row_factory = sqlite3.Row
    return conn

def get_db_cursor():
    conn = sqlite3.connect('books.db')
    cursor = conn.cursor()