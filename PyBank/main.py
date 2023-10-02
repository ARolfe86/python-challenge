'''
Module 3 PyBank Project

This program analyzes the dataset with two columns for Date and Profit/Losses. 
It calculates the total number of months included in the dataset, the net total
amount of Profit/Loss over the entire period, the changes in Profit/Losses over
the entire period, then averaging those changes, the greatest increase in profits
over the entire period and the greatest decrease in profits over the entire period.
'''


# Import needed libraries
import os
import csv

# Set up input and output file variables
budget_data_csv = os.path.join("Resources", "budget_data.csv")
analysis_txt = os.path.join("analysis", "analysis.text")

# Local variables
header = True                # boolean that is true when the header row has not been processed
first_month = True           # boolean is true if we are on the first month
date_col = 0                 # index of the date column
profit_loss_col = 1          # index of the profit/loss column

number_of_months = 0         # total number of months for the report
net_total = 0                # sum of the profit and losses
greatest_increase_month = "" # month of greatest increase in profit
greatest_increase_amount = 0 # the amount of the greatest increase in profit
greatest_decrease_month = "" # month of the greatest decrease in profit
greatest_decrease_amount = 0 # the amount of the greatest decrease in profit
previous_profit_loss = 0     # the profit or loss from the previous month to calculate the current change
total_changes = 0            # sum of the monthly changes


# open the budget data csv file and set up a csv reader
with open (budget_data_csv) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    
    # process each row of the budget data
    for row in csvreader:
        if header:
            # the first row is the header, do nothing and set header variable to false
            header = False
        else:
            number_of_months = number_of_months + 1
            current_profit_loss = int(row[profit_loss_col])
            net_total = net_total + current_profit_loss

            if first_month:
                # there is no change to calculate for the first month of data
                first_month = False
            else: 
                current_change = current_profit_loss - previous_profit_loss 
                total_changes = total_changes + current_change

                if current_change > greatest_increase_amount:
                    greatest_increase_amount = current_change
                    greatest_increase_month = row[date_col]

                if current_change < greatest_decrease_amount:
                    greatest_decrease_amount = current_change
                    greatest_decrease_month = row[date_col]
            
            previous_profit_loss = current_profit_loss
    
    # create a list of lines to be output to the terminal and a text file
    output_list = [
       "Financial Analysis\n", 
        "------------------------\n",
        f'Total Months: {number_of_months}\n',
        f'Total: ${net_total}\n',
        f'Average Change: ${(total_changes / (number_of_months - 1)):.2f}\n',
        f'Greatest Increase in Profits: {greatest_increase_month} $({greatest_increase_amount})\n',
        f'Greatest Decrease in Profits: {greatest_decrease_month} $({greatest_decrease_amount})'
    ]

    # output to terminal
    for line in output_list:
        print(line)

    # output to file
    with open(analysis_txt, "w+") as output:
        output.writelines(output_list)
            