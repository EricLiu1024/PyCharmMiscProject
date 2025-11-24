dna_seq = 'ATCGACGTgctaaattggccAGCTTGCAGagccctt'
dna_seq_u = dna_seq.upper()
cg_ratio = (dna_seq_u.count('G')+dna_seq_u.count('C')) / len(dna_seq_u)
print(dna_seq.upper())
print(str(cg_ratio * 100) + '%')
print(dna_seq_u[::-1])
print(dna_seq_u[-10:-4:])
i = 0
for base in dna_seq_u:
    if i % 3 == 0 and i != 0:
        print(' ',end = '')
    print(base,end = '')
    i+=1
print('\nATC GAC GTg cta aat tgg ccA GCT TGC AGa gcc ctt')
print('\n' + dna_seq_u)
