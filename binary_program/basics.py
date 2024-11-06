x = 12
y = 10
#conversion to binary. type is str.
x_b = bin(x) #<class 'str'>
y_b = bin(y) #<class 'str'>
print('x = ', x_b, ' ,y = ',y_b)
print(f'type: x ={type(x_b)}, y ={type(y_b)}')

#binary operator 
print('x and y =', bin(x & y))
print('x or y = ', bin(x | y))
print('x xor y = ', bin(x ^ y))

# not
print('~x', ~x, bin(~x))
print('x+ (~x) = ', x + (~x))
print('x+ (~x + 1) = ', x + (~x+1))

# minus 
print('-x', -x, bin(-x))
print('x+ (-x) = ', x + (-x))

print('~x+1 == -x: ', ~x+1 == -x)
print('-x is 2 complement representation.', bin(-x & 0xFFF))

# - bin(x)
print(format(~x, '08b'))
#２complement
print(format(~x & 0xFF, '08b'))
print(~x & 0xFF & x)

# bit shift
x = 9
print(x, ' bin:', bin(x))

print('left bit shift:' , x << 1)
print('right bit shift:', x >> 1)

x = -9

print('x bin: ', bin(x))
print('2 complement x:', bin(x & 0xFF))

print(x << 1)
print(bin(x << 1))
print(bin((x << 1) & 0xFF))
print(x >> 1)
print(bin(x >> 1))
print('2 complement x >> 1', bin((x >> 1) & 0xFF))