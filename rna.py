# Replacing T in Coding Strand with U
def usub(b):
    rna = b.replace('T','U')
    return rna


if __name__ == '__main__':
    bases = open('datasets/rosalind_rna.txt').read()
    print(usub(bases))