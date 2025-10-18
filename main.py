# 初始化计数器
letters = 0
digits = 0
spaces = 0
others = 0

# 获取输入并处理空输入情况
line = input("请输入一行字符：")
if not line:
    print("未输入任何字符")
else:
    # 遍历统计
    for char in line:
        if char.isalpha():
            letters += 1
        elif char.isdigit():
            digits += 1
        elif char.isspace():
            spaces += 1
        else:
            others += 1
    # 输出结果
    print(f"英文字符: {letters}")
    print(f"数字: {digits}")
    print(f"空格: {spaces}")
    print(f"其他字符: {others}")
