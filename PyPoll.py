## PyPoll
#In this challenge, you are tasked with helping a small, rural town modernize its vote-counting process. 
# #(Up until now, Uncle Cleetus had been trustfully tallying them one-by-one, but unfortunately, his concentration isn't what it used to be.)
#You will be give a set of poll data called [election_data.csv](PyPoll/Resources/election_data.csv). The dataset is composed of three columns:
# `Voter ID`, `County`, and `Candidate`. Your task is to create a Python script that analyzes the votes and calculates each of the following:

#modules (libraries)
import os
import csv

#set file path
file_to_load = os.path.join("Resources", "election_data.csv")
file_to_output = os.path.join("analysis", "election_analysis.txt")

candidate_options = []
votes_earned = {}

#acknowledge header
#csv_header = next(csvreader)
#first_row = next(csvreader)
#candidate_options.append(first_row[0])

total_votes = 0

#counter for votes and candidates
winner = ""
winning_count = 0

#read and open csv
with open(file_to_load) as election_data:
    csvreader = csv.DictReader(election_data)

    #acknowledge header
    csv_header = next(csvreader)
    first_row = next(csvreader)
    #candidate_options.append(first_row[0])

    for row in csvreader:

        #print(". ", end=""),

        total_votes = total_votes + 1

        #pull candidate name out of list
        candidate_name = row["Candidate"]

        #create loop in case candidate is not found
        if candidate_name not in candidate_options:

            candidate_options.append(candidate_name)
            votes_earned[candidate_name] = 0

        votes_earned[candidate_name] = votes_earned[candidate_name] + 1

#print results in text file
with open(file_to_output, "w") as txt_file:

    #print final vote counts formatted 
    election_results = (
        f"\nElection Results\n"
        f"Total Votes: {total_votes}\n")
    print(election_results, end="")

    #save final vote count to text file
    txt_file.write(election_results)

    #Find the winner loop
    for candidate in votes_earned:

        #get vote count and %
        votes = votes_earned.get(candidate)
        vote_percentage = float(votes) / float(total_votes) * 100

        #Find winning candidate
        if (votes > winning_count):
            winning_count = votes
            winner = candidate

        #Print output
        voter_output = f"{candidate}: {vote_percentage:.3f}% ({votes})\n"
        print(voter_output, end="")

        #Save to text file
        txt_file.write(voter_output)

    #Print the winner's name and info
    winner_summary = (
        f"Winner: {winner}\n")
    print(winner_summary)

    #Save to the text file
    txt_file.write(winner_summary)