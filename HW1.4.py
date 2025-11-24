dict = {'C':12.01,'H':1.01,'O':16.00,'N':14.01,'S':32.07}
num_s = int(input())
weight = dict['C'] * 187 + dict['H'] * 291 + dict['N'] * 45 + dict['O'] * 59 + dict['S'] * num_s
print(f'The molecular weight of the unkown compound is {weight} Da.')