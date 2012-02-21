'''
This is my first python program. 
What it does is explained here: 
https://github.com/thehackerwithin/PyTrieste/wiki/ExerciseSession1-Basics
'''
import os
import sys

''' main '''
def main():

  dirList = MakeFileNameList()
  for fileName in dirList:
    if LineContainsResponseN(fileName):
      ChangeNtoM(fileName)
 


''' MakeFileNameList() finds all of the filenames and puts them in a list '''
def MakeFileNameList():
  path="/afs/ictp.it/home/y/ykolahdo/ShellExample/thehackerwithin-PyTrieste-4f54727/shellExample/cleaneddata/alexander"
  dirList=os.listdir(path)
  return dirList





''' LineContainsResponseN() checks if a given line contains a question with an N response '''
def LineContainsResponseN(filename)
  '''if contains'''
  return True

  ''' else '''
  return False




def ChangeNtoM(a_line)
  
  if LineContainsResponseN(a_line)
  ''' Change N in the line to M'''
  return True











