
def readFile(filePath):
    """Reading a file and returning a list of lines"""
    with open(filePath, 'r') as f:
        return [l.strip() for l in f.readlines()]

def gc_content(seq):
    """GC CONTENT IN A DNA/RNA SEQUENCE"""
    return round((seq.count('C') + seq.count('G'))/len(seq) * 100, 6)

FASTAFile = readFile("/Users/mariaalejandrarojo/Desktop/MR/Bioinformatics/Rosalind-problems/test_data/gc_content.txt")
FASTADict = {}
FASTALabel = ""

# print(FASTAFile)
 
for line in FASTAFile:
    if '>' in line:
        FASTALabel = line
        FASTADict[FASTALabel] = ""
    else: 
        FASTADict[FASTALabel] += line

# print(FASTADict)

RESULTDict = {key: gc_content(value) for (key, value) in FASTADict.items()}
# print(RESULTDict)

MaxGCkey = max(RESULTDict, key=RESULTDict.get)


print(f'{MaxGCkey[1:]}\n{RESULTDict[MaxGCkey]}')

