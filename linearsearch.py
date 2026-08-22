arr = [3, 6, 8, 10, 1, 2, 1]
target = 8
result = -1
for i in range(len(arr)):
    if arr[i] == target:
        result = i
        break
print(result)
