# set the name of input DNA sequence file
seq = 'c:/home/codebind/Desktop/Scripts/nad4L.txt'
# open the input file 
infile = open(seq,'r')
dna_sequence = infile.read().rstrip()
seq_len = len(dna_sequence)
freqA = dna_sequence.count('A')/seq_len
freqG = dna_sequence.count('G')/seq_len
freqT = dna_sequence.count('T')/seq_len
freqC = dna_sequence.count('C')/seq_len
GCcontent = freqG + freqC
check = freqA + freqG + freqT + freqC
print("This is to check the correctness of sum of all GATC", str(check))
infile.close()
outfile = open('STDOUT', 'w')
outfile.write('sequence lenght:'+ str(seq_len) + 'nt'+ "\n"
'Freq of A:' + str(freqA) + "\n"
'Freq of C:' + str(freqC) + "\n"
'Freq of G:' + str(freqG) + "\n"
'Freq of T:' + str(freqT) + "\n"
"G+C content:" + str(GCcontent)
)
outfile.close()
