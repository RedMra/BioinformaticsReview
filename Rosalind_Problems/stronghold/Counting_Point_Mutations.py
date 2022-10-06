seq1 =  "GAGCCTACTAACGGGAT"
seq2 =  "CATCGTAATGACGGCCT"
seq_1 = list(seq1) 
seq_2 = list(seq2)

def mutation_counter():
    counter = 0
    for i in range(len(seq_1)):
        if seq_1[i] != seq_2[i]:
            counter += 1
    return counter

print(mutation_counter()) 

# A Pythonic version 

def mutation_counter_2():
    counter = 0
    for pair in zip(seq1, seq2):
        if pair[0]!=pair[1]:
            counter += 1
    return counter

print(mutation_counter_2())