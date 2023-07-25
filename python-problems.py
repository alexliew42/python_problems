n = 100


def findDigits(n):
    string = str(n)
    total = 0
    for number in string:
      if int(number) == 0:
        nothing = True
      elif n % int(number) == 0:
        total += 1
    return total

findDigits(n)