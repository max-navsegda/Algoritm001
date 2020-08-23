from random import random
N = 128
array = []
for i in range(N):
    array.append(int(random()*100))
array.sort()
print(array)

number = int(input())

low = 0
high = N-1
count = 0

while low <= high:
    count += 1

    mid = (low + high) // 2
    if number < array[mid]:
        high = mid - 1
    elif number > array[mid]:
        low = mid + 1
    else:
        print("ID =", mid + 1, count)
        break
else:
    print("No the number", count)
