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


def seq_list(data):
    # IMPORTANT: Remove '\n' characters from string before creating list
    data = re.sub('\s+', '', data)
    # Each '>...' becomes an item in list
    matches = re.findall('>Rosalind_[0-9]{1,}[ACGT]+', data)
    seqs = []
    # Separate seqs and seq ids, returning seqs only
    for i in matches:
        seq_id = re.findall('Rosalind_[0-9]{1,}', i)[0]
        dna = re.findall('[ACGT]+', i)[0]

        seqs.append(dna)

    return seqs


def splice_introns(strings):
    str = "".join([strings[0]])
    introns = strings[1:]

    for i in range(len(introns)):
        intron = introns.pop(0)
        str = str.replace(intron, '')

    return str


def translate(str):
    protein = ''
    for i in range(0, len(str), 3):
        codon = DNA_CODON_TABLE[str[i:i+3]]
        if codon == 'Stop':
            break
        else:
            protein += codon
    return protein


if __name__ == '__main__':

    import re

    data = open('datasets/rosalind_splc.txt').read()
    print(translate(splice_introns(seq_list(data))))
