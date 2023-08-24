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

# c = [0, 0, 0, 1, 0, 0]
# def jumpingOnClouds(c):
#   i = 0
#   total = 0
#   while i < len(c) - 1 :
#     print(i)
#     if i == len(c) - 2:
#       total += 1
#       i += 1
#     elif c[i + 2] == 0:
#       total += 1
#       i += 2
#     else:
#       i += 1
#       total += 1
    
#   print(total)
  

# jumpingOnClouds(c)

# arr = [1, 4, 4, 4, 5, 3, 2, 2, 2]

# def migratoryBirds(arr):
#     bird_dict = {}
#     for number in arr:
#       if number in bird_dict:
#         bird_dict[number] += 1    
#       else:
#         bird_dict[number] = 1
    
#     maxValue = max(bird_dict.values())
    
#     maxKeys = [key for key in bird_dict.keys() if bird_dict[key] == maxValue]

#     return (min(maxKeys))
      

# migratoryBirds(arr)

# bubble sort

# arr = [39, 12, 18, 85, 72, 10, 2, 18]

# def bubble_sort(arr):
#   while True:
#     swapped = False
#     for index in range(len(arr) - 1):
#       if arr[index] > arr[index + 1]:
#         swapped = True
#         arr[index], arr[index + 1] = arr[index + 1], arr[index]
#     if swapped == False:
#       print(arr)    #or return
#       break

# bubble_sort(arr)

# numRows=5
# finalNums=[]
# finalNums.append([1])
# for i in range(numRows-1):
#     # for number in 4 => 1, 2, 3, 4
#     newRow=[1]
#     for j in range(i):
#         #for number in 1, 2, 3, 4 => 1, 1, 2 , 1, 2, 3, 1, 2, 3, 4
#           newRow.append(finalNums[i][j]+finalNums[i][j+1])
#           #
#     newRow.append(1)
#     finalNums.append(newRow)
# print(finalNums)
  

# for j in range(5):
#   print(j)

# num_rows = 5
# 0[1]0
# 0[1, 1]0
# 0[1, 2, 1]0
# 0[1, 3, 3, 1]0
# 0[1, 4, 6, 4, 1]0

num_rows = 5
triangle = [[1]]
for i in range(num_rows - 1):
    place_holder = [0] + triangle[-1] + [0]
    row = []
    for j in range(len(triangle[-1]) + 1):
      row.append(place_holder[j] + place_holder[j + 1])
    triangle.append(row)

print(triangle)

