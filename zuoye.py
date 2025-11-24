#s = input()
#cat = s.count('cat')
#hat = s.count('hat')
#if cat == 0 and hat == 0:
#    print('False!')
#elif cat == hat:
#    print('Equal!')
#elif cat > hat:
#    print('We have more cats!')
#else:
#    print('We have more hats!')
list = input().split(',')
 sum = 0
 for i in list:
    if i == 'J' or i == 'Q' or i == 'K':
        sum += 10
    else:
        sum += int(i)
 if sum == 21:
    print('You win!')
elif sum > 21:
    print('You lose!')
elif sum < 21:
    print('Add more cards!')