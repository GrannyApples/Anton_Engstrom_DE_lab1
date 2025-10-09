import matplotlib.pyplot as plt

def Read_File(file):
    dna_seq = {}
    key = []
    #reads a file and fills it in a hashset by goin over it line by line
    with open(file) as f:
        for line in f:
            #removes whitespace
            line = line.strip()
            if line.startswith(">"):
                #skips first index of seq line(in this case the > .) so the dict key reads seq# instead of >seq#...
                key = line[1:]
                dna_seq[key] = []
            else:
                dna_seq[key].append(line)

    return dna_seq
    

#count how many of each letter there are in each value key pair
def Letter_count(dna_seq):
    counts={}

    for seq, lines in dna_seq.items():
        lineCount = []
        #loops thru the dict, and then the value of the key and then each char in the value, prob is a one line to do this with an import or something?
        for line in lines:
            count={}
            line = line.upper()
            for char in line:
                #adds it to the count if it alrdy exists in the dict, else it creates the start of the count
                if char in count:
                    count[char] +=1
                else:
                    count[char]=1
            lineCount.append(count) #adds a new value to the key if it has multiple lines.
        counts[seq] = lineCount #adds all the line values to the current key.

    return counts

def draw_Plot(dna_count):
    for seq, lineCount in dna_count.items():
        for i, count in enumerate(lineCount):
            letters = list(count.keys())
            values = list(count.values())

            fig = plt.figure()
            ax = plt.axes()

            ax.plot(letters,values)
            plt.show()

# MAIN

file1 = "dna_raw.txt"
dna1 = Read_File(file1)
dna1_count= Letter_count(dna1)
dna1_plot = draw_Plot(dna1_count)
print(dna1_plot)

input("\nPress ENTER to show dna seq 2...\n")

file2 = "dna_raw_complicated.txt"
dna2 = Read_File(file2)
dna2_count = Letter_count(dna2)
dna2_plot = draw_Plot(dna2_count)
print(dna2_plot)
