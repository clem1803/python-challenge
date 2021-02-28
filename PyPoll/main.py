import csv
import os

# source to csv file
poll_data = "Resources/election_data.csv"

candidates_dic = {}

with open(poll_data) as csvfile:
    csv_reader = csv.reader(csvfile,delimiter=",")
    next(csv_reader)
    for row in csv_reader:
        row_candidate = row[2]
        if row_candidate in candidates_dic:
            candidates_dic[row_candidate] = candidates_dic[row_candidate] + 1
        else:
            candidates_dic[row_candidate] = 1
# print(candidates_dic)

totalvote = 0
win = 0
winner = ""
for k, v in candidates_dic.items():
    totalvote = totalvote + v
    if v > win:
        win = v
        winner = k

print ("Election Result")
print("--------------------------------")
print(f"Total votes: {totalvote}")
print("--------------------------------")

for k, v in candidates_dic.items():
    print(f"{k}: {'{:.3f}%'.format(float(v/totalvote)*100)} ({v})")

print("--------------------------------")

winning_candidate = [(value, key) for key, value in candidates_dic.items()]
print (f"Winner: {max(winning_candidate)[1]}")

output_file = "analysis/out_put.txt"

with open(output_file, "w", newline='') as datafile:
    writer = csv.writer(datafile)

    writer.writerow(["Number of vote", "Candidate"])

    writer.writerows(winning_candidate)
