#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Sep 24 16:27:43 2023

@author: nargizshemssulldin
"""

#Open the csv file with open ('election_data.csv', 'r') as file:
    
#set counter for total votes cast
# First we'll import the os module
# This will allow us to create file paths across operating systems
import os

# Module for reading CSV files
import csv

csvpath = os.path.join('.', 'Resources', 'election_data.csv')



# Method 2: Improved Reading using CSV module

with open(csvpath) as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')

    total_votes= 0
    total_candidates= []
    x= {}
    # Read the header row first (skip this step if there is now header)
    csv_header = next(csvreader)

    # Read each row of data after the header
    for row in csvreader:
        total_votes= total_votes +1     
        if row[2] not in total_candidates:
            total_candidates.append(row[2]) 
            x[row[2]]=0
        x[row[2]]+=1
print (x)
print (total_candidates)
print (total_votes)
# =============================================================================

# 
#     
# #loop through csv for row in reader:

# 
# a= candidates
# 
# = ["Charles Casper Stockham", "Diana DeGette", "Raymon Anthony Doane""]
#          print(a)
# =============================================================================
