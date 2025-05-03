import streamlit as st
import pandas as pd
import datetime
from modules.home import init_user_profile
import modules.db_utilize as dbstuff
import seaborn as sns
import matplotlib.pyplot as plt
            

def schedule():
    st.subheader("Today's Target Weight")
    schedule_data = dbstuff.fetch_schedule_data()
    schedule_df = pd.DataFrame(schedule_data, columns=["ID", "User ID", "Schedule Date", "Projected Weight", "Upper Bound", "Lower Bound", "Phase"])
    schedule_df = schedule_df.drop(columns=["ID", "User ID"])  # Drop the ID and User ID columns if not needed
    
    #Display today's stats
    schedule_df["Schedule Date"] = pd.to_datetime(schedule_df["Schedule Date"]).dt.date  # Convert to datetime
    today = datetime.date.today()  # Get today's date as a datetime.date object
    
    #Use boolean indexing to filter the DataFrame for today's date
    today_schedule = schedule_df[schedule_df["Schedule Date"] == today]
    if not today_schedule.empty:
        st.write(f"Today's Target Weight: {today_schedule['Projected Weight'].values[0]}")

    # Display the filtered DataFrame
    filtered_schedule = schedule_df

    # Create a container for the buttons
    with st.container():
        # Create a custom number of buttons for the user to select
        button_count = max(schedule_df["Phase"])  # Get the maximum phase number

        # Create columns for the buttons
        columns = st.columns(button_count)

        for ct in range(button_count):
            ct_out = f"Phase {ct}" if ct > 0 else f"Full Schedule"
            with columns[ct]:
                # Create a button for each phase
                phase_button = st.button(f"{ct_out}", key=f"phase_{ct}")
                
                if phase_button:
                    # Filter the DataFrame based on the selected phase
                    filtered_schedule = schedule_df[schedule_df["Phase"] == ct] if ct > 0 else schedule_df

        ct += 1 

    # Display the schedule as a table
    st.subheader("Schedule")
    sns.set_theme(style="whitegrid")
    
    # Create a matplotlib figure
    plt.figure(figsize=(12, 6))
    
    # Add Seaborn line plots
    sns.lineplot(data=filtered_schedule, x="Schedule Date", y="Projected Weight", label="Projected Weight")
    sns.lineplot(data=filtered_schedule, x="Schedule Date", y="Upper Bound", label="Upper Bound")
    sns.lineplot(data=filtered_schedule, x="Schedule Date", y="Lower Bound", label="Lower Bound")
    
    # Add a vertical line for today's date
    if min(filtered_schedule["Schedule Date"]) <= today <= max(filtered_schedule["Schedule Date"]):
        plt.axvline(x=today, color='black', linestyle='--', label="Today's Date")
    
    # Add labels and title
    plt.xlabel("Schedule Date")
    plt.ylabel("Weight")
    plt.title("Projected Weight Schedule")
    plt.legend()
    
    # Display the plot in Streamlit
    st.pyplot(plt)

    st.subheader("Schedule Data")
    st.dataframe(filtered_schedule, hide_index=True)  # Display the filtered schedule as a table
