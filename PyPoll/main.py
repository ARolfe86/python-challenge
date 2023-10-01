import os
import csv

election_data_csv = os.path.join("Resources", "election_data.csv" )
analysis_txt = os.path.join("analysis", "analysis.text")

header = True
candidate = dict()
candidate_col = 2
number_of_votes = 0
most_votes = 0
winning_candidate = ""


with open (election_data_csv) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    for row in csvreader:

        if header:
            header = False
        else:
            number_of_votes = number_of_votes + 1
            name = row[candidate_col]
            votes= candidate.get(name, 0) + 1
            candidate[name] = votes

    for name in candidate.keys():
        print(f'{name} votes {candidate[name]} {candidate[name]/number_of_votes}')
    
    print(number_of_votes)

    output_list = [
        "Election Results\n",
        "--------------------\n",

        f'Total Votes: {number_of_votes}\n',

        "---------------------\n",

    ]
    for name in candidate.keys():
        vote_percentage = (candidate[name]/number_of_votes) * 100
        output_list.append(f'{name:} {vote_percentage:.3f}% ({candidate[name]})\n')
        
        if candidate[name] > most_votes:
            most_votes = candidate[name]
            winning_candidate = name

    output_list.append("---------------------\n")
    output_list.append(f'Winner: {winning_candidate}\n')
    output_list.append("---------------------\n")
    
    
    for line in output_list:
        print(line)  

    with open(analysis_txt, "w+") as output:
        output.writelines(output_list)         
          
    
                



