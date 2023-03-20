# import election_data.csv
import csv
import os


# Set path for file
election_data_csv = os.path.join("election_data.csv")

# Initialize variables
total_votes = 0
candidates = []
candidate_votes = {}

# Read in the CSV file
with open(election_data_csv, 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')

    # Skip the header row
    header = next(csvreader)

    # Loop through the data
    for row in csvreader:
        # Count the total number of votes cast
        total_votes += 1

        # Extract the candidate name from the row
        candidate_name = row[2]

        # Add the candidate to the list of candidates (if not already in the list)
        if candidate_name not in candidates:
            candidates.append(candidate_name)

        # Add a vote to the candidate's total vote count
        if candidate_name in candidate_votes:
            candidate_votes[candidate_name] += 1
        else:
            candidate_votes[candidate_name] = 1

# Initialize variables for storing the winner and the winner's vote count
winner = ""
winner_count = 0

# Print the election results
print("Election Results")
print("-------------------------")
print(f"Total Votes: {total_votes}")
print("-------------------------")

# Loop through the list of candidates
for candidate in candidates:
    # Calculate the percentage of votes and the total number of votes for the candidate
    votes = candidate_votes[candidate]
    vote_percentage = round(votes / total_votes * 100, 3)

    # Print the candidate's name, percentage of votes, and total number of votes
    print(f"{candidate}: {vote_percentage}% ({votes})")

    # Check if the candidate has the highest number of votes so far
    if votes > winner_count:
        winner = candidate
        winner_count = votes

print("-------------------------")
print(f"Winner: {winner}")
print("-------------------------")
