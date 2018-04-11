def align_asym(seq1, seq2):
    i = 0
    while i < len(seq1) and i < len(seq2):
        if seq1[i] == seq2[i]:
            i += 1
        else:
            k = i
            min_idx1 = len(seq1)
            min_idx2 = len(seq2)
            while k < min_idx2 and k < len(seq1):
                idx = seq2.find(seq1[k], i)
                if idx >= 0 and min_idx2 > idx:
                    min_idx1 = k
                    min_idx2 = idx
                k += 1
            if min_idx1 > min_idx2:
                seq2 = seq2[:min_idx2] \
                    + '-' * (min_idx1 - min_idx2) \
                    + seq2[min_idx2:]
            elif min_idx1 < min_idx2:
                seq1 = seq1[:min_idx1] \
                    + '-' * (min_idx2 - min_idx1) \
                    + seq1[min_idx1:]
            i = max(min_idx1, min_idx2) + 1
    i = len(seq1)
    j = len(seq2)
    if i < j:
        seq1 = seq1 + '-' * (j - i)
    else:
        seq2 = seq2 + '-' * (i - j)

    #print(seq1+'\n'+seq2)
    return (seq1,seq2);
def afis(seq1,seq2):
    i = 0
    S = "";
#    nr_plus = 0
    while i < len(seq1) and i < len(seq2):
    	if seq1[i] == seq2[i]:
    		S +='+';
 #   		nr_plus +=1
    		i+=1
    	else:
    		S +='-';
    		i+=1
    print(S);

def simple_score(seq1,seq2):
    i = 0
    S = "";
    nr_plus = 0
    while i < len(seq1) and i < len(seq2):
    	if seq1[i] == seq2[i]:
    		S +='+';
    		nr_plus +=1
    		i+=1
    	else:
    		S +='-';
    		i+=1
    print(S);
    return( ((nr_plus/(i))*100))

def align(seq1,seq2):
	score1 = simple_score(seq1,seq2);
	score2 = simple_score(seq2,seq1);

	return max(score1,score2);
#print(align_asym("RQASPQT","RTSPTA"));
#plus_minus("RQASPQT-","RT-SP-TA");
tuple2 = (align_asym("RQASPQT","RTSPTA"))
#print(align("MALEKSLVRLLLLVLILLVLGWVQPSLGKESRAKKFQRQHMDSDSSPSSSSTYCNQMMRRRNMTQGRCKPVNTFVHEPLVDVQNVCFQEKVTCKNGQGNCYKSNSSMHITDCRLTNGSRYPNCAYRTSPKERHIIVACEGSPYVPVHFDASVEDST","MALEKSLVLLPLLVLILLVLGWVQPSLGKESRAKKFQRQHVDSDSSPSSSSTYCNQMMRRRNMTQGRCKPVNTFVHEPLVDVQNVCFQEKVTCKNGQGNCYKSNSSMHITDCRLTNGSRYPNCAYRTSPKERHIIVACEGSPYVPVHFDASVEDST"))
print(tuple2[0]);
print(tuple2[1]);
afis(tuple2[0],tuple2[1]);
print(simple_score(tuple2[0],tuple2[1]));