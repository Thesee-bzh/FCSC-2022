#!/usr/bin/python3

from pwn import *
import os

target = remote('challenges.france-cybersecurity-challenge.fr', 2001)

MAX = pow(256, 8)
m = MAX // 2

N = 64
M = 16


def dichotomy():
    (a, b) = (0, MAX - 1)
    
    while b - a > 1:
        m = (a + b) // 2
        #print(a, b, m)
        target.send(str(m).encode() + b'\n')
        data = target.recvline().strip()[4::]
        #print(data)

        if data == b'-1':
            b = m
        elif data == b'+1':
            a = m
        else:
            data = target.recvline().strip()
            print(data)
            return 1
    return 0

success = 0
try:
        for i in range(M):
                res = dichotomy()
                success += res
        if success == M:
                data = target.recvline().strip()
                print(data)
except:
	pass

# FCSC{7b20416c4f019ea4486e1e5c13d2d1667eebac732268b46268a9b64035ab294d}
