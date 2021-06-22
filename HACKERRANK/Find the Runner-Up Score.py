n = int(input())
arr = list(map(int, input().split()))
print(max([x for x in arr if max(arr) != x]))