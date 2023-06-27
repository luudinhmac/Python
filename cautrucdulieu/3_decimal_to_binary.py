# decimal to binary
# vd : 14 -> binary
# 14:2 =7 dư 0  : 0
# 7:2 = 3 dư 1  : 1
# 3:2 = 1 dư 1  : 1
# 1:2 = 0 dư 1  : 1
# => 1110


def decimal_to_binary_stack(num):
    stack = []
    while num != 0:
        sd = num % 2
        stack.append(sd)
        num = num//2
    print(stack)
    st = ""
    while stack != []:
        st = st + str(stack.pop())
    return st


print(decimal_to_binary_stack(14))

