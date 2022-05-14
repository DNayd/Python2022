from Bio import SeqIO
sequence = SeqIO.parse(open('/Users/dnayd/Documents/Python/pythonProject2022/sequences.fasta'), 'fasta')
for feature in sequence:
    print(f'id:{feature.id} name:{feature.name}\nseqs {feature.seq}')
