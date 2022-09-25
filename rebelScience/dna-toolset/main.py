
from tkinter import Frame
from DNAtoolkit import *
from Utilities import colored
import random

rndDNAStr = ''.join([random.choice(Nucleotides)
                    for nuc in range(200)])

DNAstr = validateSeq(rndDNAStr)

print(f'\nSequence: {colored(DNAstr)}\n')
print(f'[1] + sequence length: {len(DNAstr)}\n')
print(colored(f'[2] + Nucleotide Frequency: {countNucFrequency(DNAstr)}\n'))

print(f'[3] + DNA/RNA Transcription: {colored(transcription(DNAstr))}\n')

print(f"[4]+ DNA string + reverse_complement:\n \n 5'{colored(DNAstr)} 3' ")
print(f"   {''.join(['|' for C in range(len(DNAstr))])}")
print(f" 3' {colored(reverse_complement(DNAstr))} 5'[complement] \n")
print(f" 5'{colored((reverse_complement(DNAstr))[::-1])} 3' [rev. complement]\n")

print(f'[5] + GC content: {gc_content(DNAstr)}%\n')

print(
    f"[6] + GC content in subsection k=5: {gc_content_subsec(DNAstr, k=10)} \n")

print(
    f'[7] + Aminoacids sequence from DNA: {translate_seq(DNAstr)} \n')

print(
    f'[8] + Codon frequency (L): {codon_usage(DNAstr, "L")}\n')

print ('[9] + reading_frames:')
for frame in gen_reading_frames(DNAstr):   
    print(frame)

# test_rf_frame = ['H', 'M', 'I', 'N', 'S', 'V', 'T', 'V', 'V', 'T', 'P', 'D', 'N', '_', 'S', 'R']

# print(proteins_from_rf(test_rf_frame))


print('\n[10] + All prots in 6 apen reading franes:')
for prot in all_proteins_from_orfs(DNAstr, 0, 0, True):
    print(f'{prot}')

# print(seq_str)

