# Election_Analysis
## Project Overview
Colorado Board of Elections employee, Seth, and his manager need the following tasks done to complete an election audit of a recent local congressional election, by using python.
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
  
## Challenge Overview
Tom and Seth requested additional information for their audit. They need the code do the following:
1. Calculate the voter turnout for each county
2. Calculate the percentage of votes from each county out of the total count
3. Calculate the county with the highest turnout

## Challenge Summary
To caluculate the voter turnout in each county, the code used was:
 ```total_county_votes = total_votes + 1 
        # 3: Extract the county name from each row.
        county_name = row[1]
        # county does not match any existing county in the county list.
        if county_name not in county_list:
        # 4b: Add the existing county to the list of counties.
            county_list.append(county_name)
         # 4c: Begin tracking the county's vote count.
            county_votes[county_name] = 0
        # 5: Add a vote to that county's vote count.
        county_votes[county_name] += 1 
  ```
 To calculate the percentage of votes for each county:
 ```
 for county_name in county_votes:
        # 6b: Retrieve the county vote count.
        votes_county = county_votes[county_name]
        # 6c: Calculate the percent of total votes for the county.
        county_vote_percentage = float(votes_county) / float(total_votes) * 100
  ```
To determine the county with the largest voter turnout:
```
 if (votes_county > largest_turnout_count) and (county_vote_percentage > largest_county_percentage):
            largest_turnout_count = votes_county
            largest_county_percentage = county_vote_percentage
            county_largest_turnout = county_name
```
### Results
After the code was ran, the results are as follows:
- The percentage of the votes and number of votes by county were:
  - Jefferson County made up 10.5% of the votes with 38,855 voters
  - Denver County made up 82.8% of the votes with 272,892 voters
  - Arapahoe County made up 6.7% of the vote with 24,801 voters
- Denver had the largest county turnout
- The winner of the election was:
  - Diana DeGette, who received 73.8% of the vote and 272,892 number of votes.
### Audit Summary
With minor modifications, this script can be used to pull and calculate data from any election. It may need to be modified in order to be used to calculate the number of candidates received from each county and the percentage of the county vote that each candidate received. 

