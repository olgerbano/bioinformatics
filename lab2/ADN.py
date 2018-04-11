def ADN(n):
	import random
	
	secv = ""
	
	for i in range(n):

		x=random.randint(0,3);

		if x ==0:
			secv = secv+'T';
		elif x == 1:
			secv = secv+'A';
		elif x == 2:
			secv = secv+'G';
		elif x == 3:
			secv = secv+'C';

	return secv	

ADN = ADN(6)

print(ADN)
print(ADN[0])