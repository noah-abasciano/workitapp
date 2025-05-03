#!/usr/bin/env python3
import streamlit as st
import pandas as pd
import sqlite3
import datetime

def initiate_db():
    try:
        # Connect to the SQLite database
        conn = sqlite3.connect('workit.db')
        c = conn.cursor()

        # Create a table for workout data if it doesn't exist  
        c.execute('''
            CREATE TABLE IF NOT EXISTS workouts (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                user_id INTEGER NOT NULL,
                exercise_id INTEGER NOT NULL,
                date DATETIME NOT NULL,
                sets INTEGER NOT NULL,
                reps INTEGER NOT NULL,
                FOREIGN KEY (user_id) REFERENCES users (id),
                FOREIGN KEY (exercise_id) REFERENCES exercises (id)
            )
        ''')

        # Create a table for daily tracking if it doesn't exist
        c.execute('''
            CREATE TABLE IF NOT EXISTS dayly (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                user_id INTEGER NOT NULL,
                date DATETIME NOT NULL,
                weight REAL NOT NULL,
                calories INTEGER NOT NULL,
                steps INTEGER NOT NULL,
                workout BOOLEAN NOT NULL,
                FOREIGN KEY (user_id) REFERENCES users (id)
            )
        ''')
        conn.commit()

        # Create a table for user profile if it doesn't exist
        c.execute('''
            CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                username TEXT NOT NULL,
                start_weight REAL NOT NULL,
                goal_weight REAL NOT NULL,
                current_weight REAL NOT NULL,
                age INTEGER NOT NULL
            )
        ''')
        conn.commit()

        #Create a table for the schedule if it doesn't exist
        c.execute('''
            CREATE TABLE IF NOT EXISTS schedule (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                user_id INTEGER NOT NULL,
                date DATETIME NOT NULL,
                projected_weight REAL NOT NULL,
                upper_bound REAL NOT NULL,
                lower_bound REAL NOT NULL,
                phase INTEGER NOT NULL,
                FOREIGN KEY (date) REFERENCES dayly (date)
            )
        ''')

        # Close the connection
        conn.close()

    except Exception as e:
        st.error(f"An error occurred while initializing the database: {e}")