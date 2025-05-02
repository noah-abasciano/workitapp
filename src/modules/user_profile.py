#!/usr/bin/env python3

# Import necessary libraries
import streamlit as st
import modules.workitdb as dbstuff

def user_profile():
    st.title("User Profile")
    st.write("This page will display the user profile.")
    dbstuff.display_exercise_entry()