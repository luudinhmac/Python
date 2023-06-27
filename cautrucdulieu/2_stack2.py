# Bieu thuc hau va stack
# Biểu thức trung tố: các phép toán(toán tử) năm giữa các con số , biến số(toán hạng)
# ex: 2+5 = 7
# 1+2x(4-3) = 1+2x1 = 1 + 2 = 3

# Biểu thức hậu tố: toán tử nằm sau toán hạng
# 2+5 => 25+
# 4-3 => 34-
# 1+2x(4-3) => 1243-x+
# 3x((5-2)x(7+1)-6) => 352-71+x6-x

# Giải bài toán hậu tố sử dụng stack
# giai 352-71+x6-x
# các bước thực hiện 
# Đọc toán hạng và toán tử từ trái sang phải
# nếu gặp toán hạng , lưu vào stack
# nếu gặp toán tử, ta đọc 2 toán hạng (a1,a2) trong stack và lưu kết quả tính vào a1,a2

# Thực hiện
"""
số 3 là toán hạng => lưu vào stack  : [3]
số 5 là toán hạng => lưu vào stack  : [3,5]
số 2 là toán hạng => lưu vào stack  : [3,5,2]
- là toán tử => lấy toán hạng (5,2) trong stack, tính 5-2 =3 lưu vào stack  : [3,3]
7 là toán hạng => lưu vào stack : [3,3,7]
1 là toán hạng => luu vào stack : [3,3,7,1]
+ là toán tử lấy toán hạng (7,1) trong stack, tính 7+1 =8 lưu vào stack : [3,3,8]
x là toán tử lấy toán hạng (3,8) tính 3x8 =24 lưu vào stack : [3,24]
6 là toán hạng lưu vào stack : [3,24,6]
- là toán tử lấy toán hạng (24,6) tính 24-6 =18 lưu vào stack : [3,18]
* là toán tử láy toán hạng(3,18) tính 3*18 lưu vào stack [54]
"""

