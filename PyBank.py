#modules (libraries)
import os
import csv

# Set the path to access the file
csvpath = os.path.join("Resources", "budget_data.csv")

# Define total months
total_months = 0

# Defint net total
net_total = 0

# Define list of change values
empty_list = []
month_list = []
profit_list = []
monthly_profit_change = []
net_change=0
greatest_increase = ["",0]
greatest_decrease = ["",0]


# Open the CSV
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile)


    # Acknowledge the header and read
    csv_header = next(csvreader)
    first_row = next(csvreader)
    month_list.append(first_row[0])
    # append the profit list
    profit_list.append(int(first_row[1]))

    #
    total_months = total_months + 1

    #
    net_total = net_total + int(first_row[1])

    #
    #changes = int(first_row[1])
    
    prev_net = int(first_row[1])


    # Create a for loop to read through data after the header
    for row in csvreader:
        print(row)

# Calculate the total months in the dataset
        total_months = total_months + 1
        print(total_months)

        month_list.append(row[0])

        # append the profit list
        profit_list.append(int(row[1]))

        # Net changes
        net_total = net_total + int(row[1])
        print(net_total)

        # Find the changes
        changes = int(row[1]) - prev_net
        empty_list.append(changes)
        prev_net = int(row[1])

        #need to do greatest increast/ decrease in here
        if changes > greatest_increase[1]:
            greatest_increase[0]=row[0]
            greatest_increase[1] = changes

        if changes < greatest_decrease[1]:
            greatest_decrease[0]=row[0]
            greatest_decrease[1] = changes

# create a loop to get the monthly change in profits
for i in range(len(profit_list)-1):

    # Find the difference between any two months, and append to the monthly change in profits
    monthly_profit_change.append(profit_list[i+1]-profit_list[i])

#Calculating average monthly change
average_monthly_change = sum(monthly_profit_change) / len(monthly_profit_change)

#Set an output file
output=(f"\nAnalysis\n"
f"----------------------------------------\n"
f"Total Months:{total_months}\n"
f"Total:${net_total}\n"
f"Average Monthly Change:${average_monthly_change:.2f}\n"
f"Greatest Increase Month:{greatest_increase[0]}(${greatest_increase[1]})\n"
f"Greatest Decrease Month:{greatest_decrease[0]}(${greatest_decrease[1]})\n")

with open("file_to_create.txt","w") as txt_file:
    txt_file.write(output)

print(total_months)
print(net_total)
print(average_monthly_change)
print(greatest_increase)
print(greatest_decrease)

