from Bio import SeqIO
from Bio.Alphabet import IUPAC
from Bio import Entrez
Entrez.email = 'abc@gmail.com' #o adresa de e-mail
#cautarea unei gene in baza de date cu nucleotide si extragerea informatiei in

#extragerea informatiei
handle = Entrez.efetch(db="nuccore", id="NC_009084", rettype="fasta")
#salvarea informatiei extrase intr-un SeqRecord
secrec = SeqIO.read(handle, "fasta")
print(secrec.seq.alphabet);
handle.close()
#scrierea secventei in fisierul FASTA
handle = open("searchNC_009084.fasta", "w")
SeqIO.write([secrec], handle, "fasta")
handle.close()


#extragerea informatiei
handle = Entrez.efetch(db="nuccore", id="NC_009084", rettype="fasta")
#salvarea informatiei extrase intr-un SeqRecord
secrec = SeqIO.read(handle, "fasta")
print(secrec.seq.alphabet);
secrec.seq.alphabet= IUPAC.unambiguous_dna;
print(secrec.seq.alphabet);
handle.close()
#scrierea secventei in fisierul FASTA
handle = open("searchNC_009084modalf.fasta", "w")
SeqIO.write([secrec], handle, "fasta")
handle.close();