# My code
def DNA_strand(dna):
    complemento = {'A': 'T', 'T': 'A', 'C': 'G', 'G': 'C'}
    fita = []
    for base in dna:
        if base in complemento:
            fita.append(complemento[base])
    return ''.join(fita)


#Best Way to do
def DNA_strand(dna):
    print (dna.translate(str.maketrans("ATCG","TAGC")))
DNA_strand('ATTCG')