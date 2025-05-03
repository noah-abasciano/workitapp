#!/usr/bin/env python3
# Import necessary libraries
import streamlit as st
import pandas as pd
import datetime
from modules.home import init_user_profile
import modules.db_utilize as dbstuff
import seaborn as sns
import matplotlib.pyplot as plt

#Function to initialize the schedule
def init_schedule():
    user_info = dbstuff.fetch_user_profile()
    if not user_info:
        init_user_profile()
    
    if st.checkbox("Create Schedule"):
        
        if st.checkbox("Are you sure you want to overwrite your current schedule?"):
            

            # Create a placeholder for dynamic messages
            status_placeholder = st.empty()

            #Delete the current schedule
            status_placeholder.write("Clearing current schedule...")
            dbstuff.clear_schedule_data(user_info[0][0])
            

            status_placeholder.write("Creating schedule...")
            #Initialize the schedule dataframe
            weights = []
            days = []
            phase = []

            #Initialize the starting variables
            workdate = datetime.date.today()
            projected_weight = user_info[0][2]  # Start weight
            goal_weight = user_info[0][3] # Goal weight

            #Phase variables
            weight_loss_phase = True
            weight_loss_phase_ct = 1
            weight_loss_rate = 0.01/7*projected_weight
            ct = 0

            #Create a periodized schedule to reach goal weight
            while projected_weight > goal_weight:

                #Increment the schedule components
                workdate += datetime.timedelta(days=1)
                projected_weight -= weight_loss_rate
                weights.append(projected_weight)
                days.append(workdate)
                phase.append(weight_loss_phase_ct)
                
                #Change the phase if 70 days have passed
                if ct == 70:
                    weight_loss_phase = not weight_loss_phase
                    #Check the rate
                    weight_loss_rate = projected_weight*0.01/7 if weight_loss_phase else 0
                    weight_loss_phase_ct += 1 if weight_loss_phase else 0
                    ct = 0
                ct += 1
        
            schedule_df = pd.DataFrame({"Schedule Date": days, "Projected Weight": weights, "Phase": phase})
            schedule_df["Upper Bound"] = schedule_df["Projected Weight"].apply(lambda x: x + x*0.01)
            schedule_df["Lower Bound"] = schedule_df["Projected Weight"].apply(lambda x: x - x*0.01)

            #Update the schedule in the database
            status_placeholder.write("Uploading schedule to database...")
            for row in schedule_df.iterrows():
                dbstuff.update_schedule_data(user_info[0][0], row[1]["Schedule Date"], row[1]["Projected Weight"], row[1]["Upper Bound"], row[1]["Lower Bound"], row[1]["Phase"])
            
            #Finish the schedule creation process
            status_placeholder.success("Schedule created successfully!")
            st.balloons()