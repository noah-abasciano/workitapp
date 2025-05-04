#!/usr/bin/env python3
import streamlit as st
import pandas as pd
import sqlite3

def fetch_user_profile():
    # Connect to the SQLite database
    conn = sqlite3.connect('workit.db')
    c = conn.cursor()
    #Display the user profile information. If it doesn't exist, prompt the user to enter their information.
    user_info = c.execute('''SELECT * FROM users''')
    return user_info.fetchall()

def create_user_profile(username, start_weight, goal_weight, current_weight, age):
    # Connect to the SQLite database
    conn = sqlite3.connect('workit.db')
    c = conn.cursor()

    #Insert the user profile information into the database.
    c.execute('''INSERT INTO users (username, start_weight, goal_weight, current_weight, age) VALUES (?, ?, ?, ?, ?)''',
              (username, start_weight, goal_weight, current_weight, age))
    conn.commit()

def fetch_workout_data():
    # Connect to the SQLite database
    conn = sqlite3.connect('workit.db')
    c = conn.cursor()
    #Fetch the workout data from the database.
    workout_data = c.execute('''SELECT * FROM workouts''')
    return workout_data.fetchall()

def fetch_daily_tracking_data():
    # Connect to the SQLite database
    conn = sqlite3.connect('workit.db')
    c = conn.cursor()
    #Fetch the daily tracking data from the database.
    daily_tracking_data = c.execute('''SELECT * FROM dayly''')
    return daily_tracking_data.fetchall()

def update_daily_tracking_data(user_id, date, weight, calories, steps, workout):
    # Connect to the SQLite database
    conn = sqlite3.connect('workit.db')
    c = conn.cursor()
    #Update the daily tracking data in the database.
    c.execute('''INSERT dayly SET weight=?, calories=?, steps=?, workout=? WHERE user_id=? AND date=?''',
              (weight, calories, steps, workout, user_id, date))
    conn.commit()
    conn

def update_workout_data(user_id, exercise_id, date, sets, reps):
    # Connect to the SQLite database
    conn = sqlite3.connect('workit.db')
    c = conn.cursor()
    #Update the workout data in the database.
    c.execute('''UPDATE workouts SET sets=?, reps=? WHERE user_id=? AND exercise_id=? AND date=?''',
              (sets, reps, user_id, exercise_id, date))
    conn.commit()
    conn.close()

def clear_schedule_data(user_id):
    # Connect to the SQLite database
    conn = sqlite3.connect('workit.db')
    c = conn.cursor()
    #Clear the schedule data from the database.
    c.execute('''DELETE FROM schedule WHERE user_id=?''', (user_id,))
    conn.commit()
    conn.close()

def update_schedule_data(user_id, date, projected_weight, upper_bound, lower_bound, phase):
    # Connect to the SQLite database
    conn = sqlite3.connect('workit.db')
    c = conn.cursor()
   
    #Update the schedule data in the database.
    c.execute('''
        INSERT INTO schedule (user_id, date, projected_weight, upper_bound, lower_bound, phase) VALUES (?, ?, ?, ?, ?, ?)''',
        (user_id, date, projected_weight, upper_bound, lower_bound, phase))
    conn.commit()
    conn.close()

def fetch_schedule_data():
    # Connect to the SQLite database
    conn = sqlite3.connect('workit.db')
    c = conn.cursor()
    #Fetch the schedule data from the database.
    schedule_data = c.execute('''SELECT * FROM schedule''')
    return schedule_data.fetchall()