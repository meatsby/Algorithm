# 연산자 끼워넣기 (2)
import sys
input = sys.stdin.readline

n = int(input())
nums = list(map(int, input().split()))
oper = list(map(int, input().split()))
mx, mn = -1e9, 1e9

def dfs(idx, ans, add, sub, mul, div):
    global mx, mn
    if idx == n:
        mx = max(mx, ans)
        mn = min(mn, ans)
        return
    if add > 0:
        dfs(idx+1, ans+nums[idx], add-1, sub, mul, div)
    if sub > 0:
        dfs(idx+1, ans-nums[idx], add, sub-1, mul, div)
    if mul > 0:
        dfs(idx+1, ans*nums[idx], add, sub, mul-1, div)
    if div > 0:
        dfs(idx+1, ans//nums[idx] if ans > 0 else -((-ans)//nums[idx]), add, sub, mul, div-1)

dfs(1, nums[0], oper[0], oper[1], oper[2], oper[3])
print(mx)
print(mn)
