import csv
import os

budget_data = "Resources/budget_data.csv"
output_file = "analysis/out_put.txt"

with open(budget_data) as csvfile:
    # create empty list called dataset to store each row
    dataset = []
    csvreader = csv.reader(csvfile)
    #Each row is a list, add each row into the dataset
    for row in csvreader:
        dataset.append(row)
    # print(dataset)


# def total_number_of_month ():
#     length =
#     return
print("PyBank answers")
print("----------------------------------")


#The total number of months included in the dataset
print("Total Months:" ,len(dataset)-1)

#The net total amount of "Profit/Losses" over the entire period

#set variable to hold the total
total_profit_loss = 0
#loop through each row in the dataset
for row in dataset:
    #skip the first line
    # print("this is the header" ,dataset[0])
    # print("this is the current row", row)
    if dataset[0]==row:
        continue
    profit_loss = int(row[1])
    total_profit_loss = total_profit_loss + profit_loss
#you want to do this for the 2nd column
print("Total: $",total_profit_loss)

#Calculate the changes in "Profit/Losses" over the entire period,
#then find the average of those changes

#calculate the difference between each months
#do this for column 2
#calculate average difference

months = []
differences = []
dataset_noheader = dataset[1:]
for i, row in enumerate(dataset_noheader):
    if row != dataset_noheader[+1]:
        months = dataset_noheader[+1]
        months.append(dataset_noheader[+1])
    # print(i, row)
    #Until it is not equal (last row) do the follwoings
    if row != dataset_noheader[-1]:
        next_row = dataset_noheader[i+1]
        profit_loss_t0 = int(row[1])
        profit_loss_t1 = int(next_row[1])
        monthly_change = profit_loss_t1 - profit_loss_t0
        differences.append(monthly_change)
# print(differences)
# print(months)

average_change = sum(differences) / len(differences)
average_change = "{:.2f}".format(average_change)
print("Average Change: $",average_change)
    # month_difference = row + row[+1]


# The greatest increase in profits (date and amount) over the entire period
#from monthly change list, extract highest value

print ("Greatest Increase in Profits:" ,max(differences))

print ("Greatest Decrease in Profits:" ,min(differences))

# print value in the .txt file

with open(output_file, "w") as datafile:
    datafile.write("I dont know how to write my function/answers into this text file")
    # writer = writer(datafile)
    #
    # # writer.writerow(["Index", "Employee", "Department"])
    #
    # writer.writerows(len(dataset)-1, total_profit_loss)
