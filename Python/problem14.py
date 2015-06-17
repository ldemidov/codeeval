"""

https://www.codeeval.com/open_challenges/14/

CHALLENGE DESCRIPTION:

Write a program which prints all the permutations of a string in alphabetical order. We consider that digits < upper case letters < lower case letters. The sorting should be performed in ascending order.

INPUT SAMPLE:

Your program should accept a file as its first argument. The file contains input strings, one per line.

For example:


1
2
3
hat
abc
Zu6
OUTPUT SAMPLE:

Print to stdout the permutations of the string separated by comma, in alphabetical order.

For example:


1
2
3
aht,ath,hat,hta,tah,tha
abc,acb,bac,bca,cab,cba
6Zu,6uZ,Z6u,Zu6,u6Z,uZ6

"""
import sys


def permute(level, str, used, original, resultList):

	length = len(original)
	#print 'in loop', level, str, used

	#bottom level
	if(level == (length-1)):
		for x in range(0, len(used)):
				if not used[x]:
					#print str + original[x]
					resultList.append(str + original[x])
		return

	#keep going down
	for i in range(0, length):
		# dont process letter already done on upper level
		if(used[i]): continue

		
		if(level < (length-1)):
			used[i] = 1
			permute(level+1, str + original[i], used, original, resultList)
			used[i] = 0
		
		



if len(sys.argv) > 1:
	filename = sys.argv[1]
else:
	filename = 'problem14.txt'

test_cases = open(filename, 'r')
for test in test_cases:
 
    
    sortedString = ''.join(sorted(test.rstrip()))
    
    resultList = []

    if len(sortedString) > 0:
		used = [0 for i in range(len(sortedString))]		
    	
		permute(0, '', used, sortedString, resultList)
		print ','.join(resultList)

test_cases.close()
