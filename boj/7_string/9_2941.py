s = input()
c = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']
count = 0

for i in c:
    s = s.replace(i, 'C')

print(len(s))
