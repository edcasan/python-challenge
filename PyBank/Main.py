import os
import csv

# Store data
months = []
profits = []
change_list=[]
greatest_increase = 0
greatest_decrease = 0
change=0

# Path for file budget
budget = os.path.join('Resources', 'budget_data.csv')

# Split file into List
with open(budget) as csvfile:
    csvread = csv.reader(csvfile, delimiter=',')
    next(csvread) 

# Profits list 
    for row in csvread:
        months.append(row[0])
        profits.append(int(row[1]))

# Profits
profits = [int(row) for row in profits]

# Loop profits 
for i in range(len(profits)):
    if i < len(profits) - 1:
        change = change + (profits[i + 1] - profits[i])
        change_list.append(change)
        change = 0

# Calculations of profits to total 
average_change = round(sum(change_list) / len(change_list),2)
greatest_increase = max(change_list)
greatest_decrease = min(change_list)
greatest_decrease_month = change_list.index(greatest_decrease)
greatest_increase_month = change_list.index(greatest_increase)

# Variables for greatest and least month
greatest_month = months[greatest_increase_month+1]
least_month = months[greatest_decrease_month+1]

# Path for analysis file
analysis = os.path.join('..','analysis','financial_analysis.txt')

# Analysis text 
with open(analysis, 'w') as text:
    text.write('Financial Analysis\n')
    text.write('----------------------------' + '\n')
    text.write('Total Months: ' + str(len(months)) + '\n')
    text.write('Total: $' + str(sum(profits)) + '\n')
    text.write('Average Change: $' + str((average_change)) + '\n')
    text.write('Greatest Increase in Profits: ' + greatest_month + ' ($' + str(greatest_increase) + ')'+ '\n')
    text.write('Greatest Decrease in Profits: ' + least_month + ' ($' + str(greatest_decrease) + ')')

# Print Analysis  
with open(analysis, 'r') as readfile:
    print(readfile.read())

