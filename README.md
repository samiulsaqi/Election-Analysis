#Election Analysis

##Overview of Election Audit

The main purpose this election audit analysis is done is to find out if we can automate the voting result calculation and submit the result in an easy to read format.

##Election-Audit Results:

The results based on the election results data file are summarized below:
    - Total Votes cast were 369,711
    - County wise the results are:
        -Jefferson county had 38,855 votes cast, being 10.5% of total votes;
        -Denver county had 306,055 votes cast, being 82.8% of total votes;
        -Arapahoe had 24,801 votes cast, being6.7% of total votes.
    - Denver had the largest number of votes (82.8%)
    - Results according to candidates:
        - Charles Casper Stockham received 85,213 votes, which is 23.0% of total votes;
        - Diana DeGette received 272,892 votes, which is 73.8% of total votes;
        - Raymon Anthony Doane received 11,606 votes, which is 3.1% of total votes.
    - Based on the election result, Diana DeGette won the election, receiving 272,892 votes, or 73.8% of total votes.

Election result summary
<img src=resources/election_results.png></img>

##Election-Audit Summary:

The script used in this audit was useful in analyzing the result in an efficient manner. This gave us an output in a summary format. Even though this script was written for this election, it can be reused as long as the election data format used for this audit stays the same. Two easy changes that can be incorporated for future elections can be changing the heading for the results output so that it says what election is being audited and changing what is being printed, i.e. candidate/county name, votes and percentage. Other than that, it is fairly self maintaining.