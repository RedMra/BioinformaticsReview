
from bio_structs import DNA_Codons, DNA_Nucleotides
from collections import Counter
import random


class bio_seq:
    """DNA sequence class . Defalt value: ATCG, DNA, No label"""
    def __init__(self, seq="ATCG", seq_type="DNA", label='No label'):
        self.seq = seq.upper()
        self.label = label
        self.seq_type = seq_type
        self.is_valid = self.__validate() 
        assert self.is_valid, f"Provided data does not seem to be correct {self.seq_type} sequence"

    #DNA toolkit functions
    def __validate(self):# __ para poner pribada 
        return set(DNA_Nucleotides).issuperset(self.seq)

    def get_seq_biotype(self):
        return self.seq_type

    def get_seq_info(self):
        return f"[label]: {self.label}\n[Sequence]: {self.seq}\n[Biotype]: {self.seq_type}\n[Length]: {len(self.seq)}"

    def generate_rnd_seq(self, length =10,seq_type="DNA"):
        seq = ''.join([random.choice(DNA_Nucleotides)
            for X in range(length)])
        self.__init__(seq, seq_type, " ramdomly generated sequence")

    def nucleotide_frequency(self):
        return dict(Counter(self.seq))
    
    def transcription(self):
        return self.seq.replace("T","U")

    def  reverse_complement(self):
        mapping = str.maketrans('ATCG', 'TAGC')
        return self.seq.translate(mapping)[::-1]

    def gc_content(self):
        return round((self.seq.count('C') + self.seq.count('G'))/len(self.seq) * 100)

    def gc_content_subsec(self, k = 20):
        res = []  
        for i in range(0, len(self.seq) - k + 1, k):  
            subseq = self.seq[i:i + k]
            res.append(
                round((subseq.count('C') + subseq.count('G')) /len(subseq) * 100))
        return res
    
    def translate_seq(self, init_pos = 0):
        return [DNA_Codons[self.seq[pos:pos + 3]] for pos in range(init_pos,len(self.seq) - 2, 3)]

    def codon_usage(self, aminoacid):
        tmpList = []
        for i in range(0, len(self.seq) - 2, 3):
            if DNA_Codons[self.seq[i:i + 3]]== aminoacid:
                tmpList.append(self.seq[i:i + 3])
        
        freqDict = dict(Counter(tmpList))
        totalWight = sum(freqDict.values())
        for seq in freqDict:
            freqDict[seq] = round(freqDict[seq] / totalWight, 2)
        return freqDict

    def gen_reading_frames(self):
        frames = []
        frames.append(self.translate_seq(0))
        frames.append(self.translate_seq(1))
        frames.append(self.translate_seq(2))
        tmp_seq = bio_seq(self.reverse_complement(), self.seq_type)
        frames.append(tmp_seq.translate_seq(0))
        frames.append(tmp_seq.translate_seq(1))
        frames.append(tmp_seq.translate_seq(2))
        del tmp_seq
        return frames

    def proteins_from_rf(self, aa_seq):
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

    def all_proteins_from_orfs(self, starReadpos=0, endReadpos=0, ordered=False):
        if endReadpos > starReadpos:
            tmp_seq = bio_seq(
                self.seq[starReadpos: endReadpos], self.seq_type)
            rfs = tmp_seq.gen_reading_frames()
        else:
            rfs = self.gen_reading_frames()

        Res = []
        for rf in rfs:
            prots = self.proteins_from_rf(rf)
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

