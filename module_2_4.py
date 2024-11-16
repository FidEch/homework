numbers = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
prime = []
not_prime = []
for i in numbers:
  is_prime = True
  if i == 1:
    continue
  for j in range(2, i // 2+1):
    if i % j == 0:
      is_prime = False
  if is_prime == False:
    not_prime.append(i)
  else:
    is_prime = True
    prime.append(i)
print("Число простое: ", prime)
print("Число не является простым: ", not_prime)


