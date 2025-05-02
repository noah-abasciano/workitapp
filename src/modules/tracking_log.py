#!/usr/bin/env python3
# Import necessary libraries
import streamlit as st
import modules.workitdb as dbstuff



def tracking_log():
    st.title("Tracking Log")

    if st.button('Workout Log'):
        st.write("This page will display the workout log.")
        dbstuff.display_exercise_entry()
    
    if st.button('Health Log'):
        st.write("This page will display the health log.")
        dbstuff.display_user_entry()