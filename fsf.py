import os
if not os.path.exists('test') or os.path.getsize('test') == 0:
    print('Error! File not found!')
else:
    print('File found')
    with open('test', 'r') as file:
        lines = file.readlines()
    with open('test', 'r') as file:
        characters = len(file.read())
    with open('output', 'w') as new_file:
        new_file.write(f'Lines in test file: {len(lines)}\n')
        new_file.write(f'Characters in test file: {characters}\n')