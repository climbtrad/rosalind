# Create dictionary of sequences and their IDs
def parse_fasta(data):
    result = {}
    strings = data.strip().split('>')

    for data in strings:
        if len(data) == 0:
            continue

        parts = data.split()
        id = parts[0]
        bases = ''.join(parts[1:])

        result[id] = bases

    return result


def compute_ratio(bases):
    return (bases.count('C')+bases.count('G'))/len(bases)*100  # Return ratio as %gc content


if __name__ == '__main__':
    data_file = open('datasets/rosalind_gc.txt').read()
    parsed_fasta = (parse_fasta(data_file))
    highestgc = 0
    highestid = None

    for id, bases in parsed_fasta.items():
        gc = compute_ratio(bases)

        if gc > highestgc:                  # Report greatest gc content
            highestgc = gc
            highestid = id

    print(highestid)
    print(highestgc)








