def transcription(seq):
    """DNA -> RNA transcription. Replaacing  thymine with Uracil"""
    return seq.replace("T","U")

Seq = ("GATGGAACTTGACTACGTAAATT")

print(transcription(Seq)) 