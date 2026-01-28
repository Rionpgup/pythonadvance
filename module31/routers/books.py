import sqlite3
from typing import List
from fastapi import APIRouter,HTTPException,status,Depends
from models.book import Book, BookCreate
from database import get_db_connection
from auth.security import get_api_key
router = APIRouter()

@router.get("/books", response_model=List[Book])
def get_books():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM books")
    books = cursor.fetchall()
    conn.close()
    return[{
        "id": book[0],
        "title": book[1],
        "author_id": book[2],
        "book_linl": book[3],
        "genres":book[4].split(",") if book[4] else [],
        "average_rating":book[5],
        "average_year":book[6]

    }
        for book in books
    ]
@router.get("/books/{book_id}", response_model=Book)
def create_book(book:):
    conn = get_db_connection()
    cursor = conn.cursor()
    try: genres = ",".join(book["genres"] if book.genres else None
cursor.execute("INSERT INTO books (title, author_id, book_linl, genres, average_rating,published_year)"
               " VALUES (?,?,?,?)",)",
    (
        book.title,
        book.author_id,
        book.book_link,
        ",".join(book.genres) if book.genres else None,
        book.average_rating,
        book.published_year
            )
    )

