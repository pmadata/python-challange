import os
import csv
filename = "Resources/election_data.csv"
Total_vote = 0
candidate_list = []
percentage_list = []
t_count= {} 

with open(filename) as csvfile:
    csvread = csv.reader(csvfile)

    csv_header = next(csvread)
    
    firstrow = next(csvread)

    Total_vote += 1

    for row in csvread:
        Total_vote = Total_vote + 1
        candidate = row [2]
        
        if candidate not in candidate_list:
            candidate_list.append(candidate)
            t_count[candidate]  = 0
        t_count[candidate]  += 1
        
    for candidate in t_count:
        t_count_percent =  round((t_count[candidate] /Total_vote *100),2)
        if candidate not in percentage_list:
            percentage_list.append(candidate)
            percentage_list.append(t_count_percent)
            percentage_list.append(Total_vote)
        
print ("Election Results")
print ("-------------------------------------------")
print ("Total votes:" + str(Total_vote))
print ("-------------------------------------------")
print((str(percentage_list[0]))+":"+ (str(percentage_list[1]))+"%"+"("+(str(percentage_list[2]))+")")
print((str(percentage_list[3]))+":"+ (str(percentage_list[4]))+"%"+"("+(str(percentage_list[5]))+")")
print((str(percentage_list[6]))+":"+ (str(percentage_list[7]))+"%"+"("+(str(percentage_list[8]))+")")
print ("-------------------------------------------")
print ("Winner:" + (str(percentage_list[3])))
