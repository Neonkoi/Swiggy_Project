# This script will take the data transcription tsv file from a dataset as an argument, and output wether IDs in the transcript
# correspond to Bilingual or Monolingual data. A csv file will also be created containing a list of the results.
# USAGE: Place this script in either the Train or the Dev folder (not necesary). Run using the system console and pass the .tsv file as argument.

import sys, re, csv

inputFileName = sys.argv[1]

mycvsfile = open('MonoBiClassification.csv',"wt", newline = '') # Create .csv to store clasification
wr = csv.writer(mycvsfile, quoting=csv.QUOTE_ALL)

with open(inputFileName) as inputFile:
    for line in inputFile:
        lineList = re.split(r'\t+',line)
        transcription = re.sub('[^A-Za-z0-9]+', '', lineList[1])
        firstChar = transcription[0]
        for c in transcription:
            if(c != firstChar):
                flag = 1
                break
            else: flag = 0

        if (flag == 1):
            print("\n" + lineList[0] + "\tBilingual")
            csvline = (lineList[0],"Bilingual",lineList[1])
            wr.writerow(csvline)
        elif(flag == 0):
            print("\n" + lineList[0] + "\tMonolingual")
            csvline = (lineList[0],"Monolingual",lineList[1])
            wr.writerow(csvline)
        else: print("\n" + lineList[0] + "\tERROR")

print("...Done!")