#!/usr/bin/env python3

# Import necessary libraries
import streamlit as st
import modules.db_utilize as dbstuff
import pandas as pd

# Function to initialize the user profile
def init_user_profile():
    st.write("No user profile found. Please create a profile.")
    username=st.text_input("Username")
    start_weight=st.number_input("Start Weight", min_value=0)
    goal_weight=st.number_input("Goal Weight", min_value=0)
    current_weight=st.number_input("Current Weight", min_value=0)
    age=st.number_input("Age", min_value=0)    
    if st.button("Create Profile"):
        dbstuff.create_user_profile(username, start_weight, goal_weight, current_weight, age)

#Function to display the user profile on the home page
def display_user_profile():
    user_info = dbstuff.fetch_user_profile()
    if not user_info:
        init_user_profile()    
    st.subheader("User Profile Information")
    # Convert user_info to a DataFrame for better display
    user_data = pd.DataFrame(user_info, columns=["ID", "Username", "Start Weight", "Goal Weight", "Current Weight", "Age"], index=None)
    user_data = user_data.drop(columns=["ID"])  # Drop the ID column if not needed
    st.dataframe(user_data, hide_index=True)  # Display the user profile as a table
        

def home():
    st.title("Welcome to the Home Page!")
    st.write("This is the home page of the app. You can navigate to other pages using the sidebar on the left.")
