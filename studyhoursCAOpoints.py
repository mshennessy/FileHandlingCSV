# G.Hennessy CUS
# Sample code for plotting histograms, scatter plots and pie-charts
# Scatter plot are for bi-variate data (eg study hours vs CAO Points)
# Histograms are for showing the distribution or spread of a single
# data point (eg CAO points)
# Pie charts require some data to the added up and aggregated.
# Note that the function dayBreakdown() on line 66 should be at
# the top of the file but I wanted to keep it with the pie chart code
# For plotting graphs
import matplotlib.pyplot as plt
# For producing statistical data
#import numpy as np
# For data analysis
import pandas as pd

#-------------------------------------------------------------------------------------------------------#
# Read from the csv file using pandas. Pandas returns a data structure
# called a dataframe df
df = pd.read_csv('studyvsCAOpoints.csv')

# Now read the contents of two columns into a pandas series (like an array/list)
studyHours = pd.Series(df["Hours of study"])
points = pd.Series(df["CAO points"])

# Initialise a figure and plot - we do this every time
# fig and ax are returned by pyplot and allow you to access
# the area around your graph (figure) and your graph (ax)
# Ax is short for Axis, but it applies to any graph including
# pie-charts below.
fig, ax = plt.subplots()

# The scatterplot will plot hours of study against CAO points
ax.set_xlabel('Hours of Study')
ax.set_ylabel('CAO Points')
ax.set_title('Scatterplot of Hours Study vs CAO Points')
plt.scatter(studyHours, points)

plt.show()

# Try a histogram 
fig, ax = plt.subplots()

# the histogram of the CAO Points Distribution
ax.set_xlabel('CAO Points')
ax.set_ylabel('Frequency')
ax.set_title('Histogram: Distribution of CAO Points')
plt.hist(points)
plt.show()

# the histogram of the Average Study Hours Distribution 
fig, ax = plt.subplots()

ax.set_xlabel('Hours of Study')
ax.set_ylabel('Frequency')
ax.set_title('Histogram: Distribution of Average Hours of Study per day')
plt.hist(studyHours)
plt.show()


# Now for something more complicated
# I am going to build up info for a new graph - 2 pie charts showing average
# hours breakdown for study, exercise and social media for males v females

# Function to take total hours for each activity, average them and return
# values in an ordered list
# We could call this function for all boys, all girls, all 19 year olds or whatever
def dayBreakdown(sleep,school,study,exercise,socials,count):
    breakdown=[]
    sleepHrs= sleep/count
    studyHrs= study/count
    exerciseHrs= exercise/count
    socialsHrs= socials/count
    otherHrs = 24-(sleepHrs+school+studyHrs+exerciseHrs+socialsHrs)
    breakdown.append(sleepHrs)
    breakdown.append(school)
    breakdown.append(studyHrs)
    breakdown.append(exerciseHrs)
    breakdown.append(socialsHrs)
    breakdown.append(otherHrs)
    return breakdown

# Initialise values
girlsStudyHrs = boysStudyHrs = girlsExerciseHrs = boysExerciseHrs = 0
girlsSleep = boysSleep = girlsSocials = boysSocials = 0
girlCount = boyCount = 0
# Loop through the whole dataframe, tallying stats for boys and girls
for i in range(len(df)):
    if df["Gender"][i] == "Male":
        boysStudyHrs += df["Hours of study"][i]
        boysExerciseHrs += df["Exercise"][i]
        boysSleep += df["Sleep"][i]
        boysSocials += df["Socials"][i]
        boyCount +=1
    else:
        girlsStudyHrs += df["Hours of study"][i]
        girlsExerciseHrs += df["Exercise"][i]
        girlsSleep += df["Sleep"][i]
        girlsSocials += df["Socials"][i]
        girlCount +=1

# Assume that all students spend an average of 8 hours in class
pieLabels = ["Sleep","School","Study","Exercise","Social Media", "Other"]
girlsPieList=dayBreakdown(girlsSleep,8,girlsStudyHrs,girlsExerciseHrs,girlsSocials,girlCount)
boysPieList=dayBreakdown(boysSleep,8,boysStudyHrs,boysExerciseHrs,boysSocials,boyCount)
print(pieLabels)
print(girlsPieList)
print(boysPieList)


# You call subplots this way
# 1,2 denotes 1 row, 2 columns - if you want to stack vertically, it would be 2,1
# figsize can be any size - try bigger or smaller
fig, (ax1,ax2) = plt.subplots(1,2,figsize=(10,10)) #ax1,ax2 refer to your two pies


# Pass the values, labels
# the autpct is optional - it shows the % of each wedge %1d%% rounds, %1.1f%% give one dec place
ax1.pie(girlsPieList,labels = pieLabels,autopct = '%1.2f%%') #plot first pie
ax1.set_title('Day Breakdown for Girls')

ax2.pie(boysPieList,labels = pieLabels,autopct = '%1d%%') #plot second pie
ax2.set_title('Day Breakdown for Girls')
plt.show()