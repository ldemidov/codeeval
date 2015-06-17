"""

https://www.codeeval.com/open_challenges/6/

LONGEST COMMON SUBSEQUENCE

CHALLENGE DESCRIPTION:

You are given two sequences. Write a program to determine the longest common subsequence between the two strings (each string can have a maximum length of 50 characters). NOTE: This subsequence need not be contiguous. The input file may contain empty lines, these need to be ignored.

INPUT SAMPLE:

The first argument will be a path to a filename that contains two strings per line, semicolon delimited. You can assume that there is only one unique subsequence per test case. E.g.

XMJYAUZ;MZJAWXU
OUTPUT SAMPLE:

The longest common subsequence. Ensure that there are no trailing empty spaces on each line you print. E.g.

MJAU

"""


import sys

def rec(first, second, firstIdx, secondIdx, answer):
    if firstIdx > len(first):
        return lst

    banswer = answer
    for f in range(firstIdx, len(first)):
        for i in range(secondIdx, len(second)):
            if first[f]==second[i]:
                banswer2 = rec(first, second, f+1, i+1, answer+second[i])
                if len(banswer2) > len(banswer):
                    banswer = banswer2
            
    return banswer

   
if len(sys.argv) > 1:
    filename = sys.argv[1]
else:
    filename = 'problem6.txt'

test_cases = open(filename, 'r')

for test in test_cases.read().splitlines():
    # ignore test if it is an empty line
    if len(test) > 0:    
        firstString = test.split(';')[0]
        secondString = test.split(';')[1]
        myanswer = rec(firstString, secondString, 0, 0, '')
        print myanswer


test_cases.close()



