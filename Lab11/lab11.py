from Bio import SeqIO
from Bio.Alphabet import IUPAC
from Bio import Entrez
Entrez.email = 'abc@gmail.com' #o adresa de e-mail
#cautarea unei gene in baza de date cu nucleotide si extragerea informatiei in
#format FASTA
handle = Entrez.esearch(db="nucleotide",term="PAX-6[Gene]")
#print(handle)
rec = Entrez.read(handle)
print (rec["Count"])
print (rec["IdList"])
#extragerea informatiei
handle1 = Entrez.efetch(db="nucleotide", id=rec["IdList"][1], rettype="fasta")
#salvarea informatiei extrase intr-un SeqRecord
secrec1 = SeqIO.read(handle1, "fasta")
handle1.close()

#extragerea informatiei
handle5 = Entrez.efetch(db="nucleotide", id=rec["IdList"][5], rettype="fasta")
#salvarea informatiei extrase intr-un SeqRecord
secrec5 = SeqIO.read(handle5, "fasta")
handle5.close()

#scrierea secventei in fisierul FASTA
handle1 = open("search1.fasta", "w")
SeqIO.write([secrec1], handle1, "fasta")
handle1.close()

#scrierea secventei in fisierul FASTA
handle5 = open("search5.fasta", "w")
SeqIO.write([secrec5], handle5, "fasta")
handle5.close()