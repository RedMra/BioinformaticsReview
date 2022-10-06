
from bio_structs import RNA_Codons

seq_ARN = "AUGGCCAUGGCGCCCAGAACUGAGAUCAAUAGUACCCGUAUUAACGGGUGA"

def translate_seq(seq,init_pos = 0):
    """Translates a RNA sequence into an aminoacid sequence"""
    aminoA =  "".join([RNA_Codons[seq[pos:pos + 3]] for pos in range(init_pos,len(seq) - 2, 3)])
    return aminoA


print(translate_seq(seq_ARN))
 