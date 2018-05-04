from Bio import SeqIO
record = SeqIO.read(open("searchNC_016438.gb"), "genbank")
print(type(record));
print(record.features);
#from Bio.SeqRecord import SeqRecord
#simple_seq_r = SeqRecord(record)
#print(simple_seq_r);