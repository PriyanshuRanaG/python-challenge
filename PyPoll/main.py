# Import necessary libraries
import os
import csv

# Initialize variables to store the total number of votes and candidates' vote count
number_of_votes = 0
Canditate = {}  
max_votes = 0

# Open the election data file
with open('/Users/priyanshurana/Desktop/Starter_Code/PyPoll/Resources/election_data.csv', 'r', newline='') as file:
    Reader = csv.reader(file)
    next(Reader, None)  # Skip the header row

    # Iterate over each row in the CSV file
    for row in Reader:
        number_of_votes += 1  # Increment the total vote count
        candidate_name = row[2]  # Get the candidate's name from the row

        # Check if the candidate is already in the dictionary
        if candidate_name in Canditate:
            Canditate[candidate_name] += 1  # Increment the candidate's vote count
        else:
            Canditate[candidate_name] = 1  # Add a new candidate to the dictionary with one vote

# Determine the winner of the election
for candidate_name, votes in Canditate.items():
    if votes > max_votes:
        max_votes = votes
        winner = candidate_name  # Update the winner

# Print the election results to the console
print("Election Results")
print("-------------------------")
print(f"Total Votes: {number_of_votes}")
print("-------------------------")
for candidate_name, votes in Canditate.items():
    percentage = (votes / number_of_votes) * 100  # Calculate vote percentage
    print(f"{candidate_name}: {percentage:.3f}% ({votes})")
print("-------------------------")
print(f"Winner: {winner}")
print("-------------------------")

# Write the election results to a text file
with open('election_results.txt', 'w') as txt_file:
    txt_file.write("Election Results\n")
    txt_file.write("-------------------------\n")
    txt_file.write(f"Total Votes: {number_of_votes}\n")
    txt_file.write("-------------------------\n")
    for candidate, votes in Canditate.items():
        percentage = (votes / number_of_votes) * 100  # Calculate vote percentage
        txt_file.write(f"{candidate}: {percentage:.3f}% ({votes})\n")
    txt_file.write("-------------------------\n")
    txt_file.write(f"Winner: {winner}\n")
    txt_file.write("-------------------------\n")

