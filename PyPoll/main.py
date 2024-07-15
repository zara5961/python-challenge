import os
import csv
from pathlib import Path

csv_path = Path('./Resources/election_data.csv').expanduser()

    # Define Variables 
total_votes = 0 
Charles_votes = 0
Diana_votes = 0
Raymon_votes = 0

    # Define Lists 
candidates = []
votes = []


# Start working on the csv file by using with comand which open the file to apply the changes
with csv_path.open('r', newline='', encoding='utf-8') as csvfile:
    csvreader = csv.reader(csvfile)

    for row in csvreader:
        # Count the Ballot ID to have the total amount of votes and store in a new variable as total_votes
        total_votes +=1

        # There are three candidates in the csv file (Track by filter), start going row by row and if we find exact name of the any candidate add the number of repetion of the name in a list
        
        if row[2] == "Charles Casper Stockham": 
            Charles_votes +=1
        elif row[2] == "Diana DeGette":
            Diana_votes +=1
        elif row[2] == "Raymon Anthony Doane": 
            Raymon_votes +=1


     # NOw we have the total number for each name
     # I add names and numbers separetly in the lists
candidates = ["Charles Casper Stockham", "Diana DeGette", "Raymon Anthony Doane"]
votes = [Charles_votes, Diana_votes, Raymon_votes]

# I zip(paire the elements from two lists ) them together as a dictionary with key value of candidates and the value of total votes
# If I run max function on the dictionary and request for the key which has highest value I will have the winner
# I found zip function with the help of google!
 
dict_total = dict(zip(candidates,votes))
win = max(dict_total, key=dict_total.get)

 
# The values I had for each candidate divided by total votes and times to 100 will give the % of the vote
# Print a the summary of the analysis
Charles_percent = (Charles_votes/total_votes) *100
Diana_percent = (Diana_votes/total_votes) * 100
Raymon_percent = (Raymon_votes/total_votes)* 100


# Print a the summary of the analysis 
print(f"Election Results")
print(f"----------------------------")
print(f"Total Votes: {total_votes}")
print(f"----------------------------")
print(f"Charles Casper Stockham: {Charles_percent:.3f}% ({Charles_votes})")
print(f"Diana DeGette: {Diana_percent:.3f}% ({Diana_votes})")
print(f"Raymon Anthony Doane: {Raymon_percent:.3f}% ({Raymon_votes})")
print(f"----------------------------")
print(f"Winner: {win}")
print(f"----------------------------")

# Output files
# To have a text file I assign file location in analysis folder and with the help of google with Write methods add to Elections_Summary 
output_file = Path('./analysis/Election_Summary.txt')

with open(output_file,"w") as file:

    file.write(f"Election Results")
    file.write("\n")
    file.write(f"----------------------------")
    file.write("\n")
    file.write(f"Total Votes: {total_votes}")
    file.write("\n")
    file.write(f"----------------------------")
    file.write("\n")
    file.write(f"Charles Casper Stockham: {Charles_percent:.3f}% ({Charles_votes})")
    file.write("\n")
    file.write(f"Diana DeGette: {Diana_percent:.3f}% ({Diana_votes})")
    file.write("\n")
    file.write(f"Raymon Anthony Doane: {Raymon_percent:.3f}% ({Raymon_votes})")
    file.write("\n")
    file.write(f"----------------------------")
    file.write("\n")
    file.write(f"Winner: {win}")
    file.write("\n")
    file.write(f"----------------------------")


