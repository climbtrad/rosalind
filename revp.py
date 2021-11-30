def revp(data):

    # Return bases from a single fasta seq
    parts = data.strip().split()
    bases = ''.join(parts[1:])

    # Find all substr in len 4-13
    results = []
    for i in range(len(bases)):  # iterate through all positions
        for j in range(4, 13):   # iterate through substring length

            # Do not count substrings that are out of range
            if i + j > len(bases):
                continue

            # Find all substr and their reverse complements
            substr1 = bases[i:i+j]
            substr2 = revc(substr1)

            # If equal, they are reverse palindrome. Return start position and length
            if substr1 == substr2:
                results.append((i+1, j))

    return results


def revc(str):
    cbase = {'A': 'T', 'C': 'G', 'G': 'C', 'T': 'A'}
    cstr = "".join(cbase.get(i, i) for i in str)
    result = cstr[::-1]

    return result


if __name__ == '__main__':
    data_file = open('datasets/test.fasta').read()
    results = revp(data_file)
    print("\n".join([' '.join(map(str, r)) for r in results]))
