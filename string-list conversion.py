strings = list(str(input()))
strings_new = list(dict.fromkeys(strings))
print(sorted(strings_new))
