# n = 100


# def findDigits(n):
#     string = str(n)
#     total = 0
#     for number in string:
#       if int(number) == 0:
#         nothing = True
#       elif n % int(number) == 0:
#         total += 1
#     return total

# findDigits(n)

# k = 2
# c = [0, 0, 1, 0, 0, 1, 1, 0]

# def jumpingOnClouds(c, k):
#   energy = 100
#   i = 0
#   while True:
#     i += k
#     energy -= 1
#     if i >= len(c):
#       i = i % len(c)
#     if c[i] == 1:
#       energy -= 2
#     if i == 0:
#       break
#   return(energy)

# jumpingOnClouds(c, k)

c = [0, 0, 0, 1, 0, 0]
def jumpingOnClouds(c):
  i = 0
  total = 0
  while i < len(c) - 1 :
    print(i)
    if i == len(c) - 2:
      total += 1
      i += 1
    elif c[i + 2] == 0:
      total += 1
      i += 2
    else:
      i += 1
      total += 1
    
  print(total)
  

jumpingOnClouds(c)
    