# This library saves us all the trouble of having
# to split the input into comma separated values
# and new lines
# A python list is automatically added as a row
# to the CSV file.

import csv

# This is a not on your reference guide, but "with open()"
# is a handier way to open a file, as it is
# automatically closed after (no need for file.close()
with open("student.csv","a",newline = "") as file:
    db = csv.writer(file)
    header = ["firstname","lastname","phone"]
    db.writerow(header)
    db.writerow(["Jim","Jarmusch","01234444"])
    db.writerow(["Wim","Wenders","9799798"])
    db.writerow(["Lars","vonTrier","887711"])

print("All done ... check your CSV file")
print("what happens if you run me again? (What does the \"a\" do in line 12?")