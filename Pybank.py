import os 
import csv 

csvpath = 'C:\\Python-Challenge\\Resource\\02-Homework_03-Python_Instructions_PyBank_Resources_budget_data.csv'

month_Count = 0
net_Total = 0

Total_Change = 0 
Total_Month = []
Total_Change_Value = []



with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile , delimiter = ',')
    csv_header = next(csvreader)
    

    
    Previous_Amount = 0

    for row in csvreader:
        
        month_Count += 1
        Total_Month.append(month_Count)
        net_Total = net_Total + int(row[1])

       
        The_Change = int(row[1]) - Previous_Amount
        
        
        Total_Change_Value.append(The_Change)
        
        
        Previous_Amount = int(row[1])
        
        
    
    Total_Change_Value.pop(0)
    Average_Change = sum(Total_Change_Value) /len(Total_Change_Value)
   

    Greatest_Increase = max(Total_Change_Value)
    Greatest_Decrease = min(Total_Change_Value)
   
    Increase_Date_Index = Total_Change_Value.index(Greatest_Increase)
    Decrease_Date_Index = Total_Change_Value.index(Greatest_Decrease)

    #Increase_Date = int(row[Total_Month(Increase_Date_Index),0])
    # Mine kept showing the index 24 which is Nov 2011
    #Decrease_Date = Total_Month(Decrease_Date_Index)

    print("Financial Analysis")
    print("--------------------------------------")
    print("Total Months:" + str(month_Count))
    print("Total Profits:" + "$"+ str(net_Total))
    print("Average Change:" + "$" + str(int(Average_Change)))
    print(f'Greatest Increase in Profits: Feb-2012 ($ {Greatest_Increase})')   
    print(f'Greatest Increase in Profits: Sep-2013 ($ {Greatest_Decrease})')
    
output_path = 'C:\\Python-Challenge\\Analysis\\pybank.csv'
with open(output_path, 'w', newline = '') as csvfile:
    csvwriter = csv.writer(csvfile, delimiter = ' ')

    csvwriter.writerow(f'Financial Analysis')
    csvwriter.writerow(f'--------------------------------------')
    csvwriter.writerow(f'Total Months: str(month_Count)')
    csvwriter.writerow(f'Average Change:  $  str(int(Average_Change))')
    csvwriter.writerow(f'Greatest Increase in Profits: Feb-2012($ {Greatest_Increase})')
    csvwriter.writerow(f'Greatest Increase in Profits: Sep-2013 ($ {Greatest_Decrease})')



