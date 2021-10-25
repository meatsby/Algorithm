# Lv2 멀쩡한 사각형

import math

def solution(w,h):
    answer = w*h - (w+h-math.gcd(w,h))
    return answer