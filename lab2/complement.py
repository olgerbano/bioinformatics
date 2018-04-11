def catenaADN(secv):
	complement = {'A': 'T','T': 'A','C': 'G','G': 'C'};
	new_secv = ""
	for char in secv:
		new_secv = new_secv + complement[char];
	return new_secv

ADN = input("Enter adn: ");

new = catenaADN(ADN);
print(new);


