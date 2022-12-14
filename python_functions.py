# Challenge 1

def sum_to(num):
  sum = 0
  for n in range(1, num + 1):
    sum += n
  return sum

print(sum_to(6))

# Challenge 2

def largest(list1):
  max = list1[0]
  for x in list1:
    if x > max:
      max = x
  return max
  
print(largest([1, 2, 3, 4, 0]))
print(largest([10, 4, 2, 231, 91, 54]))

# Challenge 3

def occurrences(str1, str2):
  return str1.count(str2)

print(occurrences('fleep floop', 'fe'))


# Challenge 4

def product(*args):
  num = 1
  for arg in args:
    num *= arg
  return num

print(product(2, 5, 5))