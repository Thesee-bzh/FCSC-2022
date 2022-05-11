import random

flag = list(open("output.txt", "rb").read().strip())

def shuffle(ls, seed):
  # Shuffle the list ls using the seed `seed`
  random.seed(seed)
  random.shuffle(ls)
  return ls

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

# FCSC{d93d32485aec7dc7622f13cd93b922363911c36d2ffd4f829f4e3264d0ac6952}
