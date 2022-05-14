from Bio import SeqIO
from collections import Counter
sequence = SeqIO.parse(open('/Users/dnayd/Documents/Python/pythonProject2022/sequences.fasta'), 'fasta')
print(f"{'Name':<10} {'Length':<10} {'Bases frequency:':<50}")
for feature in sequence:
    print(f'{feature.name:<10} {len(feature):<10} {str(dict(Counter(feature))):<50}')
