#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Sep 24 13:51:55 2023

@author: nargizshemssulldin
"""
import csv

with open("Resources/budget_data.csv", "r") as file:
    reader =csv.reader(file)
    
    
   
    
    # Skip header row
    next(reader)
    
    # set counter for total months
    total_months = 0
    
    # set counter for total change
    total_changes= 0
    
    #Set previous month value
    previous_month = None
    
    #counter for total month changes
    total_month_changes = 0 
    
    #variables for greatest increase and decrease
    greatest_increase = 0
    greatest_decrease = 0
    
    # Counter for actual month
    greatest_increase_month = None
    greatest_decrease_month = None
    
    
    # Loop through csv
    for row in reader:
        total_months= total_months + 1
        
        # Parse through the second column
        change = int(row[1])
        
        #calculate total_changes
        total_changes = total_changes + change
        
    
            
        if previous_month is not None:
            month_change = change -previous_month
            total_month_changes = total_month_changes + month_change
        
        
        #update counters
            if month_change >greatest_increase:
                greatest_increase = month_change
            if month_change < greatest_decrease:
                greatest_decrease = month_change
            if month_change == greatest_increase:
                greatest_increase_month = row[0]
            if month_change == greatest_decrease:
                greatest_decrease_month = row [0]
        previous_month = change    
avg = total_month_changes / (total_months - 1)
#print(total_months)
#print(total_changes)
#print(avg)
#print(greatest_increase, greatest_increase_month)
#print(greatest_decrease, greatest_decrease_month)

print("Financial Analysis")
print("---------------")
print(f"Total Months {total_months}")
print(f"Total ${total_changes}")
print(f"Average Change ${avg}")
print(f"Greatest Increase In Profits {greatest_increase_month} {greatest_increase}")
print(f"Greatest Decrease in Profits {greatest_decrease_month} {greatest_decrease}")

with open("results.txt", "w") as file:
    file.write("Financial Analysis\n")
    file.write("---------------\n")
    file.write(f"Total Months {total_months}\n")
    file.write(f"Total ${total_changes}\n")
    file.write(f"Average Change ${avg}\n")
    file.write(f"Greatest Increase In Profits {greatest_increase_month} {greatest_increase}\n")
    file.write(f"Greatest Decrease in Profits {greatest_decrease_month} {greatest_decrease}\n")
    