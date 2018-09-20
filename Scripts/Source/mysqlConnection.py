#!/usr/bin/python
import mysql
import mysql.connector
import json

class Mysqlcon:
    # Open database connection
    db = mysql.connector.connect(host="localhost",  # your host 
                        user="root",       # username
                        passwd="anirban",     # password
                        db="test")   # name of the database
    # prepare a cursor object using cursor() method
    cursor = db.cursor()


    

    def getData(self):
        sql = "SELECT * FROM clicks" 
        # Execute the SQL command
        self.cursor.execute(sql)
        items = []
        # Fetch all the rows in a list of lists.
        results = self.cursor.fetchall()
        for row in results:
            items.append({'Id':row[0], 'firstName':row[1], 'lastName':row[2]})
            # Now print fetched result
        return items    
    
    # disconnect from server
    #db.close()