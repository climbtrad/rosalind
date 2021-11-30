# Print the reverse complement
def revc(b):
    base_complements = {'A': 'T', 'C': 'G', 'G': 'C', 'T': 'A'}

    complementary_strand = "".join(base_complements.get(i, i) for i in b)   # Sub in base complements

    rev = complementary_strand[::-1]


if __name__ == '__main__':
    bases = open('datasests/rosalind_revc.text')
    print(revc(bases))