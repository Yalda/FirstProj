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
    ChangeNtoM(fileName)

  print "DONE"



''' MakeFileNameList() finds all of the filenames and puts them in a list '''
def MakeFileNameList():
  dirList=os.listdir(path)
  return dirList



''' ChangeNtoM() replaces N with M '''
def ChangeNtoM(filename)

  pathToFile = path + filename  
  fileToCheck = open("pathToFile","a") #open for append
  
  for line in open("pathToFile"):
      line = line.replace("Sex: N","Sex: M")
      fileToCheck.write(line + "\n")
      fileToCheck.close()



















