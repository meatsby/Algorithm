n, m, k = 5, 8, 3
data = sorted([2, 4, 5, 4, 6], reverse=True)
result = 0
count = 0

## My Answer
# if data[0] == data[1]:
#     print(data[0]*8)
# else:
#     for i in range(m):
#         if count == 3:
#             result += data[1]
#             count = 0
#             continue
#         result += data[0]
#         count += 1

# Better Answer
count = m//(k+1)*k + m%(k+1)
result = count*data[0] + (m-count)*data[1]

print(result)
