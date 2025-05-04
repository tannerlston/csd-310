""" import statements """
import mysql.connector # to connect
from mysql.connector import errorcode

import dotenv # to use .env file
from dotenv import dotenv_values

#using our .env file
secrets = dotenv_values(".env")

""" database config object """
config = {
    "user": secrets ["USER"],
    "password": secrets["PASSWORD"],
    "host": secrets["HOST"],
    "database": secrets["DATABASE"],
    "raise_on_warnings": True #not in .env file
}
def show_films(cursor, title):
    # Method to execute an inner join on all tables,
    # iterate over the dataset and output the results to the terminal window.
    
    # Inner join query
    query = """
    SELECT 
        film.film_name AS Name, 
        film.film_director AS Director, 
        genre.genre_name AS Genre, 
        studio.studio_name AS 'Studio Name'
    FROM film
    INNER JOIN genre ON film.genre_id = genre.genre_id
    INNER JOIN studio ON film.studio_id = studio.studio_id;
    """
    
    cursor.execute(query)

    # Get the results from the cursor object
    films = cursor.fetchall()

    print("\n -- {} --"
    "".format(title))

    # Iterate over the film dataset and display the results 
    for film in films:
        print("Film Name: {}\nDirector: {}\nGenre: {}\nStudio Name: {}\n".format(film[0], film[1], film[2], film[3]))

def insert_newRecord(cursor):
    cursor.execute("INSERT INTO film (film_name, film_releaseDate, film_runtime, film_director, studio_id, genre_id) VALUES ('Speak No Evil', '2024', 110, 'James Watkins', 3, 1)")

def update_AlienGenre(cursor):
    cursor.execute("UPDATE film SET genre_id = 1 WHERE film_name = 'Alien';")

def delete_gladiatorRecord(cursor):
    cursor.execute("DELETE FROM film WHERE film_name = 'Gladiator';")



try:
    """ try/catch block for handling potential MySQL database errors """ 

    db = mysql.connector.connect(**config) # connect to the movies database 
    
    cursor = db.cursor()

    # output the connection status 
    print("\n  Database user {} connected to MySQL on host {} with database {}".format(config["user"], config["host"], config["database"]))

    input("\n\n  Press any key to continue... \n")
    
    
    
    show_films(cursor, "DISPLAYING FILMS")
    
    insert_newRecord(cursor)
    
    show_films(cursor, "DISPLAYING FILMS AFTER INSERT")
    
    update_AlienGenre(cursor)
    
    show_films(cursor, "DISPLAYING FILMS AFTER UPDATE- Changed Alien to Horror")
    
    delete_gladiatorRecord(cursor)
    
    show_films(cursor, "DISPLAYING FILMS AFTER DELETE")





    

except mysql.connector.Error as err:
    """ on error code """

    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print("  The supplied username or password are invalid")

    elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print("  The specified database does not exist")

    else:
        print(err)

finally:
        db.close()


