def roi(dt, cp):
    return (dt - cp)/cp
def quyet_dinh_dau_tu(roi):
    if roi >= 0.75:
        return "Nên đầu tư!"
    else:
        return "Không nên đầu tư!"

print("Chương trình roi")
cp = float(input("Nhập vào chi phí"
))
dt = float(input("Nhập vào doanh thu"))
b =roi(dt,cp)
a = quyet_dinh_dau_tu(b)
print(b)
print(a)

