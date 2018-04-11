gene = open("sequence.txt","r")

gene.readline()

nr_A = 0;
nr_G = 0;
nr_C = 0;
nr_T = 0;

for line in gene:
	for char in line:
		if char == "A":
			nr_A = nr_A + 1;
		if char == "G":
			nr_G = nr_G + 1;
		if char == "C":
			nr_C = nr_C + 1;
		if char == "T":
			nr_T = nr_T + 1;

print("nr of A's is "+ str(nr_A));
print("nr of T's is "+ str(nr_T));
print("nr of G's is "+ str(nr_G));
print("nr of C's is "+ str(nr_C));
GC = nr_G+nr_C + 0.;
Total = nr_C+nr_G+nr_T+nr_A + 0.;

p_GC = GC/Total;

print(str(p_GC));
