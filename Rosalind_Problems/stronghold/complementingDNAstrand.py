
Nucleotides = ["A", "C", "G", "T"]
DNA_reverseComplement = {'A': 'T', 'T': 'A', 'G': 'C', 'C': 'G'}


def  reverse_complement(seq):
    """Swapping adenine with thymine and guanine with cytosine.reversing newly generated string """
    return ''.join([DNA_reverseComplement[nuc] for nuc in seq])[::-1]

seq = ("AAAACCCGGT")

print (reverse_complement(seq))