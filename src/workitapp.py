#!/usr/bin/env python3

import streamlit as st
from streamlit_option_menu import option_menu
import modules.home as home
import modules.your_stats as your_stats
import modules.tracking_log as tracking_log
import modules.schedule as schedule
import modules.exercise_tutorials as exercise_tutorial_links
import modules.db_init as dbinit

#Initiate Title Page and Navigation Bar
st.title("Workit Calisthenics")

# Create the sidebar with navigation options
with st.sidebar:
    pages = option_menu("Main Menu", ["Home", "Your Stats", "Tracking Log", "Schedule", "Exercise Tutorial Links"], 
                                icons=["house", "bar-chart", "calendar", "clock", "link"],
                                menu_icon="cast",
                                default_index=0)

# Initialize the database
dbinit.initiate_db()

#Display the selected page based on the logic in the pages subdirectory
if pages == "Home":
    home.display_user_profile()
    home.home()
elif pages == "Your Stats":
    your_stats.your_stats()
elif pages == "Tracking Log":
    tracking_log.tracking_log()
elif pages == "Schedule":
    schedule.init_schedule()
    schedule.schedule()
elif pages == "Exercise Tutorial Links":
    exercise_tutorial_links.exercise_tutorials()

