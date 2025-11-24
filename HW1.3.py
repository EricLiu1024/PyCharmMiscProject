data = str(input())
a,b = data.split(',')
print(a + b[::-1] + a)