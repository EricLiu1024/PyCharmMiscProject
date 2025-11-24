catalog = "CS101|MATH200|HIST150|PHYS120"
request = "MATH-200, CS-101, PHYS-100, ENGL-110"
course_c = catalog.split('|')
print(set(course_c))
translate_table = str.maketrans('','',',-')
request = request.translate(translate_table)
course_r = request.split(' ')
print(set(course_r))
enrolled = tuple(set(course_r) & set(course_c))
print(enrolled)
not_found = tuple(set(course_r) - set(course_c))
print(not_found)
enrolled_str = ','.join(enrolled)
not_found_str = ','.join(not_found)
print(f'nrolled: <{enrolled_str}> | Not found: <{not_found_str}>')



