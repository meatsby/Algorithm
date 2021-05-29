n = int(input())
scores = list(map(int, input().split()))
new_s = []

for i in scores:
  new_s.append(i/max(scores)*100)

print(sum(new_s)/len(new_s))
