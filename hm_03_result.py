# 1> 定义一个记录最终结果的变量
result = 0
i = 0
while i <= 100:
# 判断变量 i中的数值. 是否是一个偶数
# 偶数 i % 2 ==0
# 奇数 i % 2 !=0
    if i % 2 == 0:
        print(i)
        result += i
    i += 1
print("0-100之间的偶数累加结果= %d" % result)