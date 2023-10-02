'''
Module 3 PyPoll Project

This program analyzes a dataset with three columns for Ballot Id, 
County and Candidate. It calculates the total number of votes cast, 
lists each candidate that received votes, the number of votes each
candidate received, the percentage of the votes won by each candidate
and the winner of the election based on popular vote. It presents output 
to the terminal and also saves the output in a text file.
'''

# Import needed libraries
import os
import csv

# Set up input and output file variables 
election_data_csv = os.path.join("Resources", "election_data.csv" )
analysis_txt = os.path.join("analysis", "analysis.text")

# Local variables
header = True           # boolean that is true when the header row has not been processed
candidate = dict()      # dictionary using the candidate name as a key and storing the number of votes as a value
candidate_col = 2       # index in the csv file of the candidate name column
number_of_votes = 0     # number of votes cast
most_votes = 0          # stores the votes of the candidate that received the most votes
winning_candidate = ""  # name of the winning candidate


# open the election data csv file and set up a csv reader
with open (election_data_csv) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    
    # process each row of election data
    for row in csvreader:

        if header:
            # the first row is the header, do nothing and set header variable to false
            header = False
        else:
            number_of_votes = number_of_votes + 1
            name = row[candidate_col]
             
            # get the votes for the candidate in this row, if the candidate is not already
            # in the dictionary, return a default value of 0
            votes= candidate.get(name, 0) + 1
            candidate[name] = votes

    # create a list of lines to be output to the terminal and a text file
    output_list = [
        "Election Results\n",
        "--------------------\n",
        f'Total Votes: {number_of_votes}\n',
        "---------------------\n"
    ]  
     
    # add the candidate information to the output list
    for name in candidate.keys():
        vote_percentage = (candidate[name]/number_of_votes) * 100
        output_list.append(f'{name:} {vote_percentage:.3f}% ({candidate[name]})\n')
        
        if candidate[name] > most_votes:
            most_votes = candidate[name]
            winning_candidate = name

    # add the winner to the output list
    output_list.append("---------------------\n")
    output_list.append(f'Winner: {winning_candidate}\n')
    output_list.append("---------------------\n")
    
    # output to terminal 
    for line in output_list:
        print(line)  

    # output to file
    with open(analysis_txt, "w+") as output:
        output.writelines(output_list)         
          