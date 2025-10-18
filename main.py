letters = 0digits = 0spaces = 0others = 0
line = input()
for char in line:if char.isalpha():letters += 1elif char.isdigit():digits += 1elif char.isspace():spaces += 1else:others += 1
print (f"英文字符: {letters}")print (f"数字: {digits}")print (f"空格: {spaces}")print (f"其他字符: {others}")
