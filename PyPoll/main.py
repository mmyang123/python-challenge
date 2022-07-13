# Modules
import os
import csv
import locale
from threading import local

locale.setlocale(locale.LC_ALL, '')

# set path for file
csvFilePath = os.path.join("Resources", "election_data.csv")

# find the following dataset
totalVotesCast = 0
candidateData = []

winnerName = ""

# Intermediate computations
previousCandidate = ""
currentCandidateName = ""
currentCandidatesVoteCount = 0
currentCandidate = {}

totalCandidates = 0

# open the csv
with open(csvFilePath, encoding= 'utf') as csvfile:
    csvreader = csv.reader (csvfile, delimiter= ",")

    # Skip first row of CSV file - normally header row
    next(csvreader)

    for currentRow in csvreader:
        totalVotesCast = totalVotesCast + 1

        # Test if the candidateData list of dictionary items has any records
        if(candidateData):
            currentCandidateName = currentRow[2]
            candidateFound = False
            currentCandidateIndex = 0

            # Find if the currentCandidateName is already in the list of candidates
            for currentCandidate in candidateData:
                if(currentCandidateName == currentCandidate["name"]):
                    candidateFound = True
                    break
                currentCandidateIndex = currentCandidateIndex + 1

            # See if the current candidate was found
            if(candidateFound):
                # Update the current candidate's vote count
                candidateData[currentCandidateIndex]["voteCount"] = candidateData[currentCandidateIndex]["voteCount"] + 1
            else:
                # A candidate that was not found must be a new candidate
                currentCandidate = {"name":currentRow[2],"votePercent":0,"voteCount":1}
                candidateData.append(currentCandidate)        
        else:
            # Add first candidate
            totalCandidates = totalCandidates + 1
            currentCandidate = {"name":currentRow[2],"votePercent":0,"voteCount":1}
            candidateData.append(currentCandidate)

currentCandidateIndex = 0

# Write analysis file
analysisFilePath = os.path.join("analysis", "analysis.txt")
analysisFile = open(analysisFilePath, "w")

# Print to analysis file
analysisFile.write("Election Results\n")
analysisFile.write("------------------------\n")
analysisFile.write("Total Votes: {votes}\n".format(votes = totalVotesCast))
analysisFile.write("------------------------\n")

# Print to terminal
print("Election Results\n")
print("------------------------\n")
print("Total Votes: ", totalVotesCast)
print("------------------------\n")

greatestVoteCount = 0
winnerName = ""

for candidate in candidateData:
    candidate["votePercent"] = candidate["voteCount"]/totalVotesCast
    currentCandidateIndex + currentCandidateIndex + 1
    # print(candidateData)
    print(candidate["name"] + ": {:.3%} ".format(candidate["votePercent"]) + " ({votes})\n".format( votes = candidate["voteCount"] ))
    analysisFile.write(candidate["name"] + ": {:.3%} ".format(candidate["votePercent"]) + " ({votes})\n".format( votes = candidate["voteCount"] ))

    # Find winner
    if(candidate["voteCount"] > greatestVoteCount):
        winnerName = candidate["name"]
        greatestVoteCount = candidate["voteCount"]


# Print to terminal
print("------------------------\n")
print("Winner: ", winnerName)
print("------------------------\n")

analysisFile.write("------------------------\n")
analysisFile.write("Winner: {winner}\n".format(winner = winnerName))
analysisFile.write("------------------------\n")

analysisFile.close()
