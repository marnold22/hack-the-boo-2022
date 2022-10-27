from Crypto.Util.number import bytes_to_long, getPrime
import random

from sympy import public

FLAG = b'HTB{??????????????????????????????????????????????????????????????????????}'

def gen_params():
  p = getPrime(1024)
  g = random.randint(2, p-2)
  x = random.randint(2, p-2)
  h = pow(g, x, p)

  print("p = ", p)
  print("g = ", g)
  print("x = ", x)
  print("h = ", h)

  return (p, g, h, x), x

def encrypt(pubkey):
  p, g, h, x = pubkey
  m = bytes_to_long(FLAG)
  y = random.randint(2, p-2)

  print("y = ", y)

  s = pow(h, y, p)
  print("s = ", s)

  c3 = m * s
  print("c3 = ", c3)
  print("m = ", m)
  return (g * y % p, m * s % p)

# def decrypt():
#   pubkey, privkey = gen_params()
#   c1, c2 = encrypt(pubkey)


def main():
  pubkey, privkey = gen_params()
  c1, c2 = encrypt(pubkey)

  with open('data.txt', 'w') as f:
    f.write(f'p = {pubkey[0]}\ng = {pubkey[1]}\nh = {pubkey[2]}\nx = {pubkey[3]}\n(c1, c2) = ({c1}, {c2})\n')


if __name__ == "__main__":
  main()