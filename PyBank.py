#modules (libraries)
import os
import csv

#Set the path to access the file
csvpath = os.path.join("Resources","budget_data.csv")

#Define total months
total_months = 0

#Defint net total
net_total = 0

#Define list of change values
empty_list = []

#Open the CSV
with open (csvpath) as csvfile:
    csvreader = csv.reader(csvfile)

    #Acknowledge the header and read
    csv_header = next(csvreader)
    first_row = next(csvreader)

    #
    total_months = total_months + 1

    #
    net_total = net_total + int(first_row[1])

    changes = int(first_row[1])

    
    #Create a for loop to read through data after the header
    for row in csvreader:
        print(row)



#Calculate the total months in the dataset
        total_months = total_months + 1 
        print(total_months)


        #Calculate the net total
        net_total = net_total + int(row[1])
        print(net_total)

        #Find the changes 
        changes = int(row[1]) - changes
        empty_list.append(changes)
        changes = int(row[1])
print(changes)