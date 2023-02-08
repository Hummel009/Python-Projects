

def launch():
    n = int(input())
    arr = []
    
    for i in range(n):
        arr.append(int(input()))
        if arr[i] < 0:
            arr[i] = abs(arr[i])
        
    for i in range(n - 1):
        if (arr[i] != 0):
            while True:
                if arr[i] < arr[i + 1]:
                    arr[i + 1] = arr[i + 1] % arr[i]
                else:
                    temp = arr[i];
                    arr[i] = arr[i + 1];
                    arr[i + 1] = temp;
                    
                if  arr[i] == 0:
                    break

    print("GCD is", arr[n - 1])
