peptide_a = 'MDDDIAALVVDNGSGMCKAGF'
peptide_b = 'ILTLKYPIEHGIVTNWDDME'
set_a = set(peptide_a)
set_b = set(peptide_b)
print(f'{len(set_a)}   {len(set_b)}')
unique_a = set_a - set_b
unique_b = set_b - set_a
common = set_a & set_b
print(f'{unique_a}\n{unique_b}\n{common}')
similarity = len(common) / len(set_a | set_b) * 100
print(f'{similarity}%')
