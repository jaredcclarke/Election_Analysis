# The data we need to retrieve.
#add our dependencies
import csv
import os
# Assign a variable for the file to load and the path
file_to_load = os.path.join("Resources", "election_results.csv")
# Assign a variable to save the file path
file_to_save = os.path.join("analysis", "election_analysis.txt")
# Open the election results and read the file.
with open(file_to_load) as election_data:

     # Read and print the header row
     file_reader = csv.reader(election_data)
     headers = next(file_reader)
     print(headers)
   
#creat a filename variable to a dirct or indirect path to the file.

# Using the open() function with the "w" mode we will write data to the file.

# Using the with statement open the file as a text file


# Write three counties to the file

    
# Close the file.
#outfile.close
# 1. The total number of votes cast
# 2. A complete list of candidates who received votes
# 3. The percentage of votes each candidate won
# 4. The total number of votes each candidate won
# 5. The winner of the election based on popular vote.
