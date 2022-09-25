
import collections
with open('rosalind_dna (3).txt','r') as fr:
    seq = ''

    for line in fr:
        if ">" in line:               
            continue
        else:
            line = line.rstrip("\n")
            seq = seq+line 
            
Nucleotides = ["A", "C", "G", "T"]

def validateSeq(dna_seq):
    tmpseq = dna_seq.upper()
    for nuc in tmpseq:
        if nuc not in Nucleotides:
            return False
    return tmpseq

#print(validateSeq(seq)) 

def countNucFrequency(seq):
    return dict(collections.Counter(seq))

print(countNucFrequency(seq))

total_len = len(seq)
ContC = round((seq.count("C")/total_len)*100,2)
ContG = round((seq.count("G")/total_len)*100,2)
print('content of C: ',ContC ,'%')
print('content of G: ',ContG,'%')

suma = round(ContG + ContC,2)
print ('Contenido GC: ', suma,'%')


