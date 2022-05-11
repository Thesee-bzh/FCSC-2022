# Misc / Guessme

## Challenge :star:
> Devine le secret !

    nc challenges.france-cybersecurity-challenge.fr 2001

    Note : Soyez rapides, la connexion est coupée au bout de cinq minutes.

## Inputs
- server at `challenges.france-cybersecurity-challenge.fr:2001`
- server code [guessme.py](./guessme.py)

## Solution
When interacting with the server on port 2001, we can submit numbers and get `+1` or `-1` in response.
So we have to find a secret using a dichotomy approach.
Also, we need to do this multiple times (`M=16` from the available server code).

We'll use `pwntools` to interact with the server, send/receive data.

I defined a function `dichotomy()` returning whether or not we found the secret. And we call it in a loop, until `M=16` different secrets are found.
```python
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
```

Here is the output of the execution, showing the flag returned by the server after `M=16` successful guesses.
```console
$ python3 sol.py
[+] Opening connection to challenges.france-cybersecurity-challenge.fr on port 2001: Done
b'1 found, 15 more to go'
b'2 found, 14 more to go'
b'3 found, 13 more to go'
b'4 found, 12 more to go'
b'5 found, 11 more to go'
b'6 found, 10 more to go'
b'7 found, 9 more to go'
b'8 found, 8 more to go'
b'9 found, 7 more to go'
b'10 found, 6 more to go'
b'11 found, 5 more to go'
b'12 found, 4 more to go'
b'13 found, 3 more to go'
b'14 found, 2 more to go'
b'15 found, 1 more to go'
b'16 found, 0 more to go'
b'FCSC{7b20416c4f019ea4486e1e5c13d2d1667eebac732268b46268a9b64035ab294d}'
[*] Closed connection to challenges.france-cybersecurity-challenge.fr port 2001
```

## Python code
Complete solution in [sol.py](sol.py)

## Flag
FCSC{7b20416c4f019ea4486e1e5c13d2d1667eebac732268b46268a9b64035ab294d}
