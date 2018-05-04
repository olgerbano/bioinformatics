from Bio import SeqIO
from Bio.Alphabet import IUPAC
from Bio.SeqFeature import SeqFeature
from Bio.SeqFeature import FeatureLocation
record = SeqIO.read(open("search1.fasta"), "fasta")
print(record)
print('\n');
record.seq.alphabet = IUPAC.unambiguous_dna;

print(record)