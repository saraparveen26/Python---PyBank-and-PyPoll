# **Python-Challenge**

This repository is created to submit Challenge # 3 for Data Analytics Bootcamp at University of Toronto. In this challenge, we were given two CSV files as a resource. We were required to create Python scripts to analyze the data in these CSV files and export the outputs to text files in the respective folders.

There are two separate folders created for the two parts of the challenge: PyBank and PyPoll. Each of these folders contain:
    - Resources folder containing the original CSV file
    - main.py Python file containing the script
    - Analysis folder containing the output Text file created as a result of running the script

## **PyBank:**

As first part of the challenge, I used Python script to analyze the data in the CSV file for budget. The original data contains two columns: Date and Profit/ Losses. The script starts by importing the modules for OS and CSV, setting the path for source file, and reading the header. In the next step, I declared some variables, and initiated lists and disctionaries to store data.

The script then loops through the entire data in CSV. It firsts stores the data in both Data and Profit/Losses to two separate lists. Then the values in Profit/Losses dataset are added to calculate the Net Total Amount of Profit/ Losses. 

In order to calculate and store the Changes in Profit/ Losses over the entire period, the Changes are calculated by subtracting the value in the previous row from the value in the cutrrent row. An If statement is used to only perform the subtraction if the previous row is not blank: this excludes calculating the change for the first value in Profit/ Losses as we do not have a preceding value to compare. All the change values are stored in a list, and a cumulative total change value is updated as the data is iterated. 

If statements are used to calculate the Greatest Increase and Decrease in Profits and the respective dates. An initial value of zero is assigned for the profit when dictionaries were created in the beginning. The script compares each change amount to the initial value and updates it to the change amount if it is higher/ lower to calculate the greatest increase/ decrease. The respective dates are also stored to the dictionary. 

The Total number of Months in the dataset are then derived by calculating the length of the list creatred to store all dates. 

The Average of all Changes is calculated by dividing the amount in Total Change by the length of the list containing all Changes. The result is rounded to 2 decimals.

In the next step, all the results are printed to the terminal.

Finally, an output path is initiated to create a Text file. The text file is then written to store the Analysis results.

## **PyPoll:**

As first part of the challenge, I used Python script to analyze the data in the CSV file for elections. The original data contains three columns: Ballot ID, County and Candidate. The script starts by importing the modules for OS and CSV, setting the path for source file, and reading the header. In the next step, I declared some variables, and initiated lists to store data. The required analysis will mostly be based on data under the heaeder "Candidate".

The script then loops through the entire data in CSV. It firsts stores the data under Candidate to a list. Then the Total number of Votes casted are calculated by adding the number of entries as we iterate through the entire loop. An alternate way of calculating total number of votes is to count the length of any lists created to store data under any of the headers. I had used that method in the PyBank challenge.

In the next step, a list contaning Unique names of Candidates is created. This is done by comparing the value in each row under Candidate to eisting values in the list containing Unique names.

Another nested loop is then started to calculate total votes and percentage of votes for each candidate. First, the name in the list containing all entries for Candidate is compared with the name in the list containing only unique names. For each incidence of the unique name in the total candidate list, 1 vote is added for that unique candidate's Total vote count. Once all the votes are added up for that particular candidate, the total number of votes for that candidate is divided by the total votes casted calculated earlier to derive the Percentage of votes for each unique candidate. The percentage number is rounded to 3 decimals. The values for Total counts and Percentage of Votes for each unique candidate are stored in two separate lists.

The Winner of the elections is then identified based on popular vote. This is done by comparing the total votes for each candidate with the votes for winner (it was initally assigned a value of zero) within the nested loop created above. If the total votes of candidate are higher than the vote count for winner, then the winner vote count is updated to that number. The winner name is also updated to the unique candidate name currently being reviewed under the loop. 

The total vote count for each unique candidate is then reset to zero at the end of the loop to start fresh calculations for the next unique candidate name.

In the next step, all the results are printed to the terminal. A loop is used to zip the values from the three lists created for unique candidate name, total vote count for each candidate, and percentage of votes for each candidate. This zipping allows to print the respective values in each of these three lists in one statement. 

Finally, an output path is initiated to create a Text file. The text file is then written to store the Analysis results.

## **Conclusion**

PyBank and PyPoll exercises were a great practice for me to practice my Python programming skills and problem solving. It gave me an opportunity to test different concepts and logics we learnt in the class in order to perform a meaningful analysis on large datasets.