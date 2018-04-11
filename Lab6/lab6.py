import string
def copyy(fin,fout):
	fisier_in = open(fin,'r');
	fisier_out = open(fout,'w');
	nr_line = 0
	for line in fisier_in:
		if nr_line==0:
			nr_line+=1
			continue;
		line = line.strip();
		fisier_out.write(line+'\n')
		nr_line+=1
	fisier_in.close();
	fisier_out.close();

def copyy2(fin,f2in,fout):
	fisier_in = open(fin,'r');
	fisier2_in = open(f2in,'r');
	fisier_out = open(fout,'w');
	for line in fisier_in:
		line = line.strip();
		fisier_out.write(line+'\n');
	for line in fisier2_in:
		line = line.strip();
		fisier_out.write(line+'\n');

	fisier_in.close();
	fisier2_in.close();
	fisier_out.close();
def firstasn1(fin,fout):
	fisier_in = open(fin,'r');
	fisier_out = open(fout,'w');
	ok = 0;
	SS = "AA"
	for line in fisier_in:
		if (ok==0 and len(SS)==0):
			#print(SS);
			break;
		line = line.strip();
		if 'ncbi2na' in line:
			SS = "";
			ok = 1;
			SS +=line;
			fisier_out.write(line[line.find(' ')+2:]+'\n');
			continue;
		if (ok == 1 and 'H } ,' not in line):
			SS +=line;
			fisier_out.write(line+'\n');
			continue;
		if ('H } ,' in line and ok==1):
			SS += line;
			ok = 0;
			print(SS);
			fisier_out.write(line[:line.find(' ')-2]);
			SS = "";

def allasn1(fin,fout):
	fisier_in = open(fin,'r');
	fisier_out = open(fout,'w');
	ok = 0;
	SS = "AA"
	for line in fisier_in:
		line = line.strip();
		if 'ncbi2na' in line:
			SS = "";
			ok = 1;
			SS +=line;
			fisier_out.write(line[line.find(' ')+2:]+'\n');
			continue;
		if (ok == 1 and 'H } ,' not in line):
			SS +=line;
			fisier_out.write(line+'\n');
			continue;
		if ('H } ,' in line and ok==1):
			SS += line;
			ok = 0;
			#print(SS);
			fisier_out.write(line[:line.find(' ')-2]+'\n'+'\n');
			SS = "";

if __name__ == '__main__':
	copyy('nucleot.fasta','text.fasta');
	copyy2('nucleot.fasta','protein.fasta','text2.fasta');
	firstasn1('multiregion.asn1','text3.fasta');
	allasn1('multiregion.asn1','text4.fasta');