# Week 9 Assignment
# Authors: Devin Simoneaux & Nathaniel Pugh
# Program solves a world puzzle game using a dictionary
# CIS-125

def sortString(aString):
    aList = list(aString) #turns string into list of characters
    aList.sort() #puts list in alphabetical order
    return ("".join(aList))
    
def fillVWords(fileName, aDict):
    
    file = open(fileName, "r") #open the file for reading purposes only
    
    for line in file: #going through each line in the file
        word = line.strip().lower() # gets rid of punctuation and makes everything lowercase
        if word[0] == "v": #only want to add words starting with "v" to the dictionary
            aDict[sortString(word)] = word #adds the sorted string to the dictionary
    file.close()
    
def main():
    aDict = {} #declares dictionary
    fileName = "wordList.txt" #declares the file name
    fillVWords(fileName, aDict) #runs the fillVWords function
    file = open("quizwords.txt", "r") #opens the quizwords.txt file for reading purposes only
    for line in file: #go through each line in the file
        word = line.strip(",\t\n \r").lower() #gets ride of punctuation, tab, blank spaces, and makes everything lowercase
        print(word, aDict[sortString(word)]) #prints the word and its value from the dictionary
    file.close()
    
main()