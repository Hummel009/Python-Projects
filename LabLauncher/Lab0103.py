def launch():
    n = int(input())
    arr = []
    for i in range(n):
        arr.append(input())
    
    nums = set()
    
    for i in range(n):
        nums.add(arr[i])
    
    print("Unique elements:", nums)
    print("The quantity of unique elements:", len(nums))
    
    maxx = 0

    for i in range(n):
        for j in range(n):
            if arr[i] == arr[j] and i != j:
                maxx = arr[i]
                break

    for i in range(n):
        for j in range(n):
            if arr[i] == arr[j] and i != j and maxx < arr[i]:
                maxx = arr[i]
    print("Max duplicate:", maxx)