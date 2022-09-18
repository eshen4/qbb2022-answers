#!/usr/bin/env python3

import sys
import numpy as np
from fasta import readFASTA

sys.argv[1:]
#not actually sure if this was necessary but it's saying system arguments 1 and up, might've included it by accident, because I define all used system arguments ahead

input_sequences = readFASTA(open(sys.argv[1]))
#using the provided fasta.py function to decipher the fasta file given in the system line as index 1

seq1_id, sequence1 = input_sequences[0]
#setting sequence1 variable as index 0 of input_sequences variable (fasta parser)
seq2_id, sequence2 = input_sequences[1]
#setting sequence2 variable as index 1 of input_sequences variable (fasta parser)
gap_penalty = float(sys.argv[3])
#sets the gap penalty as whatever value is provided in system argument index 3, but also specifies whatever value is provided as a float

filescoremat = np.loadtxt(sys.argv[2], dtype=object, skiprows=1)
#loads in the score matrix file provided in system line index 2, but skips the first header row, and also specifies values included within as objects. this is necessary because the score matrix file includes both letters and numbers, or strings and integers
header = list(filescoremat[:,0])
#commits the first column of the score matrix file denoted above into a list. this will be used later on for indexing
scoremat = filescoremat[:,1:].astype(float)
#the actual score matrix lol. basically the previous filescoremat variable but also removing the first header column. this is just numbers essentially

Fmat = np.zeros((len(sequence1)+1,len(sequence2)+1))
#creating our f matrix by filling it with zeros based on the lengths of our sequence 1 and 2 found from our fasta file, add 1 for headers
Tmat = np.zeros((len(sequence1)+1,len(sequence2)+1))
#creating our traceback matrix by filling it with zeros based on the lengths of our sequence 1 and 2 found from our fasta file, add 1 for headers

for i in range(len(sequence1)+1):
    Fmat[i,0] = i*gap_penalty
    Tmat[i,0] = 1 #v = 1
    #this for loop is to fill in the first row of the f and traceback matrices. without this loop, it prints as full of zeros. the f matrix value should be the length of the sequence slowly multiplied by the gap penalty with increasing values, while the traceback matrix is the vertical integer.
for j in range(len(sequence2)+1):
    Fmat[0,j] = j*gap_penalty
    Tmat[0,j] = 2 #h = 2
    #this for loop is to fill in the first column of the f and traceback matrices. without this loop, it prints as full of zeros. the f matrix value should be the length of the sequence slowly multiplied by the gap penalty with increasing values, while the traceback matrix is the horizontal integer.
#print(Fmat)

for i in range(1, Fmat.shape[0]):
    for j in range(1, Fmat.shape[1]):
    #for rows and columns (i,j) in range of the shape of the fmatrix array...starts from row 1, column index 0, and row 1, column index 1
        row = header.index(sequence1[i-1])
        #sets variable row equal to that previous header list as an index for sequence1's location minus 1
        col = header.index(sequence2[j-1])
        #sets variable col (column) equal to that previous header list as an index for sequence2's location minus 1
        score = scoremat[row, col]
        #calculates score variable by using row and col variables within the scoremat set previously to find location    
        d = Fmat[i-1, j-1] + score
        #sets variable d (for diagonal not distance LOL) as location in Fmatrix -1 both horizontally and vertically  plus the score variable. Related to the substitution score taught in class
        h = Fmat[i,j-1] + gap_penalty
        #sets variable h (horizontal) as location in Fmatrix -1 column (to move horizontally) plus gap penalty specified in system line
        v = Fmat[i-1,j] + gap_penalty
        #sets variable v (vertical) as location in Fmatrix -1 row (to move vertically) plus gap penalty specified in system line
        Fmat[i,j] = max(d,h,v)
        #fills in position of fmatrix box by box with the maximum value between variables d, h, and v
        if d >= h and d >= v:
            Tmat[i,j] = 0
            #d = 0
            #if variable d is greater than h and v, fill in traceback matrix with integer 0 (it doesn't work with just the variable "d" as a string who knows why, maybe i do believe in a higher power)
        elif h >= d and h >= v:
            Tmat[i,j] = 2
            #if variable h is greater than d and v, fill in traceback matrix with integer 2, as a placeholder for variable h
        elif v >= h and v >= d:
            Tmat[i,j] = 1
            #you know the drill if variable v is greater than h and d, fill in traceback matrix in that location with integer 1, as a placeholder for variable v

i = Tmat.shape[0]-1
j = Tmat.shape[1]-1
align1 = ""
align2 = ""
#above are all defined variables for the following while loop. needs to be defined out of the loop otherwise it'll reset every time
#print(Tmat)
#exit()
while [i,j] != [0,0]:
#while loop, while location is not equal to 0,0...
    if Tmat[i,j] == 0: #d
        align1 += sequence1[i-1]
        align2 += sequence2[j-1]
        i -=1
        j-=1
        #if location in traceback matrix is equal to 0 (our diagonal variable), set align1 to sequence1 i minus 1 (moving horizontal back 1), set align2 to sequence2 j -1 (moving vertically up 1), move i and j both back 1. basically the align isn't actually moving the sequence, just filling in the value.
    elif Tmat[i,j] == 2: #h
        align1 += "-"
        align2 += sequence2[j-1]
        j-=1
        #similar to above but for moving horizontally. puts horizontal sequence as a gap instead of the value.
    elif Tmat[i,j] == 1: #v
        align1 += sequence1[i-1]
        align2 += "-"
        i-=1
        #similar to above but for moving vertically. puts vertical sequence as as gap instead of the value.

print(Fmat[-1,-1])
#prints the alignment score between sequences 1 and 2. The alignment score is the bottom right corner of the F matrix.
print(align1[::-1])
#prints alignment for sequence 1, aka variable align1. Prints in reverse [::-1]
print(align2[::-1])
#prints alignment for sequence 2, aka vatiable align2. Prints in reverse [::-1]
align1gap = align1.count("-")
print(align1gap)
#prints the align1gap variable, the count of the gap character used above ("-")
align2gap = align2.count("-")
print(align2gap)
#prints the align2gap variable, which was the count of the gap character used above ("-"). Don't ask me if I could've done this in one line nothing makes sense to me anymore

# for i,row in enumerate(Tmat(::-1)):
#     if i == 0:
#         best_ind = len(row)
#     else:
#         gap = best_ind
#         match = best_ind -1 #to the left and up
#         if row[gap] < row[match]:
#             best_ind = match
#         else:
#             best_ind = gap
#hey siri how do I become a nun in a tibetan monastery
#print(Fmat)


