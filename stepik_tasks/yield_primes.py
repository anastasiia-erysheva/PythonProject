def primes(left, right):

  for n in range(left, right + 1):
    if n <= 1:
      continue

    is_prime = True
    i = 2
    while i * i <= n:
      if n % i == 0:
        is_prime = False
        break
      i += 1

    if is_prime:
      yield n
generator = primes(1, 15)

print(*generator)