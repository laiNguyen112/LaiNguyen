import datetime

class SinhVien:
    truong="Dai hoc Da Lat"

    def __init__(self, maSo: int, hoTen: str,ngaySinh: datetime) -> None:
        self.__maSo = maSo
        self.__hoTen=hoTen
        self.__ngaysinh= ngaySinh
    @property
    def maSo(self):
        return self.__maSo
    def hoTen(self):
        return self.__hoTen
    def ngaySinh(self):
        return self.__ngaysinh
    @maSo.setter
    def maSo(self,maso):
        if self.laMaSoHopLe(maso):
            self.__maSo=maso
    @staticmethod
    def laMaSoHopLe(maso:int):
        return len(str(maso))==7
    
    @classmethod
    def doiTenTruong(self,tenmoi):
        self.truong=tenmoi

    def __str__(self)->str:
        return f"{self.__maSo}\t{self.__hoTen}\t{self.__ngaysinh}"
    def xuat(self):
        print(f"{self.__maSo}\t{self.__hoTen}\t{self.__ngaysinh}")
class DanhSachSV:
    def __init__(self )->None:
        self.dssv=[]
    
    def themSV(self,sv:SinhVien):
        self.dssv.append(sv)
    
    def xuat(self):
        for sv in self.dssv:
            print(sv)
    def timSVtheoMSSV(self, mssv:int):
        ds = DanhSachSV()
        for sv in self.dssv :
            if sv.maSo ==mssv:
                ds.themSV(sv)
        return ds
    def timVTSVtheoMSSV(self,mssv:int):
        for i in range(len(self.dssv)):
            if self.dssv[i].maSo==mssv:
                return i
        return -1
    def xoaSVtheoMSSV(self,maSo:int)->bool:
        vt=self.timVTSVtheoMSSV(maSo)
        if vt != -1:
            del self.dssv[vt]
            return True
        else:
            return False
    def timSVtheoTen(self, ten:str):
        ds = DanhSachSV()
        for sv in self.dssv :
           s=str(sv).split(" ")
           if s[2].split('\t')[0]==ten:
                ds.themSV(sv)
        return ds
    
dssv= DanhSachSV()
f=open("dssv.txt","r")
a= True
while(a):
    s=f.readline()
    info=s.split(",")
    date_format="%Y/%m/%d"
    dt=datetime.datetime.strptime(str(info[2]).strip('\n'),date_format)
    sv=SinhVien(int(info[0]),info[1],dt)
    dssv.themSV(sv)
    if not f.readline():
        a=False
f.close()

dssv.xuat()

#print(dssv.timSVtheoMSSV(int(211123)).xuat())

#print(dssv.timVTSVtheoMSSV(int(211123)))
print(dssv.timSVtheoTen('A').xuat())
#print(dssv.xoaSVtheoMSSV(int(210023)))

#print(dssv.xoaSVtheoMSSV(int(211023)))