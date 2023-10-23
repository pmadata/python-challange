import os
import csv
filename = "Resources/budget_data.csv"
Total_Month = 0
Profit_Loss = 0
Profit_Change = 0
Change_list = []
Max_INC = ["",0]
Max_DEC = ["",99999999999]

with open(filename) as csvfile:
    csvread = csv.reader(csvfile)  
    csv_header = next(csvread)
    print(f"CSV Header: {csv_header}")
    firstrow = next(csvread)
    print (firstrow)
    Total_Month += 1
    Profit_Change += int(firstrow[1])
    Profit_Loss = int(firstrow[1])
    #max_month = str (firstrow[0])
    for row in csvread:
        print(row)
        Total_Month = Total_Month + 1
        Profit_Change = int(row[1]) - Profit_Loss
        Profit_Loss = int(row [1])
        Change_list += [Profit_Change]
        #Greatest_INC = [Profit_Change]
        #max_seen = Change_list [0]
        
        if Profit_Change > Max_INC[1]:
            Max_INC[0] = row[0]
            Max_INC[1] = Profit_Change
            
        if Profit_Change < Max_DEC[1]:
            Max_DEC[0] = row[0]
            Max_DEC[1] = Profit_Change
                   
    Average = sum(Change_list)/len(Change_list) 
    print ("Total Months:", Total_Month)
    print ("Total:", Profit_Loss)
    print ("Average of Change:" + str(Average))
    print ("Greatest Increase in Profits:" + str(Max_INC[0]) + "," + str(Max_INC[1]))
    print ("Greatest Decrease in Profits:" + str(Max_DEC[0]) + "," + str(Max_DEC[1]))
   