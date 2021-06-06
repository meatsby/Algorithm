nums = []
rems = []

for i in range(10):
    nums.append(int(input())%42)

for i in nums:
    if i not in rems:
        rems.append(i)

print(len(rems))
