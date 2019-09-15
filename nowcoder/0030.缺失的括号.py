# https://www.nowcoder.com/practice/de7d4a4b50f643669f331941afb1e728?tpId=90&tqId=30805&tPage=2&rp=2&ru=%2Fta%2F2018test&qru=%2Fta%2F2018test%2Fquestion-ranking

"""
一个完整的括号字符串定义规则如下:
1、空字符串是完整的。
2、如果s是完整的字符串，那么(s)也是完整的。
3、如果s和t是完整的字符串，将它们连接起来形成的st也是完整的。
例如，"(()())", ""和"(())()"是完整的括号字符串，"())(", "()(" 和 ")"是不完整的括号字符串。
牛牛有一个括号字符串s,现在需要在其中任意位置尽量少地添加括号,将其转化为一个完整的括号字符串。请问牛牛至少需要添加多少个括号。

输入描述:
输入包括一行,一个括号序列s,序列长度length(1 ≤ length ≤ 50).
s中每个字符都是左括号或者右括号,即'('或者')'.

输出描述:
输出一个整数,表示最少需要添加的括号数
eg:
输入:(()(()
输出:2
"""

s = list(input().strip())
# print(s) #确认输入数据的正确与否
left_bracket = []  # 记录左括号
tmp = 0  # 记录落单的右括号

for i in s:
    if i == "(":
        left_bracket.append(i)    #发现左括号就放到列表里去
    else:
        if len(left_bracket) > 0:   #如果发现右括号，那么前面一定需要一个相对应的左括号
            left_bracket.remove("(")   #这时如果列表中有一个左括号就拿出来配对
        else:
            tmp += 1                 #如果列表为空，就说明这个右括号落单了，这里需要一个补充

print(tmp+len(left_bracket))   #最后的结果是落单的右括号数量加上落单的左括号数量
