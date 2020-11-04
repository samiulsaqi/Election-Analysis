# Add our dependencies.
import csv
import os
# Assign a variable to load a file from a path.
file_to_load = os.path.join("Resources", "election_results.csv")
# Assign a variable to save the file to a path.
file_to_save = os.path.join("analysis", "election_analysis.txt")

#create variable for total votes
total_votes=0

#create list of candidates, candidate votes, winning candidate name, percentage and number of votes
candidates_option = []
candidate_votes ={}
winning_candidate =""
winning_vote = 0
winning_percentage = 0

# Open the election results and read the file.
with open(file_to_load) as election_data:
    file_reader = csv.reader(election_data)

    # Read the header row.
    headers = next(file_reader)
    
    #print each row in the csv file
    for row in file_reader:
        #increase total vote
        total_votes+=1
        #add unique candidate name in cadidates option list
        candidate_name=row[2]
        if candidate_name not in candidates_option:
            candidates_option.append(candidate_name)
            #begin tracking candidate votes
            candidate_votes[candidate_name] = 0
            #add a vote for the candidate
        
        candidate_votes[candidate_name] +=1

# determine the percentage of votes won by each candidate
for candidate_name in candidate_votes:
    #retrive vote count for each candidate
    votes = candidate_votes[candidate_name]
    #calculate % of vote
    vote_percentage= float(votes)/float(total_votes)*100
    #print candidate name and vote percentage
    print(f"{candidate_name}: received {vote_percentage:.2f}% of the vote")

    #determine winning candidate, votes and percentage
    if vote_percentage>winning_percentage:
        winning_candidate = candidate_name
        winning_percentage = vote_percentage
        winning_vote = votes

#print winning candidate name, total votes won and percentage of vote won
print(f"The winner is {winning_candidate}, who won a total of {winning_vote} votes, which is {winning_percentage:.2f}% of total votes")
