import os
import csv

budget_data_csv = os.path.join("Resources", "budget_data.csv")
analysis_txt = os.path.join("analysis", "analysis.text")

header = True
first_month = True
date_col = 0
profit_loss_col = 1

number_of_months = 0
net_total = 0
greatest_increase_month = ""
greatest_increase_amount = 0
greatest_decrease_month = ""
greatest_decrease_amount = 0
previous_profit_loss = 0
total_changes = 0


with open (budget_data_csv) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    for row in csvreader:
        if header:
            header = False
        else:
            number_of_months = number_of_months + 1
            current_profit_loss = int(row[profit_loss_col])
            net_total = net_total + current_profit_loss

            if first_month:
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
    
    output_list = [
       "Financial Analysis\n", 
        "------------------------\n",
        f'Total Months: {number_of_months}\n',
        f'Total: ${net_total}\n',
        f'Average Change: ${(total_changes / (number_of_months - 1)):.2f}\n',
        f'Greatest Increase in Profits: {greatest_increase_month} $({greatest_increase_amount})\n',
        f'Greatest Decrease in Profits: {greatest_decrease_month} $({greatest_decrease_amount})'
    ]
    for line in output_list:
        print(line)

    with open(analysis_txt, "w+") as output:
        output.writelines(output_list)
            
   
                                           
       

