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
    winner_vote_count = 0
    winner = ""

# Declare/ initiate Lists and Dictionaries to store values
    total_candidate_list =[]
    stats = {{"candidate":[]}, {"percentage": []}, {"count": []}}


# Loop through the full dataset

    for row in csvreader:

        # Create List to store all entries for Candidates
        total_candidate_list.append(row[2])

        # Calculate Total Number of Votes cast by counting total number of data entries
        total_vote_count += 1

        # Create List of Unique Candidate names
        candidate = row[2]
        if candidate not in stats['candidate']:
            stats['candidate'].append(candidate)
 

# Calculate Total Number and Percentage of Votes for each Candidate, and name of Winner
# Loop through Unique Candidate list and within that loop through the list of all Candidate name entries
    
    for candidate_name in stats['candidate']:

        for total in total_candidate_list:

            # Calculate total and percentage votes for each Unique Candidate name
            if total == candidate_name:
                candidate_vote_count += 1

        candidate_vote_percentage = round(((candidate_vote_count/total_vote_count)*100),3)

        # Create Lists to Store Total and Percentage Votes for each Candidate
        stats['count'].append(candidate_vote_count)
        stats['percentage'].append(candidate_vote_percentage)

        # Identify the Winner of election based on popular vote
        if candidate_vote_count > winner_vote_count:
            winner_vote_count = candidate_vote_count
            winner = candidate_name

        # Reset the Total Vote count for candidates
        candidate_vote_count = 0





print(f'Election Results')
print('----------------------------')
print(f'Total Votes = {total_vote_count}')
print('----------------------------')

for each in stats:
    print(f'{stats[candidate]}: {stats[percentage]}% ({stats[count]})')
print('----------------------------')
# print(f'{stats["candidate"]}')
# print(f'{stats["count"]}')
# print(f'{stats["percentage"]}%')  
print(f'{winner}')
print('----------------------------')