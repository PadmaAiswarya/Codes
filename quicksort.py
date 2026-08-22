arr = [3, 6, 8, 10, 1, 2, 1]
stack = [(0, len(arr) - 1)]
while stack:
    low, high = stack.pop()
    if low < high:
        pivot = arr[high]
        i = low - 1
        for j in range(low, high):
            if arr[j] <= pivot:
                i += 1
                arr[i], arr[j] = arr[j], arr[i]
        arr[i + 1], arr[high] = arr[high], arr[i + 1]
        p = i + 1        
        stack.append((low, p - 1))
        stack.append((p + 1, high))
print(arr)
