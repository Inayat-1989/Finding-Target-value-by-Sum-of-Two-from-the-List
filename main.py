list = list(map(int,input("Enter a list of values:").split()))
target = int(input("Enter a single target value that you want to find:"))
seen = {}

print(list, target)
for i, num in enumerate(list):
    complement =  target - num
    if complement in seen:
        print([seen[complement], i])
    seen[num] = i