#
#
# Even Fibonacci numbers
#
#
#
sum = 0
arr = [1, 2]

for i in arr:
    if(i % 2 == 0):
        sum += i


for i in range(2, 400000):
    arr.append(i)
    arr[i] = arr[i-1] + arr[i-2]

    if(arr[i] % 2 == 0):
        if arr[i] > 4000000:
            break
        sum += arr[i]

print(sum)
