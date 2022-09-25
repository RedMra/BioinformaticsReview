# import this
from collections import Counter 


# === VARIABLES AND SOME ARITMETIC ===
# a = 924
# B = 822

# hipotenusa = int(a**2 + B**2)
# print (hipotenusa)

# a = 803
# b = 993

# print(f'{a}**2 + {b}**2 = {a**2 + b**2} ')

# ===STRINGS AND LISTS====

# wordoneStarPos = 13
# wordoneEndPos = 19

# wordTwoStarPos = 116
# wordTwoEndPos = 123

# txtStr = "6yIlP0G1m7flFScincus6sInrKnyuvMcAe09mh7udo4RDvOI5XpxP7crKdKlblP0Mrtomtdd7rGEctGku7TzTPbsgJPo0vSs0yJks5Xe7QO60AQiA4x4cinereusBtHmyzHk7Z69cu5kZhkfbuE5UQz2XqFVS8rCeVVpTdGZv3admRC80KJPNbdoGYMsEfx"

# # note :end position is not inclusive, so we add 1 to capture it

# print (
#     f'{txtStr[wordoneStarPos:wordoneEndPos +1]} {txtStr[wordTwoStarPos:wordTwoEndPos +1 ]}')

# === CONDITIONS AND LOOPS ====

starp = 100
endP = 200

# result = 0 

# for i in range(starp, endP+1):
#     if i % 2 != 0:
#         result += i

# or 

# result = [x for x in range(starp, endP+1) if x % 2 != 0]

# or 
 
# result = sum([x for x in range(starp, endP+1) if x % 2 != 0])
# print(result)

# ==== WORKING WITH FILE === 

outputFile = []

with open('/Users/mariaalejandrarojo/Desktop/MR/Bioinformatics/Rosalind-problems/Village/input.txt', 'r') as f:
       outputFile = [line for pos, line in enumerate(
              f.readlines()) if pos % 2 != 0]

print(outputFile) 

with open('/Users/mariaalejandrarojo/Desktop/MR/Bioinformatics/Rosalind-problems/Village/out.txt', 'w')  as f:
    f.write(''.join([line for line in outputFile]))
    

#==== Dictionaries  ===

txtstr = "When I find myself in times of trouble Mother Mary comes to me Speaking words of wisdom let it be And in my hour of darkness she is standing right in front of me Speaking words of wisdom let it be Let it be let it be let it be let it be Whisper words of wisdom let it be And when the broken hearted people living in the world agree There will be an answer let it be For though they may be parted there is still a chance that they will see There will be an answer let it be Let it be let it be let it be let it be There will be an answer let it be Let it be let it be let it be let it be Whisper words of wisdom let it be Let it be let it be let it be let it be Whisper words of wisdom let it be And when the night is cloudy there is still a light that shines on me Shine until tomorrow let it be I wake up to the sound of music Mother Mary comes to me Speaking words of wisdom let it be Let it be let it be let it be yeah let it be There will be an answer let it be Let it be let it be let it be yeah let it be Whisper words of wisdom let it be"

# wordcoutDict = {}

# for word in txtstr.split(' '):
#     if word in wordcoutDict:
#         wordcoutDict[word] += 1 
#     else:
#         wordcoutDict[word] = 1

#print(txtstr.split(' ')) 
# print(txtstr.split(' ')) convierte en lista teniendo en curnta los espacios
#['We', 'tried', 'list', 'and', 'we', 'tried', 'dicts', 'also', 'we', 'tried', 'Zen']

# for key, value in wordcoutDict.items():
#     print(key, value)

# or 
wordcountDict = Counter(txtstr.split(' '))


for key, value in wordcountDict.items():
       print(key, value)