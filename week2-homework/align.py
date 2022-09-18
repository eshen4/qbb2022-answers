#!/usr/bin/env python3

import sys
import numpy as np
from fasta import readFASTA

sys.argv[1:]

input_sequences = readFASTA(open(sys.argv[1]))

seq1_id, sequence1 = input_sequences[0]
seq2_id, sequence2 = input_sequences[1]
gap_penalty = float(sys.argv[3])

filescoremat = np.loadtxt(sys.argv[2], dtype=object, skiprows=1)
header = list(filescoremat[:,0])
scoremat = filescoremat[:,1:].astype(float)

Fmat = np.zeros((len(sequence1)+1,len(sequence2)+1))
Tmat = np.zeros((len(sequence1)+1,len(sequence2)+1))

for i in range(len(sequence1)+1):
    Fmat[i,0] = i*gap_penalty
    Tmat[i,0] = 1 #v = 1
for j in range(len(sequence2)+1):
    Fmat[0,j] = j*gap_penalty
    Tmat[0,j] = 2 #h = 2
#print(Fmat)

for i in range(1, Fmat.shape[0]):
    for j in range(1, Fmat.shape[1]):
        row = header.index(sequence1[i-1])
        col = header.index(sequence2[j-1])
        score = scoremat[row, col]    
        d = Fmat[i-1, j-1] + score
        h = Fmat[i,j-1] + gap_penalty
        v = Fmat[i-1,j] + gap_penalty
        Fmat[i,j] = max(d,h,v)
        if d >= h and d >= v:
            Tmat[i,j] = 0
            #d = 0
        elif h >= d and h >= v:
            Tmat[i,j] = 2
        elif v >= h and v >= d:
            Tmat[i,j] = 1

i = Tmat.shape[0]-1
j = Tmat.shape[1]-1
align1 = ""
align2 = ""
#print(Tmat)
# exit()
while [i,j] != [0,0]:
    if Tmat[i,j] == 0: #d
        align1 += sequence1[i-1]
        align2 += sequence2[j-1]
        i -=1
        j-=1
    elif Tmat[i,j] == 2: #h
        align1 += "-"
        align2 += sequence2[j-1]
        j-=1
    elif Tmat[i,j] == 1: #v
        align1 += sequence1[i-1]
        align2 += "-"
        i-=1

print(Fmat[-1,-1])
print(align1[::-1])
print(align2[::-1])
align1gap = align1.count("-")
print(align1gap)
align2gap = align2.count("-")
print(align2gap)


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


