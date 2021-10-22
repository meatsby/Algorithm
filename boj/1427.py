# 소트인사이드
import sys
input = sys.stdin.readline

print("".join(sorted(input().rstrip(), reverse=True)))
