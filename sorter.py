import os
import glob
import string

def printList(files):
	for f in files:
		# print f
		# print str(f)
		if "11" in str(f):
			for c in str(f):
				print c,
			# pos = str(f).find('(')
			# print str(f)[:pos]

# def moveFile(files):
	
	

	
if __name__ == "__main__":
	files = [f for f in os.listdir('.') if os.path.isfile(f)]
	homeDir = os.getcwd()
	print u'\u043e'
	# printList(files)


