#!/usr/bin/env python3
# Import necessary libraries
import streamlit as st
import modules.db_utilize as dbstuff



def tracking_log():
    st.subheader("Tracking Log")
    while st.checkbox("Add Today's Data"):
        with st.container():
            st.write("Add today's data:")
            date = st.date_input("Date")
            weight = st.number_input("Weight", min_value=0.0, step=0.1)
            calories = st.number_input("Calories", min_value=0, step=1)
            steps = st.number_input("Steps", min_value=0, step=1)
            workout = st.checkbox("Workout Completed?")
            
            if st.button("Submit"):
                user_info = dbstuff.fetch_user_profile()
                dbstuff.update_daily_tracking_data(user_info[0][0], date, weight, calories, steps, workout)
                st.success("Data submitted successfully!")
        

    if st.button("View Dayly Tracking Log"):
        print("peepoo poopee")