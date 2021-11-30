# Parse .fasta file into a list
def parse_fasta(fasta):
    results = []
    strings = fasta.strip().split('>')

    for i in strings:
        if len(i):
            parts = i.split()
            id = parts[0]
            bases = ''.join(parts[1:])
            results.append((id, bases))

    return results


def overlap_graph(data, k):
    result = []
    for id1, bases1 in data:
        for id2, bases2 in data:
            if id1 != id2 and bases1.endswith(bases2[:k]):  # Retrieve seqs that overlap. i.e.
                result.append((id1, id2))                   # if end of seq one matches the
                                                            # start of seq two
    return result


if __name__ == '__main__':
    fasta = open('datasets/rosalind_grph.txt').read()
    data = parse_fasta(fasta)
    for node in overlap_graph(data, 3):  # In the graph an edge is a tuple. Print each node in the
        print(node[0], node[1])          # edge in line

