import os
import csv

# Store Data

poll = {}
candidates = []
number_votes = []
vote_percent = []
winner_list = []
total_votes = 0

# Path for file election
election = os.path.join('resources', 'election_data.csv')

# Split file
with open(election, 'r') as csvfile:
    csvread = csv.reader(csvfile)
    next(csvread)

# Add total vote count for each loop
    for row in csvread:
        total_votes += 1
        if row[2] in poll.keys():
            poll[row[2]] = poll[row[2]] + 1
        else:
            poll[row[2]] = 1
 
# Append keys and number vote 
for key, value in poll.items():
    candidates.append(key)
    number_votes.append(value)

# Vote percent
for n in number_votes:
    vote_percent.append(round(n/total_votes*100, 1))

# Zip data 
clean_data = list(zip(candidates, number_votes, vote_percent))

# Winner list 
for name in clean_data:
    if max(number_votes) == name[1]:
        winner_list.append(name[0])
winner = winner_list[0]

# Winners list added
if len(winner_list) > 1:
    for w in range(1, len(winner_list)):
        winner = winner + ", " + winner_list[w]

# Path for election file
analysis = os.path.join('..','analysis', 'election_results.txt')

# Election text
with open(analysis, 'w') as text:
    text.write('Election Results\n')
    text.write('-------------------------\n')
    text.write('Total Votes: ' + str(total_votes) + '\n')
    text.write('-------------------------\n')
    for entry in clean_data:
        text.write(entry[0] + ": " + str(entry[2]) +'%  (' + str(entry[1]) + ')\n')
    text.write('------------------------- \n')
    text.write('Winner: ' + winner + '\n')
    text.write('-------------------------')

# Print election
with open(analysis, 'r') as readfile:
    print(readfile.read())
