# Index the start locations of a motif in a dna seq
def locations(data):
    result_list = []
    s, sub = data.split()
    l = len(sub)

    for i in range(len(s)-l):

        if s[i:i+l] == sub:
            result_list.append(i+1)

    return result_list


if __name__ == "__main__":
    data = open('datasets/rosalind_subs.txt').read()
    locations = locations(data)
    print(' '.join(map(str, locations)))   # Apply str() to convert list of ints to chars
                                           # then converts list to string

