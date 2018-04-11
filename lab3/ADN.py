import random
import re
def catenaADNlist(lista):
	list1 = [];
	tuple1 = ();
	complement = {'A': 'T','T': 'A','C': 'G','G': 'C'};
	for l in lista:
		for i in range(0,3):
			tuple1+=(str(complement[l[i]]),);
		list1.append(tuple1);
		del tuple1;
		tuple1=();
	return list1;

def catenaARNlist(lista):
	list1 = [];
	tuple1 = ();
	complement = {'A': 'U','U': 'A','C': 'G','G': 'C'};
	for l in lista:
		for i in range(0,3):
			tuple1+=(str(complement[l[i]]),);
		list1.append(tuple1);
		del tuple1;
		tuple1=();
	return list1;

def catenaADN(secv):
	complement = {'A': 'T','T': 'A','C': 'G','G': 'C'};
	new_secv = ""
	for char in secv:
		new_secv = new_secv + complement[char];
	return new_secv

def catenaARN(secv):
	complement = {'A': 'U','U': 'A','C': 'G','G': 'C'};
	new_secv = ""
	for char in secv:
		new_secv = new_secv + complement[char];
	return new_secv

def andbe(n):
	list1 = [];
	tuple1 = ();
	ajut ="ATGC";

	for i in range(0,n):

		tuple1+=(str(ajut[random.randint(0,3)]),);
		tuple1+=(str(ajut[random.randint(0,3)]),);
		tuple1+=(str(ajut[random.randint(0,3)]),);
		#print(tuple1);
		list1.append(tuple1);
		del tuple1;
		tuple1=();
	return list1;

def afisare(list1,n):
	secv="";
	for i in range(0,n):
		for c in list1[i]:
			secv+=c;
	#print(secv);
def afis(secv):
	return (re.sub('[^a-zA-Z]+', '',str(secv)));

def number2(secv):
	sum_A = 0;
	sum_tot = 0;
	for i in range(0,len(secv)):
		if secv[i]=='A':
			sum_A +=1;
			sum_tot +=1;
		if secv[i] == 'T':
			sum_tot+=1;
	return(sum_tot,sum_A);

lista = andbe(6);
print(lista);
afisare(lista,6);
#secv = afis(lista);
#print(secv);
print("\n");

makeARN = catenaADNlist(lista);
print(makeARN);
#makeARN = secv.replace('T','U');

#print(makeARN);
#new_secv = catenaARN(makeARN);
#print(new_secv);
#secv = 'AAATTTCTCTGGTAGA';
#print(number2(secv));
