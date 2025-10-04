file = "dna_raw.txt"
dna_seq = {}
key = []

with open(file) as f:
    for line in f:
        line = line.strip()
        if line.startswith(">"):
            key = line[1:]
            dna_seq[key] = []
        else:
            dna_seq[key].append(line)

counts={}

for seq, lines in dna_seq.items():
    count={}
    for line in lines:
        for char in line:
            if char in count:
                count[char] +=1
            else:
                count[char]=1
    counts[seq] = count
print(counts)