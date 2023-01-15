# First we'll import the os module
# This will allow us to create file paths across operating systems
import os

# Module for reading CSV files
import csv

# Set path for file
budget_csv = os.path.join ('Resources','budget_data.csv')

# CSV reader specifies delimiter and variable that holds contents
# # Open the CSV
with open(budget_csv,encoding='utf') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

# Read the header row first (skip this step if there is now header)
    csv_header = next(csvreader)
    print(f"CSV Header: {csv_header}")

# # Read each row of data after the header
#     for row in csvreader:
#         print(row)

# Calculat total number of months in dataset
    months = 0
    net_total = 0
    previous_profit = 0
    change = 0
    total_change=0
    change_periods=0
    profit_loss = []
    changes_entire =[]

    for row in csvreader:

        months += 1

        net_total += int(row[1])

        profit_loss = int(row[1])
        if previous_profit != 0:
            change = profit_loss - previous_profit
            changes_entire.append(change)
            total_change += int(change)
            change_periods +=1
        previous_profit = profit_loss
    
    average_change = round((total_change / change_periods), 2)

    #     profit_loss = int(row[1])
    #     if previous_profit != 0:
    #         change = profit_loss - previous_profit
    #         changes_entire.append(change)
    #     previous_profit = profit_loss
    
    # average_change = round((sum(changes_entire) / len(changes_entire)), 2)
    
    print(f'Total Months = {months}')
    print(f'Total: ${net_total}')
    print(f'Average Change: ${average_change}')




# # Write a function that returns the arithmetic average for a list of numbers
# def average(numbers):
#     length = len(numbers)
#     total = 0.0
#     for number in numbers:
#         total += number
#     return total / length


# # Test your function with the following:
# print(average([1, 5, 9]))
# print(average(range(11)))

# # Specify the file to write to
# output_path = os.path.join("Analysis", "Results.txt")
# # Open the file using "write" mode. Specify the variable to hold the contents
# with open(output_path, 'w') as datafile:

#     # Initialize csv.writer
#     writer = csv.writer(datafile)

#     # Write the first row (column headers)
#     writer.writerow(['First Name', 'Last Name', 'SSN'])

#     # Write the second row
#     writer.writerow(['Caleb', 'Frost', '505-80-2901'])

#  writer.writerows(roster)