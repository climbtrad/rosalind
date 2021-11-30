DNA_CODON_TABLE = {
    'TTT': 'F',     'CTT': 'L',     'ATT': 'I',     'GTT': 'V',
    'TTC': 'F',     'CTC': 'L',     'ATC': 'I',     'GTC': 'V',
    'TTA': 'L',     'CTA': 'L',     'ATA': 'I',     'GTA': 'V',
    'TTG': 'L',     'CTG': 'L',     'ATG': 'M',     'GTG': 'V',
    'TCT': 'S',     'CCT': 'P',     'ACT': 'T',     'GCT': 'A',
    'TCC': 'S',     'CCC': 'P',     'ACC': 'T',     'GCC': 'A',
    'TCA': 'S',     'CCA': 'P',     'ACA': 'T',     'GCA': 'A',
    'TCG': 'S',     'CCG': 'P',     'ACG': 'T',     'GCG': 'A',
    'TAT': 'Y',     'CAT': 'H',     'AAT': 'N',     'GAT': 'D',
    'TAC': 'Y',     'CAC': 'H',     'AAC': 'N',     'GAC': 'D',
    'TAA': 'Stop',  'CAA': 'Q',     'AAA': 'K',     'GAA': 'E',
    'TAG': 'Stop',  'CAG': 'Q',     'AAG': 'K',     'GAG': 'E',
    'TGT': 'C',     'CGT': 'R',     'AGT': 'S',     'GGT': 'G',
    'TGC': 'C',     'CGC': 'R',     'AGC': 'S',     'GGC': 'G',
    'TGA': 'Stop',  'CGA': 'R',     'AGA': 'R',     'GGA': 'G',
    'TGG': 'W',     'CGG': 'R',     'AGG': 'R',     'GGG': 'G'
}


# Find all open reading frames
def orf(bases):
    results = []
    start_here = []

    # For three diff reading frames find all positions
    # where there is a start codon i.e. Met
    for i in range(len(bases)):
        aa = translate(bases[i:i+3])

        if aa == 'M':
            start_here.append(i)

    # For each position with a start codon, translate until
    # you reach a Stop
    for i in start_here:
        prot = ""
        has_stop = False

        for j in range(i, len(bases), 3):
            aa = translate(bases[j:j+3])

            if aa == 'Stop':                # Ensures that orf has both a Start and Stop codon
                has_stop = True
                break
            else:
                prot+=aa

        if has_stop == True:
            results.append(prot)

    return results


# Find reverse complement of a string
def revc(str):
    cbase = {'A': 'T', 'C': 'G', 'G': 'C', 'T': 'A'}
    cstr = "".join(cbase.get(i, i) for i in str)
    result = cstr[::-1]
    return result


# Translate dna codon into amino acid
def translate(codon):
    amino_acid = ""
    if len(codon) == 3:
        amino_acid = DNA_CODON_TABLE[codon]
    return amino_acid


# Combine for and rev orfs and remove duplicates
def clean(f, r):
    return(set(f + r))


if __name__ == '__main__':
    data = open('datasets/rosalind_orf.txt').read()
    parts = data.strip().split()
    bases = ''.join(parts[1:])
    revc_bases = revc(bases)

    # Find open reading frames
    for_orfs = (orf(bases))
    rev_orfs = (orf(revc_bases))

    # Clean + print
    print("\n".join(clean(for_orfs, rev_orfs)))
