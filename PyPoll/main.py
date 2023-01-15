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
    total_vote_count = 0
    candidate_vote_count = 0

# Declare/ initiate Lists and Dictionaries to store values
    total_candidate_list =[]
    unique_candidate_list =[]
    total_votes_list =[]
    percentage_votes_list =[]


# Loop through the data

    for row in csvreader:

        # Create List to store all entries for Candidates
        total_candidate_list.append(row[2])

        
        # Calculate Total Number of Votes cast by counting total number of data entries
        total_vote_count += 1


        # Create List of Candidates who received votes
        candidate = row[2]
        if candidate not in unique_candidate_list:
            unique_candidate_list.append(candidate)
 

# Calculate Total Number and Percentage of Votes for each Candidate
    for candidate_name in unique_candidate_list:
        for total in total_candidate_list:
            if total == candidate_name:
                candidate_vote_count += 1
        total_votes_list.append(candidate_vote_count)
        candidate_vote_percentage = round(((candidate_vote_count/total_vote_count)*100),3)
        percentage_votes_list.append(candidate_vote_percentage)

        candidate_vote_count = 0



print(f'Election Results')
print('----------------------------')
print(f'Total Votes = {total_vote_count}')
print('----------------------------')
print(f'{unique_candidate_list}')
print(f'{total_votes_list}')
print(f'{percentage_votes_list}%')  
# print(f'Total: ${net_total}')
# print(f'Average Change: ${average_change}')
# print(f'Greatest Increase in Profits: {increase["date"]} (${increase["amount"]})')
# print(f'Greatest Decrease in Profits: {decrease["date"]} (${decrease["amount"]})')