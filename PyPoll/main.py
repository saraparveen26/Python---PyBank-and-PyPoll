# Import the OS module to create file paths across operating systems
import os

# Import module for reading CSV files
import csv

# Set path for the source file
election_csv = os.path.join ('Resources','election_data.csv')

# Open and read the CSV source file
# Specify the delimiter and CSV reader variable to hold content
with open(election_csv,encoding='utf') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

# Read the header row and print it
    csv_header = next(csvreader)
    print(f"CSV Header: {csv_header}")


# Declare Variables for data analysis and their starting values
    total_votes = 0
    # net_total = 0
    # previous_profit = 0
    # change = 0
    # total_change = 0
    # change_periods = 0

# Declare/ initiate Lists and Dictionaries to store values
    ballot_list = []
    # county_list = []
    candidate_list =[]


# Loop through the data

    for row in csvreader:

        # Create List to store source data for 'Ballots' and 'Profit/Losses' separately
        ballot_list.append(row[0])

        
        # Calculate Total Number of Votes cast by counting total number of data entries
        total_votes += 1


        # Create List of Candidates who received votes




print(f'Election Results')
print('----------------------------')
print(f'Total Votes = {total_votes}')
print('----------------------------')
# print(f'Total: ${net_total}')
# print(f'Average Change: ${average_change}')
# print(f'Greatest Increase in Profits: {increase["date"]} (${increase["amount"]})')
# print(f'Greatest Decrease in Profits: {decrease["date"]} (${decrease["amount"]})')