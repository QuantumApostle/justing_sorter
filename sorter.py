# -*- coding: gbk -*-
import os
import shutil
import glob
import string

def fileList(files):
        fileName = open("fileNames.txt", "w")
        for f in files:
                if ".mp3" in f:
                        fileName.write(str(f) + "\n")
        fileName.close()
        print "file names exported"
        
def extractFileName(files):

        names = {}
        for f in files:
                if ".mp3" in f:
                        a = f.decode("gbk")
                        for i in range(len(a)):
                                if a[i] == "（".decode("gbk") or a[i].isdigit():
                                        break
                        if ".mp" not in a[:i]:
                                names[a[:i]] = 0
        return names.keys()

def makeFolders(names):
        for name in names:
                newPath = homeDir + "\\" + name
                if not os.path.exists(newPath):
                        os.makedirs(newPath)
                        
def moveFile(files, names, homeDir):
        for name in names:
                for f in files:
                        filePath = homeDir + "\\" + f.decode("gbk")
                        dirPath = homeDir + "\\" + name
                        
                        fi = f.decode("gbk")
                        if name in fi:
                                shutil.move(filePath, dirPath)
        print "file movement finishes"


	
if __name__ == "__main__":
	files = [f for f in os.listdir('.') if os.path.isfile(f)]
	homeDir = os.getcwd()
	names = extractFileName(files)
	makeFolders(names)
	moveFile(files, names, homeDir)
