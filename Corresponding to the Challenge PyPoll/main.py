import csv

# This function finds the unique name of candidates in an array
def find_list_of_candidates (candidate_array):
    candidate_list = []  
    for candid in candidate_array:
        new_candiate_find = True
        for candidate in candidate_list:
            if candid == candidate:
                new_candiate_find = False
        if new_candiate_find == True:
            candidate_list.append(candid)     
    return candidate_list

# Path of the CSV file:
input_path = "C:/Users/18594/Desktop/python-challenge/Corresponding to the Challenge PyPoll/election_data.csv"

# Path of the output text file:
output_path = "C:/Users/18594/Desktop/python-challenge/Corresponding to the Challenge PyPoll/PyPoll_results.txt"

# Initial Values:
voter_ID_rows = []
county_rows = []
candidate_rows = []

# Open the csv file and save its data in voter_ID_rows, county_rows, and candidate_rows
with open (input_path) as csv_file:
    csv_reader = csv.reader(csv_file,delimiter = ",")
    csv_header = next(csv_reader)
    for row in csv_reader:
        voter_ID_rows.append(row[0])
        county_rows.append(row[1])
        candidate_rows.append(row[2])

# Calculation of the required parameters:
total_votes = len(voter_ID_rows)

# this function finds the name of voted candidates:
list_of_voted_candidate = find_list_of_candidates (candidate_rows)

# this array counts the votes of each candidate 
count_votes = [0] * len(list_of_voted_candidate)

for candid in candidate_rows:
    for voted_candid in range (len(list_of_voted_candidate)):
        if list_of_voted_candidate[voted_candid] == candid:
           count_votes [voted_candid]+=1

# Calculation of the percentage of votes each candidate won
percent_votes = ["{:.3%}".format(x/total_votes) for x in count_votes]

# Find the winner of the election:
winner = list_of_voted_candidate[count_votes.index(max(count_votes))]
            
# Print the results on the terminal and the output text file:
print("Election Results")
print("-------------------------")
print(f"Total Votes: {total_votes}")
print("-------------------------")
with open(output_path,'w') as output:
    output.write('{}\n{}\n{}\n{}\n'.format("Election Results","----------------------------",f"Total Votes: {total_votes}",
   "-------------------------"))
    for i in range (len(count_votes)): 
        candid_print = f"{list_of_voted_candidate[i]}: {percent_votes[i]} ({count_votes[i]})"
        print(candid_print)
        output.write('{}\n'.format(candid_print))
    output.write('{}\n{}\n{}\n'.format("-------------------------",f"Winner: {winner}","-------------------------"))
print("-------------------------")
print(f"Winner: {winner}")
print("-------------------------")

