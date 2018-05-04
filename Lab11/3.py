from Bio import SeqIO
from Bio.Alphabet import IUPAC
from Bio import Entrez
Entrez.email = 'abc@gmail.com' #o adresa de e-mail
#cautarea unei gene in baza de date cu nucleotide si extragerea informatiei in

#extragerea informatiei
handle = Entrez.efetch(db="nuccore", id="NC_016438", rettype="gb", retmode='text')
#salvarea informatiei extrase intr-un SeqRecord
secrec = SeqIO.read(handle, "gb")
print(secrec.seq.alphabet);
handle.close()
#scrierea secventei in fisierul gb
handle = open("searchNC_016438.gb", "w")
SeqIO.write([secrec], handle, "gb")
handle.close()