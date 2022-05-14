from Bio import SeqIO

seqs = input('Введите имя .fasta файла: ')
sequence = SeqIO.parse(open(seqs), 'fasta')
table = 1
min_pro_len = 100
for feature in sequence:
    for strand, nuc in [(+1, feature.seq), (-1, feature.seq.reverse_complement())]:
        for frame in range(3):
            for pro in nuc[frame:].translate(table).split("*"):   # транслирует каждый кадр и возвращает аминокислотную
                                                                  # цепочку, где каждый стоп-кодон закодирован как *
                if len(pro) >= min_pro_len:         # если длина больше 100
                    print("%s...%s - length %i, strand %i, frame %i" % (pro[:30], pro[-3:], len(pro), strand, frame))
