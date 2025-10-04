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

print(dna_seq)