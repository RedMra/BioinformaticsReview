
from ast import Return
import collections 
from typing import Mapping
from structures import *

def validateSeq(dna_seq):
    tmpseq = dna_seq.upper()
    for nuc in tmpseq:
        if nuc not in Nucleotides:
            return False
    return tmpseq   

def countNucFrequency(seq):
    tmpFreqDict = {"A":0, "C": 0, "G": 0, "T" : 0 }
    for nuc in seq:
        tmpFreqDict[nuc] += 1
    return tmpFreqDict

def transcription(seq):
    """DNA -> RNA transcription. Replaacing  thymine with Uracil"""
    return seq.replace("T","U")

def  reverse_complement(seq):
    """Swapping adenine with thymine and guanine with cytosine.reversing newly generated string """
    return ''.join([DNA_reverseComplement[nuc] for nuc in seq])[::-1]      

def gc_content(seq):
    """GC CONTENT IN A DNA/RNA SEQUENCE"""
    return round((seq.count('C') + seq.count('G'))/len(seq) * 100)

def gc_content_subsec(seq, k = 20):
    """GC content in a DNA/RNA sub-sequence length k. k=20 by default"""
    res = []  #definir una lista
    for i in range(0, len(seq) - k + 1, k): # for loop 
        subseq = seq[i:i + k]
        res.append(gc_content(subseq))
    return res

def translate_seq(seq,init_pos = 0):
    """Translates a DNA sequence into an aminoacid sequence"""
    return [DNA_Codons[seq[pos:pos + 3]] for pos in range(init_pos,len(seq) - 2, 3)]

def codon_usage(seq,aminoacid):
    """Provides the frequency of each codon encoding a given aminoacid in a DNA sequence"""
    tmpList = []
    for i in range(0, len(seq) - 2, 3):
        if DNA_Codons[seq[i:i + 3]]== aminoacid:
            tmpList.append(seq[i:i + 3])
    
    freqDict = dict(collections.Counter(tmpList))
    totalWight = sum(freqDict.values())
    for seq in freqDict:
        freqDict[seq] = round(freqDict[seq] / totalWight, 2)
    return freqDict

def gen_reading_frames(seq):
    """Genereta the six reading frames of DNA sequence, includingthe reverse complement"""
    frames = []
    frames.append(translate_seq(seq, 0))
    frames.append(translate_seq(seq, 1))
    frames.append(translate_seq(seq, 2))
    frames.append(translate_seq(reverse_complement(seq), 0))
    frames.append(translate_seq(reverse_complement(seq), 1))
    frames.append(translate_seq(reverse_complement(seq), 2))
    return frames 

def proteins_from_rf(aa_seq):
    """Compute all possible proteins in an aminoacid seq and return a listo of possible proteins"""
    current_prot = []
    proteins = []
    for aa in aa_seq:
        if aa == "_":
            #stop accumulating amino acids if _ - stop was found
            if current_prot:
                for p in current_prot:
                    proteins.append(p)
                current_prot = []
        else:
       #STARt accumulating amino acids if M.star was found
            if aa == "M":
                current_prot.append("")
            for i in range(len(current_prot)):
                current_prot[i] += aa
    return  proteins

# Generete all RF
#Extrac all prots
#return a list sorted/unsorted 

def all_proteins_from_orfs(seq, starReadpos=0, endReadpos=0, ordered=False):
    """Compute all possible proteins for all open reading frames"""
    """Protine search DB https//ncbi.nlm.nih.gov/nuccore/NM_001185097.2"""
    """API can be used to pull protein info"""
    if endReadpos > starReadpos:
        rfs = gen_reading_frames(seq[starReadpos: endReadpos])
    else:
        rfs = gen_reading_frames(seq)

    Res = []
    for rf in rfs:
        prots = proteins_from_rf(rf)
        for p in prots:
            Res.append(p)

    if ordered:
        return sorted(Res, key=len, reverse=True)
    return Res            

# def readFile(filePath):
#     """Reading a file and returning a list of lines"""
#     with open(filePath, 'r') as f:
#         return [l.strip() for l in f.readlines()]

# seq_nn = readFile("/Users/mariaalejandrarojo/Desktop/MR/Bioinformatics/Test_Data/NM_000207.3.fasta")
# seq_str = ""

# for line in seq_nn:
#     if '>' in line:
#         pass
#     else: 
#         seq_str += line




