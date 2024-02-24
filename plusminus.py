import random
import itertools

number = input ("input the number to be ran through the program: ")
zero = "0"

a = number + zero
#351320 lengh = 6 - 1
a = str(a)
length = len(a) - 1

plusminus = "+-"

for op in itertools.product(plusminus, repeat=length):
    operations = "".join(op)

    eqn = ''.join(map(''.join, zip(a, operations)))
    eqn = eqn[0:-1]
    if not eval(eqn):
        print (operations[0:-1])
        break
else:
    print("no solutions")




# suggestion of a cleaner code:
# number = input('number: ')
# import itertools
# n = len(number)
# k = n - 1
# template = [None] * (n+k)
# template[::2] = number
# for ops in itertools.product('+-', repeat=k):
#     template[1::2] = ops
#     if eval(''.join(template)) == 0:
#         print(''.join(template))
#         print(''.join(ops))
#         break
# else:
#     print('no solution')