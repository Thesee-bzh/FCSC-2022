# Crypto / Shuffled

## Challenge :star:
Oops, nous avons mélangé les caractères du flag. Pourrez-vous les remettre dans l'ordre ?

## Inputs
- A shuffled output [output.txt](./output.txt)
- The python code that shuffled the flag [shuffled.py](./shuffled.py)

## Solution
What immeditely sticks out is the very limited seed range:
```python
random.seed(random.randint(0, 256))
```

Let's bruteforce it and Google for a unshuffle method, like in here: https://crypto.stackexchange.com/questions/78309/how-to-get-the-original-list-back-given-a-shuffled-list-and-seed

```python
def unshuffle(shuffled_ls, seed):
  n = len(shuffled_ls)
  # Perm is [1, 2, ..., n]
  perm = [i for i in range(1, n + 1)]
  # Apply sigma to perm
  shuffled_perm = shuffle(perm, seed)
  # Zip and unshuffle
  ls = list(zip(shuffled_ls, shuffled_perm))
  ls.sort(key=lambda x: x[1])
  return [a for (a, b) in ls]

for seed in range (0, 256):
    unshuffled = unshuffle(flag, seed)
    #print(seed, unshuffled)
    out = bytes(unshuffled).decode()
    if 'FCSC{' in out:
        print(out)
        break
```

## Python code
Complete solution in [sol.py](sol.py)

## Flag
FCSC{d93d32485aec7dc7622f13cd93b922363911c36d2ffd4f829f4e3264d0ac6952}
