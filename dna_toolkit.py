from structures import *


def validateSeq(dna_seq):
    '''Checks if DNA Sequence has the correct letters '''
    temsep = dna_seq.upper()
    for nuc in temsep:
        if nuc not in nucleotides:
            return False
    return temsep


def countNucFrequency(seq):
    temFreqDict = {'A': 0, 'C': 0, 'G': 0, 'T': 0}
    for nuc in seq:
        temFreqDict[nuc] += 1
    return temFreqDict


def transcription(seq):
    return seq.replace('T', 'U')


def reverse_complement(seq):
    return ''.join([DNA_reverse_complement[nuc] for nuc in seq])[::-1]


def gc_content(seq):
    return round((seq.count('C') + seq.count('G')) / len(seq) * 100)


def gc_content_subsec(seq, k=20):
    res = []
    for i in range(0, len(seq) - k + 1, k):
        subseq = seq[i:i + k]
        res.append(gc_content(subseq))
    return res
