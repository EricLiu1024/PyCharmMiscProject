import os
with open('test','r') as file:
    content = file.read()
encrypted = []
for x in content:
    if 'A' <= x <= 'Z':
        encrypted.append(chr((ord(x) - 65 + 3) % 26 + 65))
    elif 'a' <= x <= 'z':
        encrypted.append(chr((ord(x) - 97 + 3) % 26 + 97))
    else:
        encrypted.append(x)
output_content = ''.join(encrypted)
with open('encrypted_test', 'w') as output_file:
    output_file.write(output_content)
