# Parse fasta into matrix

def parse_fasta(data):
    list = []
    strings = data.strip().split('>')

    for data in strings:
        if len(data) == 0:
            continue

        parts = data.split()
        bases = ''.join(parts[1:])

        list.append(bases)

    matrix = []
    for i in range(len(list)):
        matrix.append([*list[i]])

    return matrix

def profile(matrix):
    profile = []
    for i in range(len(matrix)):
        a, c, t, g = 0
        for j in range(len(matrix)):
            if matrix[j:i] == 'A':
                a += 1
            if matrix[j:i] == 'C':
                c += 1
            if matrix[j:i] == 'T':
                t += 1
            if matrix[j:i] == 'G':
                g += 1
        profile.append(a, c, t, g)
    return profile

def consensus(matrix):
    consensus_seq = ""
    return consensus_seq


if __name__ == '__main__':

    data = open('datasets/test.fasta').read()
    matrix = (parse_fasta(data))
    print(profile(matrix))