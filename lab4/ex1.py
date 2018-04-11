import random
import re

def makelist(k):
    i=0;
    stdcode = {
        'TTT':'Phe', 'TTC':'Phe', 'TTA':'Leu', 'TTG':'Leu', 'TCT':'Ser',
        'TCC':'Ser', 'TCA':'Ser', 'TCG':'Ser', 'TAT':'Tyr', 'TAC':'Tyr',
        'TAA':'Stop', 'TAG':'Stop', 'TGT':'Cys', 'TGC':'Cys', 'TGA':'Stop',
        'TGG':'Trp', 'CTT':'Leu', 'CTC':'Leu', 'CTA':'Leu', 'CTG':'Leu',
        'CCT':'Pro', 'CCC':'Pro', 'CCA':'Pro', 'CCG':'Pro', 'CAT':'His',
        'CAC':'His', 'CAA':'Gln', 'CAG':'Gln', 'CGT':'Arg', 'CGC':'Arg',
        'CGA':'Arg', 'CGG':'Arg', 'ATT':'Ile', 'ATC':'Ile', 'ATA':'Ile', 'ATG':'Met',
        'ACT':'Thr', 'ACC':'Thr', 'ACA':'Thr', 'ACG':'Thr', 'AAT':'Asn', 'AAC':'Asn', 'AAA':'Lys', 'AAG':'Lys',
        'AGT':'Ser', 'AGC':'Ser', 'AGA':'Arg', 'AGG':'Arg', 'GTT':'Val', 'GTC':'Val', 'GTA':'Val', 'GTG':'Val',
        'GCT':'Ala', 'GCC':'Ala', 'GCA':'Ala', 'GCG':'Ala', 'GAT':'Asp', 'GAC':'Asp', 'GAA':'Glu', 'GAG':'Glu',
        'GGT':'Gly', 'GGC':'Gly', 'GGA':'Gly', 'GGG':'Gly'};
    new_secv = "";
    ajut ="ATGC";
    secventa = "";
    codificat="";
    for i in range(int(k)):

        secv = "";
        secv+=str(ajut[random.randint(0,3)]);
        secv+=str(ajut[random.randint(0,3)]);
        secv+=str(ajut[random.randint(0,3)]);
        secventa+=secv;
        codificat += stdcode[secv];
        codificat+=" ";
        secventa+=" ";
    print(secventa);
    print(codificat);
    return [secventa,codificat];
def makeonel(seq):
    aminocode = {
        'Gly' : 'G', 'Ala' : 'A', 'Pro' : 'P', 'Val' : 'V',
        'Ile' : 'I', 'Leu' : 'L', 'Phe' : 'F', 'Met' : 'M',
        'Ser' : 'S', 'Cys' : 'C', 'Thr' : 'T', 'Asn' : 'N',
        'Gln' : 'Q', 'His' : 'H', 'Tyr' : 'Y', 'Trp' : 'W',
        'Asp' : 'D', 'Glu' : 'E', 'Lys' : 'K', 'Arg' : 'R'
        };
    secv = seq.replace(" ","");
    #print(secv);
    if secv[0:4]=="Stop":
        return "Stop is the first";
    if secv.find("Stop") == -1:
        secv=secv;
    else:
        secv = secv[0:secv.find("Stop")];
    #print(secv);
    protein =""
    if len(secv)%3 == 0:
        for i in range(0, len(secv), 3):
            codon = secv[i:i + 3]
            protein+= aminocode[codon]
            protein+=" ";
    return protein

secv, codificat = makelist(5);
protein = makeonel(codificat);
print(protein);
