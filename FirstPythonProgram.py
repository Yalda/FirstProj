'''
This is my first python program. 
What it does is explained here: 
https://github.com/thehackerwithin/PyTrieste/wiki/ExerciseSession1-Basics
'''
import os
import sys

path="/afs/ictp.it/home/y/ykolahdo/ShellExample/thehackerwithin-PyTrieste-4f54727/shellExample/cleaneddata/alexander"

''' main '''
def main():

  dirList = MakeFileNameList()
  for fileName in dirList:    
    index = LineContainsResponseN(fileName)
    if index:      	
      ChangeNtoM(fileName,index)
 


''' MakeFileNameList() finds all of the filenames and puts them in a list '''
def MakeFileNameList():
  dirList=os.listdir(path)
  return dirList




''' LineContainsResponseN() checks if a given line contains a question with an N response '''
def LineContainsResponseN(filename)
  
  fileToCheck = path + filename
  infile = open(fileToCheck,"r")
  contents = infile.read()
  infile.close()

  searchTerm = "Sex: N"
  index = contents.find(searchTerm)
  
  return index


def ChangeNtoM(a_line)
  
  if LineContainsResponseN(a_line)
  ''' Change N in the line to M'''
  return True











