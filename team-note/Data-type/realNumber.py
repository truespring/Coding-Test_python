# 양의 실수
a = 157.93
print(a)  # 157.93

# 음의 실수
a = -1837.2
print(a)  # -1837.2

# 소수부가 0일 때 0을 생략
a = 5.
print(a)  # 5.0

# 정수부가 0일 떼 0을 생략
a = -.7
print(a)  # -0.7

a = 0.3 + 0.6
print(a)  # 0.8999999999999999

if a == 0.9:
    print(True)
else:
    print(False)  # False

a = 0.3 + 0.6
print(round(a, 4))  # 0.9

if round(a, 4) == 0.9:
    print(True)  # True
else:
    print(False)
