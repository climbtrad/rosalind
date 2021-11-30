# Count Number of A, C, T, G in a String
def count(b):
    a = b.count('A')
    c = b.count('C')
    t = b.count('T')
    g = b.count('G')
    print(a, c, t, g)


if __name__ == '__main__':
    bases = open('datasets/rosalind_dna.txt').read()
    count(bases)