#!/usr/bin/env python3
# Import necessary libraries
import streamlit as st
import modules.db_utilize as dbstuff



def tracking_log():
    st.subheader("Tracking Log")
    if st.button("View Workouts"):
        workouts = dbstuff.fetch_workout_data()
        

    if st.button("View Dayly Tracking Log"):
        print("peepoo poopee")