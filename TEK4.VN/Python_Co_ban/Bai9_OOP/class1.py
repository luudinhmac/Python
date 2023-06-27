class class_name:
    "this is docstring is first string in class"
    
    pass
print(class_name.__doc__)
class SinhVien:
    "Đây là docstring của lớp sv"
    def in_thong_tin(self):
        print("Sinh Vien")

a = SinhVien()
b = SinhVien()
a.in_thong_tin()