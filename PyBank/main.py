import os
import csv
from pathlib import Path

# Define varialbes, since we have to count the total and changes as a numric value I define them as empty lists
# total_months [] is bringing the first column related to months and date, and total_profit [] is bringing secnd column related to Profit/Loss and monthly_change[] is calculating the change
total_months = []
total_profit = []
monthly_change = []

csv_path = Path('./Resources/budget_data.csv').expanduser()

# Start working on the csv file by using with comand which open the file to apply the changes
with csv_path.open('r', newline='', encoding='utf-8') as csvfile:
    csvreader = csv.reader(csvfile)
    
    # Skip the header labels to just go with the values from secoond row (I search what is equal to header=None -as in Pandas- in python)
    header = next(csvreader)
    
    # Going through the rows in the stored file contents
    for row in csvreader: 
        # Append and add up the total months and total profit to their defined lists
        total_months.append(row[0])
        total_profit.append(int(row[1]))

# Going through the profits(second column) to calculate the monthly change in profits
for i in range(len(total_profit) - 1):
    # The difference between two months will show profit or loss, we add to montly-change list
    monthly_change.append(total_profit[i + 1] - total_profit[i])
        
# The maximum and minimum of the monthly profit change list will give us the highest and lowest
max_value = max(monthly_change)
min_value = min(monthly_change)

# Define maximun and minimun to the proper month (index which is in column one) using month list and index which is come from maximun and minimun
# After search with google help I use the plus 1 at the end since the month related to the change we look for is coming from the next month that we show by + 1
# I define min_increase instead of max_decrease to make it more understandable for myself (As biggest loss)

max_increase_month = monthly_change.index(max_value) + 1
min_increase_month = monthly_change.index(min_value) + 1 

# Print Statements as requested in challenge

print("Financial Analysis")
print("----------------------------")
print(f"Total Months: {len(total_months)}")
print(f"Total: ${sum(total_profit)}")
print(f"Average Change: {round(sum(monthly_change) / len(monthly_change), 2)}")
print(f"Greatest Increase in Profits: {total_months[max_increase_month]} (${max_value})")
print(f"Greatest Decrease in Profits: {total_months[min_increase_month]} (${min_value})")

# Output files
output_file = Path('./analysis/Analysis_Summary.txt')

with open(output_file, "w") as file:
    # Write methods to print to Financial_Analysis_Summary 
    file.write("Financial Analysis\n")
    file.write("----------------------------\n")
    file.write(f"Total Months: {len(total_months)}\n")
    file.write(f"Total: ${sum(total_profit)}\n")
    file.write(f"Average Change: {round(sum(monthly_change) / len(monthly_change), 2)}\n")
    file.write(f"Greatest Increase in Profits: {total_months[max_increase_month]} (${max_value})\n")
    file.write(f"Greatest Decrease in Profits: {total_months[min_increase_month]} (${min_value })\n")



