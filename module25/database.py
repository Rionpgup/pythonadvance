import sqlite3
from models import Movie, MovieCreate

def create_connection():
    connection = sqlite3.connect("movies.db")
    connection.row_factory = sqlite3.Row
    return connection
def create_table():
    connection = create_connection()
    cursor = connection.cursor()
    cursor.execute("""
                   CREATE TABLE IF NOT EXISTS movies (
                   id INTEGER PRIMARY KEY AUTOINCREMENT,
                   title TEXT NOT NULL,
                   director TEXT NOT NULL,
                   )
                   """
                   )
    connection.commit()

    connection.close()

    create_table()
    def create_movie(movie: MovieCreate)-> int:
    """
 Args:
 movie (Movie Create): A pydantic model containing
 the title and director of and movie to be created
    """

connection = create_connection()
cursor = connection.cursor()
cursor.execute("Insert into movies (title, director) values (?, ?)",(movie.title, movie.director))

 connection.commit()
 movie_id = cursor.lastrowid
 connection.close()
 return movie_id

def read_movie():
    """
    Reatrieves all movies from database
    """
    connection = create_connection()
    cursor = connection.cursor()
    cursor.execute("SELECT * from movies")
    rows = cursor.fetchall()
    connection.close()
    movies = [Movie(id=row[0], title=row[1], director=row[2]) for row in rows]
    return movies
def+ read_movie(movie_id: int)
"""
Retrievers a single movie from database by its ID.
Return:
Movie: A movie model repeting the retieved movie
Return None if the movie is not found
"""
connection = create_connection()
cursor = connection.cursor()
cursor.execute("SELECT * from movies where id = ?",(movie_id,))
rows = cursor.fetchone()
connection.close()
if row is None:
    return None
return Movie(id=row["id"], title=row["title"], director=row["director"])
def update_movie(movie_id: int, movie: MovieCreate) -> bool:
    """
    Updated an existing movie in the database
    """
    connection = create_connection()
    cursor = connection.cursor()
    cursor.execute(
        "UPDATE movies SET title=?, director=? WHERE id = ?",
        (movie.title, movie.director, movie_id)
    )
    connection.commit()
    updated = cursor.rowcount
    connection.close()
    return updated > 0


def delete_movie(movie_id: int) -> bool:
    connection = create_connection()
    cursor = connection.cursor()
    cursor.execute("DELETE FROM movies WHERE id = ?", (movie_id,))
    connection.commit()
    deleted = cursor.rowcount
    connection.close()
    return deleted > 0
