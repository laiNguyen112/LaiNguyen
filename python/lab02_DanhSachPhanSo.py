from fractions import Fraction
import Lab02_Phanso

class DanhSachPhanSo:
    def __init__(self):
        self.danhSach = []

    def them(self, tu_so, mau_so):
        phanSo = Fraction(tu_so, mau_so)
        self.danhSach.append(phanSo)

    def hien_thi(self):
        for phanSo in self.danhSach:
            print(f"{phanSo.numerator}/{phanSo.denominator}")

    def nhap(self):
        soLuong = int(input("Nhập số lượng phân số: "))
        for i in range(soLuong):
            tuSo = int(input(f"Nhập tử số cho phân số {i + 1}: "))
            mauSo = int(input(f"Nhập mẫu số cho phân số {i + 1}: "))
            self.them(tuSo, mauSo)


dsPhanSo = DanhSachPhanSo()
dsPhanSo.nhap()

print("\nDanh sách phân số:")
dsPhanSo.hien_thi()

