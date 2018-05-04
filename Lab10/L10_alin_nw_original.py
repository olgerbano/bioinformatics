import numpy as np
from numpy import * 
from numpy import zeros, linspace
from sys import *

def simple(x, y):
    if x == y:
        return 1
    else:
        return -1
    
    
def BlosumScore(s1,s2):
	#from array import array
	BLOSUM = array([
    	[ 5,-2,-1,-2,-1,-1,-1, 0,-2,-1,-2,-1,-1,-3,-1, 1, 0,-3,-2, 0],
    	[-2, 7,-1,-2,-1, 1, 0,-3, 0,-4,-3, 3,-2,-3,-3,-1,-1,-3,-1,-3],
    	[-1,-1, 7, 2,-2, 0, 0, 0, 1,-3,-4,-0,-2,-4,-2,-1, 0,-4,-2,-3],
    	[-2,-2, 2, 8,-4, 0, 2,-1,-1,-4,-4,-1,-4,-5,-1, 0,-1,-5,-3,-4],
    	[-1,-4,-2,-4,13,-3,-3,-3,-3,-2,-2,-3,-2,-2,-4,-1,-1,-5,-3,-1],
    	[-1,-1, 0, 0,-3, 7, 2,-2, 1,-3,-2, 2, 0,-4,-1,-0,-1,-1,-1,-3],
    	[-1, 0, 0, 2,-3, 2, 6,-3, 0,-4,-3, 1,-2,-3,-1,-1,-1,-3,-2,-3],
    	[ 0,-3, 0,-1,-3,-2,-3, 8,-2,-4,-4,-2,-3,-4,-2, 0,-2,-3,-3,-4],
    	[-2, 0, 1,-1,-3, 1, 0,-2,10,-4,-3, 0,-1,-1,-2,-1,-2,-3,-1, 4],
    	[-1,-4,-3,-4,-2,-3,-4,-4,-4, 5, 2,-3, 2, 0,-3,-3,-1,-3,-1, 4],
    	[-2,-3,-4,-4,-2,-2,-3,-4,-3, 2, 5,-3, 3, 1,-4,-3,-1,-2,-1, 1],
    	[-1, 3, 0,-1,-3, 2, 1,-2, 0,-3,-3, 6,-2,-4,-1, 0,-1,-3,-2,-3],
    	[-1,-2,-2,-4,-2, 0,-2,-3,-1, 2, 3,-2, 7, 0,-3,-2,-1,-1, 0, 1],
    	[-3,-3,-4,-5,-2,-4,-3,-4,-1, 0, 1,-4, 0, 8,-4,-3,-2, 1, 4,-1],
    	[-1,-3,-2,-1,-4,-1,-1,-2,-2,-3,-4,-1,-3,-4,10,-1,-1,-4,-3,-3],
    	[ 1,-1, 1, 0,-1, 0,-1, 0,-1,-3,-3, 0,-2,-3,-1, 5, 2,-4,-2,-2],
    	[ 0,-1, 0,-1,-1,-1,-1,-2,-2,-1,-1,-1,-1,-2,-1, 2, 5,-3,-2, 0],
    	[-3,-3,-4,-5,-5,-1,-3,-3,-3,-3,-2,-3,-1, 1,-4,-4,-3,15, 2,-3],
    	[-2,-1,-2,-3,-3,-1,-2,-3, 2,-1,-1,-2, 0, 4,-3,-2,-2, 2, 8,-1],
    	[0,-3,-3,-4,-1,-3,-3,-4,-4, 4, 1,-3, 1,-1,-3,-2, 0,-3,-1, 5]]);
	PBET ='ARNDCQEGHILKMFPSTWYV';
	
	n1 = PBET.index(s1.upper());
	n2 = PBET.index(s2.upper());
	return BLOSUM[n1,n2];  

def NeedlemanWunsch(seq1, seq2, scoreMatrix=simple, g = -5):
    rows = len(seq1)
    cols = len(seq2)
    
    seq1 = '#' + seq1
    seq2 = '#' + seq2
    
    D = zeros((rows+1, cols+1), np.int32)
    
    #TODO - implementare algoritm
    
    #determinarea sirurilor celor doua secvente aliniate:
    #rows=len(seq1)+1;
    #cols=len(seq2)+1;
    for i in range(rows):
    	D[i][0] = i*g;
    for j in range(cols):
    	D[0][j] = j*g;
    for i in range(1,rows+1):
    	for j in range(1,cols+1):
    		D[i,j] = max(D[i-1,j-1] + scoreMatrix(seq1[i], seq2[j]), D[i-1,j] + g, D[i,j-1] + g);

    align1 = ''
    align2 = ''
    i = rows
    j = cols

    
    while i > 0 and j > 0:
        score = D[i, j]
        
        if score == D[i-1, j-1] + scoreMatrix(seq1[i], seq2[j]):
            align1 = seq1[i] + align1
            align2 = seq2[j] + align2
            i-=1
            j-=1

        elif score == D[i-1, j] + g:
            align1 = seq1[i] + align1
            align2 =     '-' + align2
            i-=1
            
        else: # score == D[i, j-1] + d
            align1 =     '-' + align1
            align2 = seq2[j] + align2
            j-=1
    
    align1 = '-'*j + seq1[1:i+1] + align1
    align2 = '-'*i + seq2[1:j+1] + align2
    
    return (align1, align2, D[rows,cols])

def NeedlemanWunschwBlosum(seq1, seq2, scoreMatrix=BlosumScore, g = -5):
    rows = len(seq1)
    cols = len(seq2)
    
    seq1 = '#' + seq1
    seq2 = '#' + seq2
    
    D = zeros((rows+1, cols+1), np.int32)
    
    #TODO - implementare algoritm
    
    #determinarea sirurilor celor doua secvente aliniate:
    #rows=len(seq1)+1;
    #cols=len(seq2)+1;
    for i in range(rows+1):
    	D[i][0] = 0
    for j in range(cols+1):
    	D[0][j] = 0
    for i in range(1,rows+1):
    	for j in range(1,cols+1):
    		choice1 = D[i-1,j-1] + scoreMatrix(seq1[i], seq2[j]);
    		choice2 = D[i-1,j] + g
    		choice3 = D[i,j-1] + g
    		D[i,j] = max(choice1, choice2, choice3);

    align1 = ''
    align2 = ''
    i = rows
    j = cols

    
    while i > 0 and j > 0:
        score = D[i, j]
        
        if score == D[i-1, j-1] + scoreMatrix(seq1[i], seq2[j]):
            align1 = seq1[i] + align1
            align2 = seq2[j] + align2
            i-=1
            j-=1

        elif score == D[i-1, j] + g:
            align1 = seq1[i] + align1
            align2 =     '-' + align2
            i-=1
            
        else: # score == D[i, j-1] + d
            align1 =     '-' + align1
            align2 = seq2[j] + align2
            j-=1
    
    align1 = '-'*j + seq1[1:i+1] + align1
    align2 = '-'*i + seq2[1:j+1] + align2
    
    return (align1, align2, D[rows,cols])


def displayAlignment(align1, align2):
    print(align1)
    
    p = ''.join(map(lambda x, y: str(int(x==y)), align1, align2))
    p = p.replace('1', '|')
    p = p.replace('0', ' ')
    print(p);
    
    print(align2);

if __name__ == '__main__':
    
    [a1, a2, sc] = NeedlemanWunsch('acgtc', 'tacgtcd')
    
    print(displayAlignment(a1,a2));
    print(sc);

    [a1, a2, sc] = NeedlemanWunschwBlosum('acgtc', 'tacgtcd')
    
    print(displayAlignment(a1,a2));
    print(sc);
