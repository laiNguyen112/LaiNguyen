class PhanSo:
    def __init__(self, tu=1, mau= 1) : 
        if mau == 0 : 
            raise ValueError (" mẫu phải khác 0")
        self.tu = tu 
        self.mau = mau

    def UCLN(self, a ,b):
        while b:
            a, b=b, a%b
        return a

    
    def __str__(self) -> str:
        return f"{self.tu}/{self.mau}"

    def RutGon(self):
        rg = self.UCLN(self.tu, self.mau)
        self.tu //= rg
        self.mau //= rg

    def __add__(self, other):
        tuMoi = self.tu * other.mau + other.tu * self.mau
        mauMoi = self.mau * other.mau
        result = PhanSo(tuMoi, mauMoi)
        result.RutGon()
        return result

    def __sub__(self, other):
        tuMoi = self.tu * other.mau - other.tu * self.mau
        mauMoi = self.mau * other.mau
        result = PhanSo(tuMoi, mauMoi)
        result.RutGon()
        return result

    def __mul__(self,other):
        tuMoi = self.tu * other.tu 
        mauMoi = self.mau * other.mau
        result = PhanSo(tuMoi, mauMoi)
        result.RutGon()
        return result
    
    def __truediv__(self,other):
        tuMoi = self.tu * other.mau 
        mauMoi = self.mau * other.tu
        result = PhanSo(tuMoi, mauMoi)
        result.RutGon()
        return result



    
