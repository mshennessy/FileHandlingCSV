# G. Hennessy
# Sample code to open a CSV file and produce a scatter plot

import csv                          # library to handle CSV
import matplotlib.pyplot as plt     # for plotting graphs

# In this example we will see if there is a correlation between hours
# of study (average per day) and CAO points achieved.
# We will read those two columns from the CSV file and store the contents in
# two lists (hours and points) and then pass these lists to the matplotlib tool
# Initialize lists for data from the CSV file
hours = []
points = []

# Open the CSV file using standard file open function
f = open('studyvsCAOpoints.csv', 'r')
# Read from file using CSV reader method which takes care
# of all the formatting issues such as \n etc
csv_reader = csv.DictReader(f)
# For loop which processes the object csv_reader row by row
for row in csv_reader:
    # All data read from a CSV file is automatically a string (even numeric data)
    # so we have to turn it into an integer or float(decimal) 
    hours.append(float(row['Hours of study']))
    points.append(int(row['CAO points']))  # Convert medals to integer
# Close the file
f.close()

print("Hours list:",hours)
print("Points list:",points)
# Create a scatter plot using matplotlib
plt.figure(figsize=(8, 8))
plt.scatter(hours, points) #, s=area, c=colors, alpha=0.5)
plt.title('CAO Points versus hours of study')
plt.xlabel("Average hours of study per day")
plt.ylabel("CAO points achieved")
# Optional saving my graph in a .png file
plt.savefig('CAOScatter.png')
plt.show()






