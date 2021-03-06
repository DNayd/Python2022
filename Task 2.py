from Bio import SeqIO
from collections import Counter
seqs = input('Введите имя .fasta файла: ')
sequence = SeqIO.parse(open(seqs), 'fasta')
print(f"{'Name':<10} {'Length':<10} {'Bases frequency:':<50}")
for feature in sequence:
    print(f'{feature.name:<10} {len(feature):<10} {str(dict(Counter(feature))):<50}')
