seq_s = "GATATATGCATATACTT"
seq_k = "ATAT"

def lookig_seq(seq):
    new_list = []
    first = seq.find(seq_k)
    if first >=0:
        while True:
            new_list.append(first+1)
            first = seq.find(seq_k,first+1)
            if first == -1:
                break
    return new_list

print(lookig_seq(seq_s))
