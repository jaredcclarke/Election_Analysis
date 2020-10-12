# Election_Analysis
## Project Overview
Colorado Board of Elections employee, Seth, and his manager need the following tasks done to complete an election audit of a recent local congressional election

Those tasks were as follows:
1. Calculate the total number of votes cast.
2. Get a complete list of candidates who received votes.
3. Calculate the total number of votes each candidate received.
4. Calculate the percentage of votes each candidate won.
5. Determine the winner of the election based on popular vote.

## Resources
- Data Source: election_results.csv
- Software: Python 3.9.0, Visual Studio Code, 1.50.1

## Summary
The analysis of the election show that:
- There were 369,711 votes cast in the election
- The candidates were: 
  - Charles Casper Stockham
  - Diana DeGette
  - Raymon Anthony Doane
- The candidate results were:
  - Charles Casper Stockham received 23.0% of the vote and 85,213 number of votes
  - Diana DeGette received 73.8% of the vote and 272,892 number of votes. 
  - Raymon Anthony Doane received 3.1% of the vote and 11,606 number of votes.
- The winner of the election was:
  - Diana DeGette, who received 73.8% of the vote and 272,892 number of votes.
  
## Challenge Overview
In order to tally up the total number of votes, the varial `total_votes` was created and initialized to zero. Then as shown in the following script, it was placed in at `for` loop to give a total number.
```for row in file_reader:
        total_votes += 1
```
In order to get the name of each candidate, the variable `candidate_name` was created and set to loop throw the name column. And to prevent repeats of names an `if` statement was created: 
        ```candidate_name = row[2]`
          if candidate_name not in candidate_options:
            # Add the candidate name to the candidate list.
            candidate_options.append(candidate_name)```
In the same loop where the total number of votes were tallied and the names of the candidates were retrieved, to count the number of votes each candidate received was done as follows
        ```candidate_votes[candidate_name] = 0
           candidate_votes[candidate_name] += 1 ```
To calculate the number of votes and percentage of votes each candidate received, the following code:
``` for candidate_name in candidate_votes:
        # Retrieve vote count and percentage
        votes = candidate_votes[candidate_name]
        vote_percentage = float(votes) / float(total_votes) * 100
        candidate_results = (
            f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")  
```
The winner of the election was determined by:
``` if (votes > winning_count) and (vote_percentage > winning_percentage):
            # If true then set the winning_count = votes and winning_percent =           #vote_percentage
            winning_count = votes
            winning_percentage = vote_percentage
            # And, set the winning_candidate equal to the candidate's name.
            winning_candidate = candidate_name
```
## Challenge Summary
For this challenge, the biggest issue face while writing the script was the spacing of the code to make for modules and loops applied to the proper variables. 

