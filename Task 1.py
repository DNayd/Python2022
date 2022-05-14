from Bio import SeqIO
seqs = input('Введите имя .fasta файла: ')
sequence = SeqIO.parse(open(seqs), 'fasta')
for feature in sequence:
    print(f'id:{feature.id} name:{feature.name}\nseqs {feature.seq}')
