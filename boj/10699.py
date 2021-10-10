# 오늘 날짜
import sys
from datetime import datetime
input = sys.stdin.readline

now = datetime.now()
print(f"{now.year}-{now.month}-{now.day}")
