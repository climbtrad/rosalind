# find the largest common shared motif in the sequences

def parse_fasta(filename):
    f = open(filename)
    sequences = {}
    for line in f:
        if line.startswith('>'):
            name = line[1:].rstrip('\n')
            sequences[name] = ''
        else:
            sequences[name] = sequences[name] + line.rstrip('\n')
    print(list(sequences.values()))
    return list(sequences.values())



def lcs(data):
    substr = ''
    if len(data) > 1 and len(data[0]) > 0:

        for i in range(len(data[0])):

            # Decrease j for each i

            for j in range(len(data[0])-i+1):


                # If greater than previous and found in all other seqs, it is lcs

                if j > len(substr) and all(data[0][i:i+j] in x for x in data):
                    substr = data[0][i:i+j]

    return substr



if __name__ == "__main__":
    data = 'datasets/test.fasta'
    print(lcs(parse_fasta(data)))









