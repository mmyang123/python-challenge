import os
import csv

# Modules
import os
import csv
import locale
from threading import local

locale.setlocale(locale.LC_ALL, '')

# set path for file
# csvFilePath = os.path.join("..", "Resources", "budget_data.csv")
csvFilePath = "C:\\Users\\maimy\\Desktop\\python-challenge\\PyPoll\\Resources\\election_data.csv"

# find the following dataset
totalVotesCast = 0
candidateData = []

winnerName = ""

# Intermediate computations
previousCandidate = ""
candidateName = ""
currentCandidatesVoteCount = 0
currentCandidate = {}
currentCandidateIndex = 0

# open the csv
with open(csvFilePath, encoding= 'utf') as csvfile:
    csvreader = csv.reader (csvfile, delimiter= ",")

    # Skip first row of CSV file - normally header row
    next(csvreader)

    for currentRow in csvreader:
        totalVotesCast = totalVotesCast + 1
        if(previousCandidate == ""):
            # Process first row
            candidateName = currentRow[2]
            previousCandidate = candidateName
            currentCandidatesVoteCount = currentCandidatesVoteCount + 1
            currentCandidate = {"name":candidateName, "votePercent": currentCandidatesVoteCount/totalVotesCast,"voteCount": currentCandidatesVoteCount}
            candidateData.append(currentCandidate)
        else:
            if(candidateName != previousCandidate):
                # Process next candidate
                currentCandidateIndex = currentCandidateIndex + 1
                currentCandidatesVoteCount = 0
                candidateName = currentRow[2]
                previousCandidate = candidateName
                currentCandidatesVoteCount = currentCandidatesVoteCount + 1
                currentCandidate = {"name":candidateName, "votePercent": currentCandidatesVoteCount/totalVotesCast,"voteCount": currentCandidatesVoteCount}
                candidateData.append(currentCandidate)
            else:
                # Process same candidate data
                candidateName = currentRow[2]
                previousCandidate = candidateName
                currentCandidatesVoteCount = currentCandidatesVoteCount + 1
                candidateData[currentCandidateIndex]['voteCount'] = currentCandidatesVoteCount

for candidate in candidateData:
    candidate["votePercent"] = candidate("voteCount")/totalVotesCast



