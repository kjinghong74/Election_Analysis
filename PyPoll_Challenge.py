import csv
import os
# Assign a variable for the file to load and the path.
file_to_load = os.path.join("Resources", "election_results.csv")
# Assign a variable to save the file to a path
file_to_save = os.path.join("Analysis", "election_analysis.txt")

#1. Initialize a total vote counter
total_votes = 0

#Declare candidate list
candidate_options = []
#Declare county list
county_options = []
#Declare candidate_vote dictionary
candidate_vote = {}
#Declare county_vote dictionary
county_vote = {}
#winning candidate and winning count tracker
winning_candidate = ""
mostVotes_county = ""
winning_count = 0
winning_percentage = 0
mostVotescounty_count = 0
mostCountyVotes_percentage = 0

# Open the election results and read the file.
with open(file_to_load) as election_data:

    # Read the file object with the reader function
    file_reader = csv.reader(election_data)
    # Read the header
    headers = next(file_reader)

    #Print each row in the csv file
    for row in file_reader:
        #2. Add to the total vote count
        total_votes = total_votes + 1

        #Find candiadate name from each row
        candidate_name = row[2]
        county_name = row[1]

        if candidate_name not in candidate_options:

        #Add candiate name to the candidate list
            candidate_options.append(candidate_name)
        #Begin tracking that candidate's vote count
            candidate_vote[candidate_name] = 0
        candidate_vote[candidate_name] = candidate_vote[candidate_name] +1

        if county_name not in county_options:
            county_options.append(county_name)
            county_vote[county_name] = 0
            
        county_vote[county_name] = county_vote[county_name] +1
    
    
    #print the final vote count to the teminal
with open(file_to_save, "w") as txt_file:
    election_results = (
        f"\nElection Results\n"
        f"---------------------------\n"
        f"Total Votes: {total_votes:,}\n"
        f"---------------------------\n"
        f"County Votes:\n")


    print(election_results, end="")

    #save the final vote count to the text file
    txt_file.write(election_results)

#print(total_votes)
#print(candidate_options)
#print(candidate_vote)

    
    
    for county_name in county_vote:
        countyVotes = county_vote[county_name]
        countyVotes_percentage = float(countyVotes)/float(total_votes)*100
        countyVotes_results = (f"{county_name}: {countyVotes_percentage:.1f}% ({countyVotes:,})\n")
        print(countyVotes_results)

    
        
        txt_file.write(countyVotes_results)
    


        if (countyVotes > mostVotescounty_count) and (countyVotes_percentage) > (mostCountyVotes_percentage):
            mostVotescounty_count = countyVotes
            mostVotes_county = county_name
            mostCountyVotes_percentage = countyVotes_percentage
        largestCountyTurnout = (
            f"---------------------------\n"
            f"Largest Vote Turnout: {mostVotes_county}\n"
            f"---------------------------\n")
    txt_file.write(largestCountyTurnout)


    for candidate_name in candidate_vote:
    #vote_percentage = float(votes)/float(total_votes) *100
        votes = candidate_vote[candidate_name]
        vote_percentage = float(votes) / float(total_votes) * 100

    #print(f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")
    
        #Save candidate results to txt file
        candidate_results = (f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")
        print(candidate_results)
        txt_file.write(candidate_results)

            #determine winning vote count and the candidate
            #1 determine if the votes are greater than the winning count
        if (votes > winning_count) and (vote_percentage > winning_percentage):
            winning_count = votes
            winning_percentage = vote_percentage
            winning_candidate = candidate_name    


    winning_candidate_summary = (
        f"---------------------------\n"
        f"Winner: {winning_candidate}\n"
        f"Winning vote count: {winning_count}\n"
        f"Winning_percentage: {winning_percentage:.1f}%\n"
        f"---------------------------\n")
    
    print(winning_candidate_summary)
#save the winning candidate's results to the text file
    txt_file.write(winning_candidate_summary)
    

   
 #3. Print total votes

