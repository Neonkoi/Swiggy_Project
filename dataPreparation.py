# This script will parse the contents of a .tsv file located in the current directory (taken as a first argument) into individual .txt files.
# The .txt files will be named after the ID in each line and will contain only the transcription associated with that ID.
# A Txt folder will be created in the current working directory where all the .txt files will be moved.
# A manifest .csv file will also be created containing the paths of the audio files and the corresponding .txt file.
#
# USAGE: Place this script in either the Train or the Dev folder. Run using the system console and pass the .tsv file as argument.

import sys
import re, os, shutil, glob, csv, pathlib

#--------FUNCTION DEFINITIONS---------

def tsvToTxt(foldertype):
    # Create folder for txt files
    print("\nCreating folder in " + destinationdir + "...")
    try:
        os.makedirs(destinationdir)
    except:
        print("[!] Error in folder creation on path: " + destinationdir + " ... Does the folder already exist?")
        quit()

    print("Creating manifest according to folder type...")
    if(foldertype=="1"):
        mycvsfile = open('data_train_manifest_PA_lang.csv',"wt", newline='')
    else:
        mycvsfile = open('data_val_manifest_PA_lang.csv',"wt", newline='')

    wr = csv.writer(mycvsfile, quoting=csv.QUOTE_ALL)
    
    # Open tsv file and read line by line. Separate ID and transcription to create .txt file and write its content.
    print("Opening " + inputFileName + "...")
    print("Creating .txt files, moving them to the Txt folder, and filling up manifest...")
    with open(inputFileName) as inputFile:
        for line in inputFile:
            lineList = re.split(r'\t+',line)
            f = open(lineList[0]+".txt","w")
            f.write(lineList[1])
            f.close()
            manifestline = (currentdir+"\\Audio"+"\\"+lineList[0]+".wav",destinationdir+"\\"+lineList[0]+".txt")
            wr.writerow(manifestline)
            shutil.move(currentdir + "\\" + lineList[0] + ".txt", destinationdir) # Move txt to Txt folder.
    print("...Done!")
    f.close()

#--------------------------------------

inputFileName = sys.argv[1]
currentdir = os.getcwd()
destinationdir = currentdir + r"\Txt"

print("\nIs this the 'Train' or 'Dev' folder?\n(1) Train folder\n(2) Dev folder\n\nIndicate option number: ")
foldertype = input()

tsvToTxt(foldertype)