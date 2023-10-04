def DNA_strand(dna):
    DNA = {'A': 'T',
          'T': 'A',
          'C': 'G',
          'G':'C'}
    new_dna= []
    for i in dna:
        dna2 = DNA.get(i)
        new_dna.append(dna2)
    
    newdna2= ''.join(new_dna)
    print(newdna2)

DNA_strand('TAACGGCGC')