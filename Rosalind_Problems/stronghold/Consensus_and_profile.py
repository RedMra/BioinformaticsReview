
def read_FASTA(filePath):
    with open(filePath, 'r') as f:
        FASTAFile = [l.strip() for l in f.readlines()]

    FastaDict = {}
    FASTALabel = ""

    for line in FASTAFile:
        if '>' in line:
            FASTALabel = line
            FastaDict[FASTALabel] = ""
        else:
            FastaDict[FASTALabel] += line
    return FastaDict
Fastafiel = (read_FASTA("/Users/mariaalejandrarojo/Library/CloudStorage/GoogleDrive-mra.rojo@gmail.com/Mi unidad/Escritorio Mac/MR/Bioinformatics-Review/Rosalind_Problems/test_data/gc_content.txt"))


def alignment_seq(fasta):
    fasta_list = list(fasta.values())
    ceros = [0 for i in range(len(fasta_list[0]))]
    seq_counter = {"A": ceros.copy() , "C": ceros.copy(), "G": ceros.copy(), "T": ceros.copy()}
    for seq in fasta.values():
        for i in range(len(ceros)):
                seq_counter[seq[i]][i] += 1
    return (seq_counter)
     
seq_counter = alignment_seq(Fastafiel)

def max_seq(seq_dict):
    size = len(seq_dict["A"])
    consensus = ""
    for i in range(size):
        max_nuc = ""
        max_val = 0
        for key in seq_dict.keys():
            if max_val < seq_dict[key][i]:
                max_nuc = key
                max_val = seq_dict[key][i]
        consensus += max_nuc
    return consensus

print(max_seq(seq_counter))
for key, value in seq_counter.items():
        value_str = [str(i) for i in value]    
        value_str = ' '.join(value_str)
       
        print(f'{key}' + ': ' + value_str)




    

