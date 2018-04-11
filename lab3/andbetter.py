import random

def AorT():
	
	x=random.randint(0,1);
	if x ==0:
		c = 'T';
	elif x == 1:
		c = 'A';
	return c

def GorC():
	x=random.randint(0,1);
	if x ==0:
		c = 'G';
	elif x == 1:
		c = 'C';
	return c

def ADN(n):

	
	secv = "";


	for i in range(0,n):
		if (i & 1) == 0:
			x=random.randint(0,3);
			
			if x == 0:
				secv = secv+'T';
			elif x == 1:
				secv = secv+'A';
			elif x == 2:
				secv = secv+'G';
			elif x == 3:
				secv = secv+'C';

		 		
		if (i & 1) == 1:

			if (secv[len(secv)-1]=='A' or secv[len(secv)-1]=='T'):
				secv = secv + AorT();
				
			else:
				secv = secv + GorC();

	return secv	

ADN = ADN(16)

print(ADN)
