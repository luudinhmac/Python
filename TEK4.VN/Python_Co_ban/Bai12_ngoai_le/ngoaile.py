class MyErr(Exception):
    def __init__(self, diem_so, thong_bao="Nhập số điểm sai"):
        self.diem_so = diem_so
        self.thong_bao = thong_bao
        super().__init__(self.thong_bao)

diem_so = int(input("Nhập điểm cho sinh viên: "))
if diem_so < 0:
    raise MyErr(diem_so)