import re

def pat_maker(forward, reverse):
    forward, reverse = forward.upper(), reverse.upper()
    forwdcode = {'A': 'A', 'T': 'T', 'C': 'C', 'G': 'G'}
    revcode = {'A': 'T', 'T': 'A', 'C': 'G', 'G': 'C'}
    pattern = ''
    for i in forward:
        pattern += forwdcode[i]
    for j in reversed(reverse):
        pattern += revcode[j]
    return pattern

def amplicon_finder(filename, pattern):
    file = open(filename, 'r')
    genome = ''
    for row in file:
        if '>' not in row:
            genome += row.strip()
        else:
            genome += '\n' + row
    result = re.findall(pattern, genome)
    file.close()
    return result

if __name__ == '__main__':
    filenameX = input('Введите .fasta файл: ')
    forwardX = input('Введите прямой праймер: ')
    reverseX = input('Введите обратный праймер ')
    patternX = pat_maker(forwardX, reverseX)
    ampliconX = amplicon_finder(filenameX, patternX)
    for i in ampliconX:
        print(i)
        print()
