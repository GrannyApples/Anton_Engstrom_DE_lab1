file = "dna_raw.txt"
dna_seq = {}
key = []
#reads a file and fills it in a hashset
with open(file) as f:
    for line in f:
        #removes whitespace
        line = line.strip()
        if line.startswith(">"):
            #removes first index of seq(in this case the > .)
            key = line[1:]
            dna_seq[key] = []
        else:
            dna_seq[key].append(line)


#count how many of each letter there are
counts={}

for seq, lines in dna_seq.items():
    count={}
    #loops thru the dict, and then the value of the key and then each char in the value, prob is a one line to do this with an import or something?
    for line in lines:
        line = line.upper()
        for char in line:
            #adds it to the count if it alrdy exists in the dict, else it creates the start of the count
            if char in count:
                count[char] +=1
            else:
                count[char]=1
    counts[seq] = count
print(counts)