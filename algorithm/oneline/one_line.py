#!/usr/bin/env python
# -*- coding=utf-8 -*-

"""
 @author 
 @create 2017-03-17 下午2:09
"""

print'\n'.join(
    [''.join(
        ['*' if abs((lambda a: lambda z, c, n: a(a, z, c, n))(lambda s, z, c, n: z if n == 0else s(s, z * z + c, c, n - 1))(0, 0.02 * x + 0.05j * y, 40)) < 2 else' 'for x in range(-80, 20)]) for y in range(-20, 20)])

print'\n'.join([''.join([('AndyLove'[(x - y) % 8] if ((x * 0.05) ** 2 + (y * 0.1) ** 2 - 1) ** 3 - (x * 0.05) ** 2 * (y * 0.1) ** 3 <= 0 else' ') for x in range(-30, 30)]) for y in range(15, -15, -1)])

print '\n'.join([' '.join(['%s*%s=%-2s' % (y, x, x * y) for y in range(1, x + 1)]) for x in range(1, 10)])

print [x[0] for x in [(a[i][0], a.append((a[i][1], a[i][0] + a[i][1]))) for a in ([[1, 1]],) for i in xrange(100)]]

print (lambda rnd: rnd.choice([1, 2, 3, 10]))(__import__('random'))
