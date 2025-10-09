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
        #figured out there is a sort of 1 liner to this, when asking LLMs, where you just select a set assortment of letters.
        #might be worth doing if you want to sort out certain identifiers.
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

#func that kinda in restrospect only works if you run the code thru the previous functions...
def draw_Plot(dna_count):
    ## CODE FROM AI TO FIGURE OUT HOW TO DRAW THEM INTO SUBPLOTS SO IT DOESNT OPEN 10 DIFFERENT WINDOWS
    #aswell as making sure it actually keeps within a set state, 5 collumns, no cap on rows tho

    total_plots = sum(len(lines) for lines in dna_count.values())
    cols = 5
    rows = total_plots // cols + (1 if total_plots % cols != 0 else 0)

    fig, axs = plt.subplots(rows, cols, figsize=(4*cols, 4*rows))
    axs = axs.flatten()  # flatten array in case rows > 1

    idx= 0
    #grab the entire dict so far
    for seq, lineCount in dna_count.items():
        #grab the values in the dict(wich is also a dict), and place the keys in a list and the values of said dict into another list.
        for i, count in enumerate(lineCount):
            #letters = list(count.keys()) #not needed but would make it more readable by defining it
            #values = list(count.values()) # by placing values and letters into the ax.bar, instead of just ".keys, .values"

            #fig = plt.figure()
            ax = axs[idx]

            ax.bar(count.keys(),count.values())
            #Got help from an LLM to figure out what kinda of args it could take when tinkering with design, i kinda dont enjoy design....
            ax.set_yticks(range(0, max(count.values()) + 1))
            ax.set(
                xlabel="Letters",
                ylabel="Amount",
                title=f"dna_seq for {seq} (line {i+1})")
            idx +=1
    plt.tight_layout()
    plt.show()
    input("press ENTER to exit")

# MAIN

file1 = "dna_raw.txt"
dna1 = Read_File(file1)
dna1_count= Letter_count(dna1)
draw_Plot(dna1_count)

#input("\nPress ENTER to show dna seq 2...\n")

file2 = "dna_raw_complicated.txt"
dna2 = Read_File(file2)
dna2_count = Letter_count(dna2)
dna2_plot = draw_Plot(dna2_count)
print(dna2_plot)
