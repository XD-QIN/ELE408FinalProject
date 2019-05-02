#!/usr/bin/env python

import sqlite3
from sense_hat import SenseHat
import os
import time
import glob

# global variables
speriod=1
dbname='/var/www/templog.db'
sense = SenseHat()



# store the temperature in the database
def log_temperature(temp):

    conn=sqlite3.connect(dbname)
    curs=conn.cursor()

    curs.execute("INSERT INTO temps values(datetime('now'), (?))", (temp,))

    # commit the changes
    conn.commit()

    conn.close()


# display the contents of the database
def display_data():

    conn=sqlite3.connect(dbname)
    curs=conn.cursor()

    for row in curs.execute("SELECT * FROM temps"):
        print (str(row[0])+"	"+str(row[1]))

    conn.close()


# main function
# This is where the program starts 
def main():


#    while True:

    # get the temperature from the device file
    temperature = sense.get_temperature()
    if temperature != None:
        print ("temperature="+str(temperature))
    else:
        # Sometimes reads fail on the first attempt
        # so we need to retry
        temperature = sense.get_temperature()
        print ("temperature="+str(temperature))

        # Store the temperature in the database
    log_temperature(temperature)

        # display the contents of the database
#        display_data()

#        time.sleep(speriod)


if __name__=="__main__":
    main()
