a = 0
b = 0
c = 0
d = 0
s = input()
for ch in s:
    if ch.isalpha():
        a += 1
    elif ch.isdigit():
        b += 1
    elif ch.isspace():
        c += 1
    else:
        d += 1
print(f"英文字符: {a}")
print(f"数字: {b}")
print(f"空格: {c}")
print(f"其他字符: {d}")
