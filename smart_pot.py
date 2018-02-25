#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sun Feb 25 14:13:15 2018

@author: pete
"""
### Import relevant libraries
#import automationhat # this library allows us to address the peripheral hardware daughter board on the RPi
#import time #this library allos us to create simple delays in second values
import sqlite3 as db #sqlite3 allows us to store data into tables that are extensible and more manageable than simple csv files

# set up RPi database
file = "parameter_log.db" # creates a database file which which will host all the parameters (temperature, soil moisture, light level ...)

con = db.connect(file) #if the file doesn't exist, sqlite creates the file (db prefix associates connect command with SQLITE3 library)

pos = con.cursor() #open the cursor system which allows us to point to the correct location within the database

def createTable(): #establish a function which, when called, creates a table of our choosing
    pos.execute('CREATE TABLE IF NOT EXISTS parameters(time, temperature, light_level, soil_moisture)')
    con.commit()
#    con.close() (FLAG TO JON HOW WE REOPEN DATABASE FURTHER DOWN THE LINE)
    print("Table create fine..")

createTable() 

#to ask John! how do we re-open a database connection?

def addData():
    i = int(input("time")) #input is a python function to accept a dynamic input andassign to a variable
    n = int(input("temperature"))
    p = int(input("light level"))
    q = int(input("soil moisture"))
    pos.execute('INSERT INTO parameters(time,temperature,light_level, soil_moisture) values(?, ?, ?, ?)', (i,n,p,q)) 
    con.commit()

addData()


def retrieve():
    pos.execute('select time from parameters')
    for row in pos:
        print(row) 
    
retrieve()



# implement Rpi control logic






