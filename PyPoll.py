import os 
import csv

csvpath = 'C:\\Python-Challenge\\Resource\\02-Homework_03-Python_Instructions_PyPoll_Resources_election_data.csv'

vote_Count = 0 


with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, dilimiter = '')
    csv_header = next(csvreader)


    for row in csvreader:
        candidates = int(row[3])

        for candidate in cadidates:
            