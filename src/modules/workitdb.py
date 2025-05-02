#!/usr/bin/env python3

import sqlite3 as sql

#Connect to or create the workout tracking SQL database
wodb = sql.connect('workout_tracker.db')
wodb_c = wodb.cursor()

#Create the workout_tracker database if it does not exist:
wodb_c.execute('''CREATE TABLE IF NOT EXISTS workout_tracker
            (wo_date DATETIME NOT NULL, 
            woID INTEGER PRIMARY KEY,
            repID INTEGER NOT NULL,
            exercise TEXT,
            liftweight FLOAT, 
            sets INTEGER
            )''')

#Create the user_stats database if it does not exist:
wodb_c.execute('''CREATE TABLE IF NOT EXISTS user_stats
            (entryID INTEGER PRIMARY KEY,
            user TEXT,
            us_date DATETIME, 
            woID INTEGER,
            sleep DATETIME,
            weight FLOAT,
            calories INTEGER, 
            steps INTEGER
            )''')

wodb_c.execute('''CREATE TABLE IF NOT EXISTS profile
            (user TEXT PRIMARY KEY,
            age INTEGER,
            height FLOAT,
            weight FLOAT,
            training_level INTEGER,
            goal_weight FLOAT,
            goal_end_date DATETIME
            )''')

wodb.commit()

def add_exercise_entry(wo_date, woID, repID, exercise, liftweight, sets):
    wodb_c.execute('''INSERT INTO workout_tracker (wo_date, woID, repID, exercise, liftweight, sets)
                    VALUES (?, ?, ?, ?, ?, ?)''', (wo_date, woID, repID, exercise, liftweight, sets))
    wodb.commit()

def add_user_entry(entryID, user, us_date, woID, sleep, weight, calories, steps):
    wodb_c.execute('''INSERT INTO user_stats (user, us_date, woID, sleep, weight, calories, steps)
                    VALUES (?, ?, ?, ?, ?, ?, ?)''', (entryID, user, us_date, woID, sleep, weight, calories, steps))
    wodb.commit()

def add_user_profile(user, age, height, weight, goal_weight, goal_end_date):
    wodb_c.execute('''INSERT INTO profile (user, age, height, weight, goal_weight, goal_end_date)
                    VALUES (?, ?, ?, ?, ?, ?)''', (user, age, height, weight, goal_weight, goal_end_date))
    wodb.commit()

# Function to update an exercise entry
def update_exercise_entry(woID, field, value):
    wodb_c.execute(f'''UPDATE workout_tracker SET {field} = ? WHERE woID = ?''', (value, woID))
    wodb.commit()

# Function to update a user entry
def update_user_entry(entryID, field, value):
    wodb_c.execute(f'''UPDATE user_stats SET {field} = ? WHERE entryID = ?''', (value, entryID))
    wodb.commit()

# Function to update a user profile
def update_user_profile(user, field, value):
    wodb_c.execute(f'''UPDATE profile SET {field} = ? WHERE user = ?''', (value, user))
    wodb.commit()

def display_exercise_entry():
    wodb_c.execute('''SELECT * FROM workout_tracker''')
    rows = wodb_c.fetchall()
    for row in rows:
        print(row)

def display_user_entry():
    wodb_c.execute('''SELECT * FROM user_stats''')
    rows = wodb_c.fetchall()
    for row in rows:
        print(row)

def display_user_profile():
    wodb_c.execute('''SELECT * FROM profile''')
    rows = wodb_c.fetchall()
    for row in rows:
        print(row)
