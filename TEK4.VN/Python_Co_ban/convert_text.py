# def convert_text(num):

#     text_num =['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight','nine']
#     L= []
#     for i in range(len(text_num)):
#         for j in str(num):
#             if j== str(i):
#                 L.append(text_num[i])

#     return ' '.join(L)
# n = int(input())
# print(convert_text(n))
def convert_text(num):
    text_num = ['zero', 'one', 'two', 'three', 'four',
                'five', 'six', 'seven', 'eight', 'nine']
    L = []
    for j in str(num):
            L.append(text_num[int(j)])
    return ' '.join(L)
n = int(input())
print(convert_text(n))
