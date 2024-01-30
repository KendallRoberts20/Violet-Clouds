import numpy as np 
import pandas as pd 


#making pandas dataframe
weather_df = pd.read_csv('WeatherEvents_Jan2016-Dec2022.csv')

#drop any rows with missing data
weather_df.dropna(inplace = True)

#print(weather_df["TimeZone"].nunique())

#make separate columns for the dates and the times 
weather_df[["StartDate(UTC)","StartTimeOnly(UTC)"]] = weather_df["StartTime(UTC)"].str.split(" ", expand = True)
weather_df[["EndDate(UTC)","EndTimeOnly(UTC)"]] = weather_df["EndTime(UTC)"].str.split(" ", expand = True)

#making the times zones into abbrievations for more conciseness
weather_df["TimeZone"] = weather_df["TimeZone"].map({"US/Mountain": "MST", "US/Central": "CST", "US/Eastern": "EST", "US/Pacific": "PST"})

weather_df.to_csv("WeatherUS.csv", index = True)