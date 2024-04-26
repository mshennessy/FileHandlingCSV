# G. Hennessy CUS
# This is a demo of a multi-line trend graph
# reading the data from a file called wrappers.csv
# using pandas and matplot lib

# For plotting graphs
import matplotlib.pyplot as plt

# For data analysis
import pandas as pd

#-------------------------------------------------------------------------------------------------------#
# Read from the csv file using pandas. Pandas returns a data structure
# called a dataframe df
df = pd.read_csv('wrappers.csv')
print (df)
# This is how we read the headings, but as our data
# goes Artist, 2000,2001,2002,2003... we just want
# from the 2nd element to the end - hence the [1:]
headings = list(df.columns.values)[1:]

# Define the size of your graph. This is big so we can read the years
plt.figure(figsize=(20,10))

# Now loop through each row of the dataframe
for x in range(len(df)):
    #Read a row from dataframe
    artist = df.iloc[x]
    # plot list of values from second column to the end [1:]
    # the label will be the artist name in the first column [0]
    # this will plot the value under 2000, 2001, 2002 etc
    # the label= part will be used in the legend
    plt.plot(headings,artist[1:], label=artist[0])
# Add labels and legend
plt.xlabel('Years') 
plt.ylabel('Income') 
plt.title("Successful wrappers")  
plt.legend()
# Often forgotten ... you have to show your plot
plt.show()
