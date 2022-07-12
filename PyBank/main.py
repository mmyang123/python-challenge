# Modules
import os
import csv
import locale
from threading import local

locale.setlocale(locale.LC_ALL, '')

# set path for file
# csvFilePath = os.path.join("..", "Resources", "budget_data.csv")
csvFilePath = "C:\\Users\\maimy\\Desktop\\python-challenge\\PyBank\\Resources\\budget_data.csv"

# find the following dataset
totalMonthsInDataSet = 0
netTotalProfitLossesOverPeriod = 0
changesProfitLossesOverPeriod = 0
greatestIncreaseInProfitOverPeriod = ["", -1]
greatestDecreaseInProfitOverPeriod = ["", -1]

# Intermediate computations
greatestIncrease = 0
greatestDecrease = 0
previousProfitLoss = 0
currentChange = 0
rowCount = 0

# open the csv
with open(csvFilePath, encoding= 'utf') as csvfile:
    csvreader = csv.reader (csvfile, delimiter= ",")

    # Skip first row of CSV file - normally header row
    next(csvreader)

    for currentRow in csvreader:
        if(totalMonthsInDataSet <= 0):
            previousProfitLoss = int(currentRow[1],10)
        else:
            currentChange = int(currentRow[1], 10) - previousProfitLoss
            previousProfitLoss = int(currentRow[1],10)
            changesProfitLossesOverPeriod = changesProfitLossesOverPeriod + currentChange
        
        totalMonthsInDataSet = totalMonthsInDataSet + 1
        netTotalProfitLossesOverPeriod = netTotalProfitLossesOverPeriod + int(currentRow[1], 10)

        if(greatestDecreaseInProfitOverPeriod[1] == -1):
            greatestDecrease = currentChange
            greatestDecreaseInProfitOverPeriod = [currentRow[0], currentChange]
        else:
            if(currentChange < greatestDecrease):
                greatestDecrease = currentChange
                greatestDecreaseInProfitOverPeriod = [currentRow[0], currentChange]

        if(greatestIncreaseInProfitOverPeriod[1] == -1):
            greatestIncrease = currentChange
            greatestIncreaseInProfitOverPeriod = [currentRow[0], currentChange]
        else:
            if(currentChange > greatestIncrease):
                greatestIncrease = currentChange
                greatestIncreaseInProfitOverPeriod = [currentRow[0], currentChange]

# Display data
print("Total months: ", totalMonthsInDataSet)
print("Total: ", locale.currency(netTotalProfitLossesOverPeriod))
print("Average Changes: ", locale.currency(changesProfitLossesOverPeriod/(totalMonthsInDataSet - 1)))
print("Greatest increase in profits: ", greatestIncreaseInProfitOverPeriod[0], locale.currency(greatestIncreaseInProfitOverPeriod[1]))
print("Greatest decrease in profits: ", greatestDecreaseInProfitOverPeriod[0], locale.currency(greatestDecreaseInProfitOverPeriod[1]))

# Write to analysis file
analysisFile = open("C:\\Users\\maimy\\Desktop\\python-challenge\\PyBank\\analysis\\analysis.txt", "w")
analysisFile.write("Total months: {count}\n".format(count = totalMonthsInDataSet))
analysisFile.write("Total: {total}\n".format(total = locale.currency(netTotalProfitLossesOverPeriod)))
analysisFile.write("Average Changes: {changes}\n".format(changes = locale.currency(changesProfitLossesOverPeriod/(totalMonthsInDataSet - 1))))
analysisFile.write("Greatest increase in profits: {increaseDate} {increaseAmount}\n".format(increaseDate = greatestIncreaseInProfitOverPeriod[0], increaseAmount = locale.currency(greatestIncreaseInProfitOverPeriod[1])))
analysisFile.write("Greatest decrease in profits: {decreaseDate} {decreaseAmount}\n".format(decreaseDate = greatestDecreaseInProfitOverPeriod[0], decreaseAmount = locale.currency(greatestDecreaseInProfitOverPeriod[1])))
analysisFile.close()
