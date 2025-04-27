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


try:
    """ try/catch block for handling potential MySQL database errors """ 

    db = mysql.connector.connect(**config) # connect to the movies database 
    
    cursor = db.cursor()

    # output the connection status 
    print("\n  Database user {} connected to MySQL on host {} with database {}".format(config["user"], config["host"], config["database"]))

    input("\n\n  Press any key to continue... \n")


   
    cursor.execute("SELECT studio_id, studio_name FROM studio")
    studios = cursor.fetchall()
    print('-- DISPLAYING Studio RECORDS --')
    for studio in studios:
        print("Studio ID: {}\n Studio Name: {}\n".format(studio[0], studio[1]))

    
    cursor.execute("SELECT genre_id, genre_name FROM genre")
    genres = cursor.fetchall()
    print('\n-- DISPLAYING Genre RECORDS --')
    for genre in genres:
        print("Genre ID: {}\n Genre Name: {}\n".format(genre[0], genre[1]))


    cursor.execute("SELECT film_name, film_runtime FROM film WHERE film_runtime < 120")
    films = cursor.fetchall()
    print('\n-- DISPLAYING Short Film RECORDS --')
    for film in films:
        print("Film Name: {}\n Film Runtime: {}\n".format(film[0], film[1]))

    cursor.execute("SELECT film_name, film_director FROM film ORDER BY film_director")
    films = cursor.fetchall()
    print('\n-- DISPLAYING Director RECORDS in Order --')
    for film in films:
        print("Film Name: {}\n Film Director: {}\n".format(film[0], film[1]))




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

