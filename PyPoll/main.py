# First we'll import the os module
# This will allow us to create file paths across operating systems
import os

# Module for reading CSV files
import csv

#     # Read the header row first (skip this step if there is now header)
#     csv_header = next(csvreader)
#     print(f"CSV Header: {csv_header}")

# Set path for file
csvpath = os.path.join ("Resources", "election_data.csv")

# CSV reader specifies delimiter and variable that holds contents
# Open the CSV
with open(csvpath,encoding='utf') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    print(csvreader)

# Read the header row first (skip this step if there is now header)
    csv_header = next(csvreader)
    print(f"CSV Header: {csv_header}")

# Read each row of data after the header
    for row in csvreader:
        print(row)


   