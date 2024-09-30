from lasotuvi.AmDuong import (canChiNgay, diaChi, ngayThangNam, ngayThangNamCanChi, namXemhan,
                     nguHanh, nguHanhNapAm, thienCan, timCuc, sinhKhac)
import time
from lasotuvi.Lich_HND import jdFromDate, L2S


class lapThienBan(object):
    def __init__(self, nn, tt, nnnn, gioSinh, gioiTinh, ten, diaBan, nnxh,
                 duongLich, timeZone=7):
        super(lapThienBan, self).__init__()
        self.gioiTinh = 1 if gioiTinh == 1 else -1
        self.namNu = "Nam" if gioiTinh == 1 else "Nữ"

        chiGioSinh = diaChi[gioSinh]
        canGioSinh = ((jdFromDate(nn, tt, nnnn) - 1) * 2 % 10 + gioSinh) % 10
        if canGioSinh == 0:
            canGioSinh = 10
        self.chiGioSinh = chiGioSinh
        self.canGioSinh = canGioSinh
        self.gioSinh = "{} {}".format(thienCan[canGioSinh]['tenCan'],
                                      chiGioSinh['tenChi'])

        self.timeZone = timeZone
        self.today = time.strftime("%d/%m/%Y")
        # self.ngayDuong, self.thangDuong, self.namDuong = \
        #     nn, tt, nnnn
        self.ten = ten
        if duongLich is True:
            self.ngayDuong, self.thangDuong, self.namDuong = nn, tt, nnnn
            self.ngayAm, self.thangAm, self.namAm, self.thangNhuan = ngayThangNam(nn,tt,nnnn,True, self.timeZone)
            
        else:
            self.ngayAm, self.thangAm, self.namAm = nn, tt, nnnn
            self.ngayDuong, self.thangDuong, self.namDuong = L2S(nn, tt, nnnn, 0,tZ=7)


        self.canThang, self.canNam, self.chiNam = \
            ngayThangNamCanChi(self.ngayAm, self.thangAm,
                               self.namAm, False, self.timeZone)
        self.chiThang = self.thangAm
        self.canThangTen = thienCan[self.canThang]['tenCan']
        self.canNamTen = thienCan[self.canNam]['tenCan']
        self.chiThangTen = diaChi[self.thangAm]['tenChi']
        self.chiNamTen = diaChi[self.chiNam]['tenChi']

        self.canNgay, self.chiNgay = canChiNgay(
            self.ngayDuong, self.thangDuong, self.namDuong,
            duongLich, timeZone)
        self.canNgayTen = thienCan[self.canNgay]['tenCan']
        self.chiNgayTen = diaChi[self.chiNgay]['tenChi']

        self.namXemHan = nnxh
        self.canNamXH, self.chiNamXH = namXemhan(self.namXemHan)
        self.canNamXHTen = thienCan[self.canNamXH]['tenCan']
        self.chiNamXHTen = diaChi[self.chiNamXH]['tenChi']

        cungAmDuong = 1 if (diaBan.cungMenh % 2 == 1) else -1
        self.amDuongNamSinh = "Dương" if (self.chiNam % 2 == 1) else "Âm"
        if (cungAmDuong * self.gioiTinh == 1):
            self.amDuongMenh = "Âm dương thuận lý"
        else:
            self.amDuongMenh = "Âm dương nghịch lý"

        cuc = timCuc(diaBan.cungMenh, self.canNam)
        self.hanhCuc = nguHanh(cuc)['id']
        self.tenCuc = nguHanh(cuc)['tenCuc']
        self.tenHanh = nguHanh(cuc)['tenHanh']

        self.menhChu = diaChi[self.canNam]['menhChu']
        self.thanChu = diaChi[self.canNam]['thanChu']

        self.menh = nguHanhNapAm(self.chiNam, self.canNam)
        menhId = nguHanh(self.menh)['id']
        menhCuc = sinhKhac(menhId, self.hanhCuc)
        if menhCuc == 1:
            self.sinhKhac = "Bản Mệnh sinh Cục"
        elif menhCuc == -1:
            self.sinhKhac = "Bản Mệnh khắc Cục"
        elif menhCuc == -1j:
            self.sinhKhac = "Cục khắc Bản Mệnh"
        elif menhCuc == 1j:
            self.sinhKhac = "Cục sinh Bản mệnh"
        else:
            self.sinhKhac = "Cục hòa Bản Mệnh"

        self.banMenh = nguHanhNapAm(self.chiNam, self.canNam, True)


