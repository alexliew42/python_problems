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

k = 2
c = [0, 0, 1, 0, 0, 1, 1, 0]

def jumpingOnClouds(c, k):
  energy = 100
  i = 0
  while True:
    i += k
    energy -= 1
    if i >= len(c):
      i = i % len(c)
    if c[i] == 1:
      energy -= 2
    if i == 0:
      break
  return(energy)

jumpingOnClouds(c, k)