# Parse fasta as list of seqs
def parse_fasta(f):
    f = re.sub('\s+', '', f)
    matches = re.findall('>Rosalind_[0-9]{1,}[ACGT]+', f)
    seqs = []

    for i in matches:
        seq_id = re.findall('Rosalind_[0-9]{1,}', i)[0]
        dna = re.findall('[ACGT]+', i)[0]

        seqs.append(dna)

    return seqs

# Find maximum overlap and combine at overlap
def find_max_overlap(a, b):
    max = 0
    overlap = ""

    for i in range(min(len(a), len(b))):

        if a.endswith(b[:i]) and max < i:    # Does suffix of a match prefix of b
                max = i
                overlap = a + b[i:]

        elif b.endswith(a[:i]) and max < i:  # Does suffix of b match prefix of a
                max = i
                overlap = b + a[i:]

    return max, overlap                      # Return max overlap value and a string that
                                             # combines a and b about the overlapping bases


def assemble(reads):
    max = 0
    result = ""

    while len(reads) > 1:

        r1 = reads[0]                        # Compare one read against others in list
        for r2 in reads:

            x, overlap = find_max_overlap(r1, r2)

            if max < x:
                max = x
                result = overlap
                a = r1
                b = r2

        if max != 0:
            reads.remove(a)
            reads.remove(b)
            reads.append(result)
            max = 0                         # Reset to max overlap to zero

    return reads

if __name__ == '__main__':
    import re
    fasta = open('datasets/test.fasta').read()
    print((assemble(parse_fasta(fasta))).pop(0))
