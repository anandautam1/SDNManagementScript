import sys;

x = 3.0
y = 5.0

print('x + y = %.3f' % (x + y));

z = 0.0
z = 50.0
print('j - c = %.3f' %(z-24));

print('x * y = %.3f' %(x * y));

print('x ** y = %.3f' %(x**y));

#divide the two numbers
x = 13.0
y = 3.0
res = x/y; 
print('x / y = %.3f' % res);

#divide and floor 
x = -13.0
y = 3.0
print('x // y = %.3f' %(x//y));

#modulo 
x = 13
y = 3
res = x % y; 
print('x %% y = %f' % res);

#left shift 
x = 2
y = 2
res = x << y; 
print('x << y = %f' % res);

x = 11
y = 1
res = x >> y;
print('x >> y = %f' % res);

x = 5
y = 3
res = x & y;
print('x & y = %f' % res);

res = x | y;
print('x | y = %f' % res);

res = x ^ y;
print('x ^ y = %f' % res);

res = ~x
print('~x = %f' % res);

res = x < y
print('x < y = %f' % res);

res = x > y
print('x > y = %f' % res);

x = 3
y = 6
res = x <= y
print('x <= y = %f' % res);

x = 4
y = 3
res = x >= y
print('x >= y = %f' % res);

x = 2
y = 2
res = x == y
print('x == y = %f' % res);

x = 'str'
y = 'stR'
res = x == y
print('x == y = %f' % res);

x = 2
y = 3
res = x != y
print('x != y = ', res);

x = True;
print ('Not x %f', not x);

x = True
y = False
res = x and y
print('x and y = ', res);

x = True
y = False
res = x or y
print('x or y = ', res);


