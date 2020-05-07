## PyPoll
#In this challenge, you are tasked with helping a small, rural town modernize its vote-counting process. 
# #(Up until now, Uncle Cleetus had been trustfully tallying them one-by-one, but unfortunately, his concentration isn't what it used to be.)
#You will be give a set of poll data called [election_data.csv](PyPoll/Resources/election_data.csv). The dataset is composed of three columns:
# `Voter ID`, `County`, and `Candidate`. Your task is to create a Python script that analyzes the votes and calculates each of the following:

#modules (libraries)
import os
import csv

#set file path
csvpath = os.path.join("Resources", "election_data.csv")

#acknowledge header
csv_header = next(csvreader)
first_row = next(csvreader)
votes_list.append(first_row[0])

total_votes = 0

candidate_options = []
candidate_votes = {}

#counter for votes and candidates
winning_candidate = ""
winning_count = 0

#read and open csv
with open(file_to_load) as election_data:
    reader = csv.DictReader(election_data)


    for row in reader:

        print(". ", end=""),

        total_votes = total_votes + 1

        #pull candidate name out of list
        candidate_name = row["Candidate"]

        #create loop in case candidate is not found
        if candidate_name not in candidate_options:

            candidate_options.append(candidate_name)
            candidate_votes[candidate_name] = 0

        candidate_votes[candidate_name] = candidate_votes[candidate_name] + 1

#print results in text file
with open(file_to_output, "w") as txt_file:

    #print final vote counts formatted 
    election_results = (
        f"\nElection Results\n"
        f"-------------------------\n"
        f"Total Votes: {total_votes}\n"
        f"-------------------------\n")
    print(election_results, end="")

    #save final vote count to text file
    txt_file.write(election_results)

    #Find the winner loop
    for candidate in candidate_votes:

        #get vote count and %
        votes = candidate_votes.get(candidate)
        vote_percentage = float(votes) / float(total_votes) * 100

        #Find winning candidate
        if (votes > winning_count):
            winning_count = votes
            winning_candidate = candidate

        #Print output
        voter_output = f"{candidate}: {vote_percentage:.3f}% ({votes})\n"
        print(voter_output, end="")

        #Save to text file
        txt_file.write(voter_output)

    #Print the winner's name and info
    winning_candidate_summary = (
        f"-------------------------\n"
        f"Winner: {winning_candidate}\n"
        f"-------------------------\n")
    print(winning_candidate_summary)

    #Save to the text file
    txt_file.write(winning_candidate_summary)