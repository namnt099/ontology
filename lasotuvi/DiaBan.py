from lasotuvi.AmDuong import diaChi, dichCung, khoangCachCung
from lasotuvi.AmDuong import (dichCung, namXemhan, ngayThangNam, ngayThangNamCanChi, nguHanh,
                     nguHanhNapAm, thienCan, timCoThan, timCuc, timHoaLinh, amDuongNamXH,
                     timLuuTru, timPhaToai, timThienKhoi, timThienMa, timLTrangSinh,
                     timThienQuanThienPhuc, timTrangSinh, timTriet, timTuVi, timLLocTon,
                     diaChi)
from lasotuvi.Sao import (saoAnQuang, saoBachHo, saoBacSy, saoBatToa, saoBenh,
                 saoBenhPhu, saoCoThan, saoCuMon, saoDaiHao, saoDaLa,
                 saoDaoHoa, saoDauQuan, saoDeVuong, saoDiaGiai, saoDiaKhong,
                 saoDiaKiep, saoDiaVong, saoDieuKhach, saoDuong, saoDuongPhu,
                 saoGiaiThan, saoHoaCai, saoHoaKhoa, saoHoaKy, saoHoaLoc,
                 saoHoaQuyen, saoHoaTinh, saoHongLoan, saoHuuBat, saoHyThan,
                 saoKiepSat, saoKinhDuong, saoLamQuan, saoLiemTrinh,
                 saoLinhTinh, saoLocTon, saoLongDuc, saoLongTri, saoLucSi,
                 saoLuuHa, saoMo, saoMocDuc, saoNguyetDuc, saoPhaQuan,
                 saoPhaToai, saoPhiLiem, saoPhongCao, saoPhucBinh, saoPhucDuc,
                 saoPhuongCac, saoQuanDoi, saoQuanPhu2, saoQuanPhu3, saoQuaTu,
                 saoQuocAn, saoSuy, saoTamThai, saoTangMon, saoTaPhu,
                 saoTauThu, saoThai, saoThaiAm, saoThaiDuong, saoThaiPhu,
                 saoThaiTue, saoThamLang, saoThanhLong, saoThatSat, saoThienCo,
                 saoThienDong, saoThienDuc, saoThienGiai, saoThienHinh,
                 saoThienHu, saoThienHy, saoThienKhoc, saoThienKhoi,
                 saoThienKhong, saoThienLa, saoThienLuong, saoThienMa,
                 saoThienPhu, saoThienPhuc, saoThienQuan, saoThienQuy,
                 saoThienRieu, saoThienSu, saoThienTai, saoThienTho,
                 saoThienThuong, saoThienTru, saoThienTuong, saoThienViet,
                 saoThienY, saoThieuAm, saoThieuDuong, saoTieuHao,
                 saoTrangSinh, saoTrucPhu, saoTu, saoTuePha, saoTuongQuan,
                 saoTuPhu, saoTuVi, saoTuyet, saoVanKhuc, saoVanTinh,
                 saoVanXuong, saoVuKhuc, saoLBachHo, saoLDaLa, saoLKinhDuong, 
                 saoLLocTon, saoLTangMon, saoLThaiTue, saoLThienHu, 
                 saoLThienKhoc, saoLThienMa, saoLBacSi, saoLThienKhong,
                 saoLQuanSach, saoLThienKhoi, saoLThienViet, saoLTrangSinh,
                 saoLMocDuc, saoLQuanDoi, saoLLamQuan, saoLDeVuong,
                 saoLSuy, saoLBenh, saoLTu, saoLMo,
                 saoLTuyet, saoLThai, saoLDuong)


class cungDiaBan(object):
    """docstring for cungDiaBan"""
    def __init__(self, cungID):
        super(cungDiaBan, self).__init__()
        hanhCung = [None, "Thủy", "Thổ", "Mộc", "Mộc", "Thổ", "Hỏa",
                    "Hỏa", "Thổ", "Kim", "Kim", "Thổ", "Thủy"]
        self.cungSo = cungID
        self.hanhCung = hanhCung[cungID]
        self.cungSao = []
        self.cungAmDuong = -1 if (self.cungSo % 2 == 0) else 1
        self.cungTen = diaChi[self.cungSo]['tenChi']
        self.cungThan = False

    def themSao(self, sao):
        dacTinhSao(self.cungSo, sao)
        self.cungSao.append(sao.__dict__)
        return self

    def cungChu(self, tenCungChu):
        self.cungChu = tenCungChu
        return self

    def daiHan(self, daiHan):
        self.cungDaiHan = daiHan
        return self

    def tieuHan(self, tieuHan):
        self.cungTieuHan = diaChi[tieuHan + 1]['tenChi']
        return self

    def anCungThan(self):
        self.cungThan = True

    def anTuan(self):
        self.tuanTrung = True

    def anTriet(self):
        self.trietLo = True


class diaBan(object):
    def __init__(self, thangSinhAmLich, gioSinhAmLich):
        super(diaBan, self).__init__()
        self.thangSinhAmLich = thangSinhAmLich
        self.gioSinhAmLich = gioSinhAmLich
        self.thapNhiCung = [cungDiaBan(i) for i in range(13)]
        self.nhapCungChu()
        self.nhapCungThan()

    def cungChu(self, thangSinhAmLich, gioSinhAmLich):
        self.cungThan = dichCung(3, thangSinhAmLich - 1, gioSinhAmLich - 1)
        self.cungMenh = dichCung(3, thangSinhAmLich - 1, - (gioSinhAmLich) + 1)
        cungPhuMau = dichCung(self.cungMenh, 1)
        cungPhucDuc = dichCung(self.cungMenh, 2)
        cungDienTrach = dichCung(self.cungMenh, 3)
        cungQuanLoc = dichCung(self.cungMenh, 4)
        self.cungNoboc = dichCung(self.cungMenh, 5)  # Để an sao Thiên thương
        cungThienDi = dichCung(self.cungMenh, 6)
        self.cungTatAch = dichCung(self.cungMenh, 7)  # an sao Thiên sứ
        cungTaiBach = dichCung(self.cungMenh, 8)
        cungTuTuc = dichCung(self.cungMenh, 9)
        cungTheThiep = dichCung(self.cungMenh, 10)
        cungHuynhDe = dichCung(self.cungMenh, 11)

        cungChuThapNhiCung = [
            {
                'cungId': 1,
                'tenCung': "Mệnh",
                'cungSoDiaBan': self.cungMenh
            },
            {
                'cungId': 2,
                'tenCung': "Phụ mẫu",
                'cungSoDiaBan': cungPhuMau

            },
            {
                'cungId': 3,
                'tenCung': "Phúc đức",
                'cungSoDiaBan': cungPhucDuc

            },
            {
                'cungId': 4,
                'tenCung': "Điền trạch",
                'cungSoDiaBan': cungDienTrach

            },
            {
                'cungId': 5,
                'tenCung': "Quan lộc",
                'cungSoDiaBan': cungQuanLoc

            },
            {
                'cungId': 6,
                'tenCung': "Nô bộc",
                'cungSoDiaBan': self.cungNoboc

            },
            {
                'cungId': 7,
                'tenCung': "Thiên di",
                'cungSoDiaBan': cungThienDi

            },
            {
                'cungId': 8,
                'tenCung': "Tật Ách",
                'cungSoDiaBan': self.cungTatAch

            },
            {
                'cungId': 9,
                'tenCung': "Tài Bạch",
                'cungSoDiaBan': cungTaiBach

            },
            {
                'cungId': 10,
                'tenCung': "Tử tức",
                'cungSoDiaBan': cungTuTuc

            },
            {
                'cungId': 11,
                'tenCung': "Phu thê",
                'cungSoDiaBan': cungTheThiep

            },
            {
                'cungId': 12,
                'tenCung': "Huynh đệ",
                'cungSoDiaBan': cungHuynhDe

            }
        ]
        return cungChuThapNhiCung

    def nhapCungChu(self):
        for cung in self.cungChu(self.thangSinhAmLich, self.gioSinhAmLich):
            self.thapNhiCung[cung['cungSoDiaBan']].cungChu(cung['tenCung'])
        return self

    def nhapDaiHan(self, cucSo, gioiTinh):
        """Nhap dai han

        Args:
            cucSo (TYPE): Description
            gioiTinh (TYPE): Description

        Returns:
            TYPE: Description
        """
        for cung in self.thapNhiCung:
            khoangCach = khoangCachCung(cung.cungSo, self.cungMenh, gioiTinh)
            cung.daiHan(cucSo + khoangCach * 10)
        return self

    def nhapTieuHan(self, khoiTieuHan, gioiTinh, chiNam):
        # Vị trí khởi tiểu Hạn là của năm sinh theo chi
        # vì vậy cần phải tìm vị trí cung Tý của năm đó
        viTriCungTy1 = dichCung(khoiTieuHan, -gioiTinh * (chiNam - 1))

        # Tiếp đó là nhập hạn
        for cung in self.thapNhiCung:
            khoangCach = khoangCachCung(cung.cungSo, viTriCungTy1, gioiTinh)
            cung.tieuHan(khoangCach)
        return self

    def nhapCungThan(self):
        self.thapNhiCung[self.cungThan].anCungThan()

    def nhapSao(self, cungSo, *args):
        for sao in args:
            self.thapNhiCung[cungSo].themSao(sao)
        return self

    def nhapTuan(self, *args):
        for cung in args:
            self.thapNhiCung[cung].anTuan()
        return self

    def nhapTriet(self, *args):
        for cung in args:
            self.thapNhiCung[cung].anTriet()
        return self


def dacTinhSao(viTriDiaBan, sao):
    saoId = sao.saoID
    maTranDacTinh = {
        1: ["Tử vi", "B", "Đ", "M", "B", "V", "M", "M", "Đ", "M", "B", "V",
            "B"],
        2: ["Liêm trinh", "V", "Đ", "V", "H", "M", "H", "V", "Đ", "V", "H",
            "M", "H"],
        3: ["Thiên đồng", "V", "H", "M", "Đ", "H", "Đ", "H", "H", "M", "H",
            "H", "Đ"],
        4: ["Vũ khúc", "V", "M", "V", "Đ", "M", "H", "V", "M", "V", "Đ", "M",
            "H"],
        5: ["Thái dương", "H", "Đ", "V", "V", "V", "M", "M", "Đ", "H", "H",
            "H", "H"],
        6: ["Thiên cơ", "Đ", "Đ", "H", "M", "M", "V", "Đ", "Đ", "V", "M", "M",
            "H"],
        8: ["Thái âm", "V", "Đ", "H", "H", "H", "H", "H", "Đ", "V", "M",
            "M", "M"],
        9: ["Tham lang", "H", "M", "Đ", "H", "V", "H", "H", "M", "Đ", "H",
            "V", "H"],
        10: ["Cự môn", "V", "H", "V", "M", "H", "H", "V", "H", "Đ", "M", "H",
             "Đ"],
        11: ["Thiên tướng", "V", "Đ", "M", "H", "V", "Đ", "V", "Đ", "M", "H",
             "V", "Đ"],
        12: ["Thiên lương", "V", "Đ", "V", "V", "M", "H", "M", "Đ", "V", "H",
             "M", "H"],
        13: ["Thất sát", "M", "Đ", "M", "H", "H", "V", "M", "Đ", "M", "H",
             "H", "V"],
        14: ["Phá quân", "M", "V", "H", "H", "Đ", "H", "M", "V", "H", "H",
             "Đ", "H"],
        51: ["Đà la", "H", "Đ", "H", "H", "Đ", "H", "H", "Đ", "H", "H", "Đ",
             "H"],
        52: ["Kình dương", "H", "Đ", "H", "H", "Đ", "H", "H", "Đ", "H", "H",
             "Đ", "H"],
        55: ["Linh tinh", "H", "H", "Đ", "Đ", "Đ", "Đ", "Đ", "H", "H", "H",
             "H", "H"],
        56: ["Hỏa tinh", "H", "H", "Đ", "Đ", "Đ", "Đ", "Đ", "H", "H", "H",
             "H", "H"],
        57: ["Văn xương", "H", "Đ", "H", "Đ", "H", "Đ", "H", "Đ", "H", "H",
             "Đ", "Đ"],
        58: ["Văn khúc", "H", "Đ", "H", "Đ", "H", "Đ", "H", "Đ", "H", "H",
             "Đ", "Đ"],
        53: ["Địa không", "H", "H", "Đ", "H", "H", "Đ", "H", "H", "Đ", "H",
             "H", "Đ"],
        54: ["Địa kiếp", "H", "H", "Đ", "H", "H", "Đ", "H", "H", "Đ", "H", "H",
             "Đ"],
        95: ["Hóa kỵ", None, "Đ", None, None, "Đ", None, None, "Đ", None, None,
             "Đ", None],
        36: ["Đại hao", None, None, "Đ", "Đ", None, None, None, None, "Đ", "Đ",
             None, None],
        30: ["Tiểu Hao", None, None, "Đ", "Đ", None, None, None, None, "Đ",
             "Đ", None, None],
        69: ["Thiên khốc", "Đ", "Đ", None, "Đ", None, None, "Đ", "Đ", None,
             "Đ", None, None],
        70: ["Thiên hư", "Đ", "Đ", None, "Đ", None, None, "Đ", "Đ", None, "Đ",
             None, None],
        98: ["Thiên mã", None, None, "Đ", None, None, "Đ", None, None, None,
             None, None, None],
        73: ["Thiên Hình", None, None, "Đ", "Đ", None, None, None, None, "Đ",
             "Đ", None, None],
        74: ["Thiên riêu", None, None, "Đ", "Đ", None, None, None, None, None,
             "Đ", "Đ", None],

    }
    if sao.saoID in maTranDacTinh.keys():
        if maTranDacTinh[sao.saoID][viTriDiaBan] in ["M", "V", "Đ", "B", "H"]:
            sao.anDacTinh(maTranDacTinh[sao.saoID][viTriDiaBan])

def lapDiaBan(diaBan, nn, tt, nnnn, gioSinh, gioiTinh, nnxh, duongLich, timeZone):
    if duongLich is True:
        nn, tt, nnnn, thangNhuan = \
            ngayThangNam(nn, tt, nnnn, duongLich, timeZone)
    canThang, canNam, chiNam = \
        ngayThangNamCanChi(nn, tt, nnnn, False, timeZone)

    canNamXH, chiNamXh = namXemhan(nnxh)

    diaBan = diaBan(tt, gioSinh)

    amDuongNamSinh = thienCan[canNam]["amDuong"]
    amDuongChiNamSinh = diaChi[chiNam]["amDuong"]

    # Bản Mệnh chính là Ngũ hành nạp âm của năm sinh
    # banMenh = nguHanhNapAm(canNam, chiNam)

    hanhCuc = timCuc(diaBan.cungMenh, canNam)
    cuc = nguHanh(hanhCuc)
    cucSo = cuc['cuc']

    # Nhập đại hạn khi đã biết được số cục
    # Theo sách Số tử vi dưới góc nhìn khoa học
    # Dương Nam - Âm Nữ theo chiều thuận
    # Âm Nam - Dương Nữ theo chiều nghịch
    diaBan = diaBan.nhapDaiHan(cucSo, gioiTinh * amDuongChiNamSinh)

    # Nhập tiểu hạn
    khoiHan = dichCung(11, -3 * (chiNam - 1))
    diaBan = diaBan.nhapTieuHan(khoiHan, gioiTinh, chiNam)

    # Bắt đầu an Tử vi tinh hệ
    viTriTuVi = timTuVi(cucSo, nn)
    diaBan.nhapSao(viTriTuVi, saoTuVi)

    viTriLiemTrinh = dichCung(viTriTuVi, 4)
    diaBan.nhapSao(viTriLiemTrinh, saoLiemTrinh)

    viTriThienDong = dichCung(viTriTuVi, 7)
    diaBan.nhapSao(viTriThienDong, saoThienDong)

    viTriVuKhuc = dichCung(viTriTuVi, 8)
    diaBan.nhapSao(viTriVuKhuc, saoVuKhuc)

    vitriThaiDuong = dichCung(viTriTuVi, 9)
    diaBan.nhapSao(vitriThaiDuong, saoThaiDuong)

    viTriThienCo = dichCung(viTriTuVi, 11)
    diaBan.nhapSao(viTriThienCo, saoThienCo)

    # Thiên phủ tinh hệ
    # viTriTuVi = 4
    viTriThienPhu = dichCung(3, 3 - viTriTuVi)
    diaBan.nhapSao(viTriThienPhu, saoThienPhu)

    viTriThaiAm = dichCung(viTriThienPhu, 1)
    diaBan.nhapSao(viTriThaiAm, saoThaiAm)

    viTriThamLang = dichCung(viTriThienPhu, 2)
    diaBan.nhapSao(viTriThamLang, saoThamLang)

    viTriCuMon = dichCung(viTriThienPhu, 3)
    diaBan.nhapSao(viTriCuMon, saoCuMon)

    viTriThienTuong = dichCung(viTriThienPhu, 4)
    diaBan.nhapSao(viTriThienTuong, saoThienTuong)

    viTriThienLuong = dichCung(viTriThienPhu, 5)
    diaBan.nhapSao(viTriThienLuong, saoThienLuong)

    viTriThatSat = dichCung(viTriThienPhu, 6)
    diaBan.nhapSao(viTriThatSat, saoThatSat)

    viTriPhaQuan = dichCung(viTriThienPhu, 10)
    diaBan.nhapSao(viTriPhaQuan, saoPhaQuan)

    # Vòng Lộc tồn
    # Vị trí sao Lộc tồn ở Can của năm sinh trên địa bàn
    #  sao Bác sỹ ở cùng cung với Lộc tồn
    viTriLocTon = thienCan[canNam]['vitriDiaBan']
    diaBan.nhapSao(viTriLocTon, saoLocTon, saoBacSy)

    amDuongNamNu = gioiTinh * amDuongNamSinh
    viTriLucSi = dichCung(viTriLocTon, 1 * amDuongNamNu)
    diaBan.nhapSao(viTriLucSi, saoLucSi)

    viTriThanhLong = dichCung(viTriLocTon, 2 * amDuongNamNu)
    diaBan.nhapSao(viTriThanhLong, saoThanhLong)

    viTriTieuHao = dichCung(viTriLocTon, 3 * amDuongNamNu)
    diaBan.nhapSao(viTriTieuHao, saoTieuHao)

    viTriTuongQuan = dichCung(viTriLocTon, 4 * amDuongNamNu)
    diaBan.nhapSao(viTriTuongQuan, saoTuongQuan)

    viTriTauThu = dichCung(viTriLocTon, 5 * amDuongNamNu)
    diaBan.nhapSao(viTriTauThu, saoTauThu)

    viTriPhiLiem = dichCung(viTriLocTon, 6 * amDuongNamNu)
    diaBan.nhapSao(viTriPhiLiem, saoPhiLiem)

    viTriHyThan = dichCung(viTriLocTon, 7 * amDuongNamNu)
    diaBan.nhapSao(viTriHyThan, saoHyThan)

    viTriBenhPhu = dichCung(viTriLocTon, 8 * amDuongNamNu)
    diaBan.nhapSao(viTriBenhPhu, saoBenhPhu)

    viTriDaiHao = dichCung(viTriLocTon, 9 * amDuongNamNu)
    diaBan.nhapSao(viTriDaiHao, saoDaiHao)

    viTriPhucBinh = dichCung(viTriLocTon, 10 * amDuongNamNu)
    diaBan.nhapSao(viTriPhucBinh, saoPhucBinh)

    viTriQuanPhu2 = dichCung(viTriLocTon, 11 * amDuongNamNu)
    diaBan.nhapSao(viTriQuanPhu2, saoQuanPhu2)

    # Vòng Địa chi - Thái tuế
    viTriThaiTue = chiNam
    diaBan.nhapSao(viTriThaiTue, saoThaiTue)

    viTriThieuDuong = dichCung(viTriThaiTue, 1)
    diaBan.nhapSao(viTriThieuDuong, saoThieuDuong, saoThienKhong)

    viTriTangMon = dichCung(viTriThaiTue, 2)
    diaBan.nhapSao(viTriTangMon, saoTangMon)

    viTriThieuAm = dichCung(viTriThaiTue, 3)
    diaBan.nhapSao(viTriThieuAm, saoThieuAm)

    viTriQuanPhu3 = dichCung(viTriThaiTue, 4)
    diaBan.nhapSao(viTriQuanPhu3, saoQuanPhu3)

    viTriTuPhu = dichCung(viTriThaiTue, 5)
    diaBan.nhapSao(viTriTuPhu, saoTuPhu, saoNguyetDuc)

    viTriTuePha = dichCung(viTriThaiTue, 6)
    diaBan.nhapSao(viTriTuePha, saoTuePha)

    viTriLongDuc = dichCung(viTriThaiTue, 7)
    diaBan.nhapSao(viTriLongDuc, saoLongDuc)

    viTriBachHo = dichCung(viTriThaiTue, 8)
    diaBan.nhapSao(viTriBachHo, saoBachHo)

    viTriPhucDuc = dichCung(viTriThaiTue, 9)
    diaBan.nhapSao(viTriPhucDuc, saoPhucDuc, saoThienDuc)

    viTriDieuKhach = dichCung(viTriThaiTue, 10)
    diaBan.nhapSao(viTriDieuKhach, saoDieuKhach)

    viTriTrucPhu = dichCung(viTriThaiTue, 11)
    diaBan.nhapSao(viTriTrucPhu, saoTrucPhu)

    #  Vòng ngũ hành cục Tràng sinh
    # !!! Đã sửa !!! *LƯU Ý Phần này đã sửa* Theo cụ Thiên Lương: Nam -> Thuận,
    # Nữ -> Nghịch (Không phù hợp)
    # **ISSUE 2**: Dương nam, Âm nữ theo chiều thuận, Âm nam Dương nữ theo
    # chiều nghịch

    viTriTrangSinh = timTrangSinh(cucSo)
    diaBan.nhapSao(viTriTrangSinh, saoTrangSinh)

    viTriMocDuc = dichCung(viTriTrangSinh, amDuongNamNu * 1)
    diaBan.nhapSao(viTriMocDuc, saoMocDuc)

    viTriQuanDoi = dichCung(viTriTrangSinh, amDuongNamNu * 2)
    diaBan.nhapSao(viTriQuanDoi, saoQuanDoi)

    viTriLamQuan = dichCung(viTriTrangSinh, amDuongNamNu * 3)
    diaBan.nhapSao(viTriLamQuan, saoLamQuan)

    viTriDeVuong = dichCung(viTriTrangSinh, amDuongNamNu * 4)
    diaBan.nhapSao(viTriDeVuong, saoDeVuong)

    viTriSuy = dichCung(viTriTrangSinh, amDuongNamNu * 5)
    diaBan.nhapSao(viTriSuy, saoSuy)

    viTriBenh = dichCung(viTriTrangSinh, amDuongNamNu * 6)
    diaBan.nhapSao(viTriBenh, saoBenh)

    viTriTu = dichCung(viTriTrangSinh, amDuongNamNu * 7)
    diaBan.nhapSao(viTriTu, saoTu)

    viTriMo = dichCung(viTriTrangSinh, amDuongNamNu * 8)
    diaBan.nhapSao(viTriMo, saoMo)

    viTriTuyet = dichCung(viTriTrangSinh, amDuongNamNu * 9)
    diaBan.nhapSao(viTriTuyet, saoTuyet)

    viTriThai = dichCung(viTriTrangSinh, amDuongNamNu * (-1))
    diaBan.nhapSao(viTriThai, saoThai)

    viTriDuong = dichCung(viTriTrangSinh, amDuongNamNu * (-2))
    diaBan.nhapSao(viTriDuong, saoDuong)

    # An sao đôi
    #    Kình dương - Đà la
    viTriDaLa = dichCung(viTriLocTon, -1)
    diaBan.nhapSao(viTriDaLa, saoDaLa)

    viTriKinhDuong = dichCung(viTriLocTon, 1)
    diaBan.nhapSao(viTriKinhDuong, saoKinhDuong)

    #  Không - Kiếp
    # Khởi giờ Tý ở cung Hợi, đếm thuận đến giờ sinh được cung Địa kiếp
    viTriDiaKiep = dichCung(11, gioSinh)
    diaBan.nhapSao(viTriDiaKiep, saoDiaKiep)

    viTriDiaKhong = dichCung(12, 12 - viTriDiaKiep)
    diaBan.nhapSao(viTriDiaKhong, saoDiaKhong)

    viTriHoaTinh, viTriLinhTinh = timHoaLinh(chiNam, gioSinh,
                                             gioiTinh, amDuongNamSinh)
    diaBan.nhapSao(viTriHoaTinh, saoHoaTinh)
    diaBan.nhapSao(viTriLinhTinh, saoLinhTinh)

    viTriLongTri = dichCung(5, chiNam - 1)
    diaBan.nhapSao(viTriLongTri, saoLongTri)

    viTriPhuongCac = dichCung(2, 2 - viTriLongTri)
    diaBan.nhapSao(viTriPhuongCac, saoPhuongCac, saoGiaiThan)

    viTriTaPhu = dichCung(5, tt - 1)
    diaBan.nhapSao(viTriTaPhu, saoTaPhu)

    viTriHuuBat = dichCung(2, 2 - viTriTaPhu)
    diaBan.nhapSao(viTriHuuBat, saoHuuBat)

    viTriVanKhuc = dichCung(5, gioSinh - 1)
    diaBan.nhapSao(viTriVanKhuc, saoVanKhuc)

    viTriVanXuong = dichCung(2, 2 - viTriVanKhuc)
    diaBan.nhapSao(viTriVanXuong, saoVanXuong)

    viTriTamThai = dichCung(5, tt + nn - 2)
    diaBan.nhapSao(viTriTamThai, saoTamThai)

    viTriBatToa = dichCung(2, 2 - viTriTamThai)
    diaBan.nhapSao(viTriBatToa, saoBatToa)

    # ! Vị trí sao Ân Quang - Thiên Quý
    # ! Lấy cung thìn làm mồng 1 đếm thuận đến ngày sinh,
    # ! lui lại một cung để lấy đó làm giờ tý đếm thuận đến giờ sinh là
    #  Ân Quang
    # ! Thiên Quý đối với Ân Quang qua trục Sửu Mùi
    # @ viTriAnQuang = dichCung(5, nn + gioSinh - 3)
    # @ viTriThienQuy = dichCung(2, 2 - viTriAnQuang)
    # Phía trên là cách an Quang-Quý theo cụ Vu Thiên
    # Sau khi tìm hiểu thì Quang-Quý sẽ được an theo Xương-Khúc như sau:
    # Ân Quang − Xem Văn Xương ở cung nào, kể cung ấy là mồng một
    # bắt đầu đếm thoe chiều thuận đến ngày sinh, lùi lại một cung,
    # an Ân Quang.
    # Thiên Quý − Xem Văn Khúc ở cung nào, kể cung ấy là mồng một,
    # !!! bắt đầu đếm theo chiều nghịch đến ngày sinh, lùi lại một cung,
    # an Thiên Quý.!!!
    # ??? Thiên Quý ở đối cung của Ân Quang qua trục Sửu Mùi mới chính xác???

    viTriAnQuang = dichCung(viTriVanXuong, nn - 2)
    diaBan.nhapSao(viTriAnQuang, saoAnQuang)

    viTriThienQuy = dichCung(2, 2 - viTriAnQuang)
    diaBan.nhapSao(viTriThienQuy, saoThienQuy)

    viTriThienKhoi = timThienKhoi(canNam)
    diaBan.nhapSao(viTriThienKhoi, saoThienKhoi)

    viTriThienViet = dichCung(5, 5 - viTriThienKhoi)
    diaBan.nhapSao(viTriThienViet, saoThienViet)

    viTriThienHu = dichCung(7, chiNam - 1)
    diaBan.nhapSao(viTriThienHu, saoThienHu)

    viTriThienKhoc = dichCung(7, -chiNam + 1)
    diaBan.nhapSao(viTriThienKhoc, saoThienKhoc)

    viTriThienTai = dichCung(diaBan.cungMenh, chiNam - 1)
    diaBan.nhapSao(viTriThienTai, saoThienTai)

    viTriThienTho = dichCung(diaBan.cungThan, chiNam - 1)
    diaBan.nhapSao(viTriThienTho, saoThienTho)

    viTriHongLoan = dichCung(4, -chiNam + 1)
    diaBan.nhapSao(viTriHongLoan, saoHongLoan)

    viTriThienHy = dichCung(viTriHongLoan, 6)
    diaBan.nhapSao(viTriThienHy, saoThienHy)

    #  Thiên Quan - Thiên Phúc
    viTriThienQuan, viTriThienPhuc = timThienQuanThienPhuc(canNam)
    diaBan.nhapSao(viTriThienQuan, saoThienQuan)
    diaBan.nhapSao(viTriThienPhuc, saoThienPhuc)

    viTriThienHinh = dichCung(10, tt - 1)
    diaBan.nhapSao(viTriThienHinh, saoThienHinh)

    viTriThienRieu = dichCung(viTriThienHinh, 4)
    diaBan.nhapSao(viTriThienRieu, saoThienRieu, saoThienY)

    viTriCoThan = timCoThan(chiNam)
    diaBan.nhapSao(viTriCoThan, saoCoThan)

    viTriQuaTu = dichCung(viTriCoThan, -4)
    diaBan.nhapSao(viTriQuaTu, saoQuaTu)

    viTriVanTinh = dichCung(viTriKinhDuong, 2)
    diaBan.nhapSao(viTriVanTinh, saoVanTinh)

    viTriDuongPhu = dichCung(viTriVanTinh, 2)
    diaBan.nhapSao(viTriDuongPhu, saoDuongPhu)

    viTriQuocAn = dichCung(viTriDuongPhu, 3)
    diaBan.nhapSao(viTriQuocAn, saoQuocAn)

    # Thai phụ - Phong Cáo
    viTriThaiPhu = dichCung(viTriVanKhuc, 2)
    diaBan.nhapSao(viTriThaiPhu, saoThaiPhu)

    viTriPhongCao = dichCung(viTriVanKhuc, -2)
    diaBan.nhapSao(viTriPhongCao, saoPhongCao)

    # Thiên giải - Địa giải
    #    Theo cụ Thiên Lương: Lấy cung Thân làm tháng Giêng, đếm thuận nhưng
    #    nhảy cung là Thiên giải. Một số trang web đếm nhưng không nhảy cung???
    #    Liệu phương cách nào đúng?
    viTriThienGiai = dichCung(9, (2 * tt) - 2)
    diaBan.nhapSao(viTriThienGiai, saoThienGiai)

    viTriDiaGiai = dichCung(viTriTaPhu, 3)
    diaBan.nhapSao(viTriDiaGiai, saoDiaGiai)

    # Thiên la - Địa võng, Thiên thương - Thiên sứ
    viTriThienLa = 5
    diaBan.nhapSao(viTriThienLa, saoThienLa)

    viTriDiaVong = 11
    diaBan.nhapSao(viTriDiaVong, saoDiaVong)

    viTriThienThuong = diaBan.cungNoboc
    diaBan.nhapSao(viTriThienThuong, saoThienThuong)

    viTriThienSu = diaBan.cungTatAch
    diaBan.nhapSao(viTriThienSu, saoThienSu)

    # Vòng Thiên mã
    viTriThienMa = timThienMa(chiNam)
    diaBan.nhapSao(viTriThienMa, saoThienMa)

    viTriHoaCai = dichCung(viTriThienMa, 2)
    diaBan.nhapSao(viTriHoaCai, saoHoaCai)

    viTriKiepSat = dichCung(viTriThienMa, 3)
    diaBan.nhapSao(viTriKiepSat, saoKiepSat)

    viTriDaoHoa = dichCung(viTriKiepSat, 4)
    diaBan.nhapSao(viTriDaoHoa, saoDaoHoa)

    # Phá toái
    viTriPhaToai = timPhaToai(chiNam)
    diaBan.nhapSao(viTriPhaToai, saoPhaToai)

    # Đẩu quân
    viTriDauQuan = dichCung(chiNam, -tt + gioSinh)
    diaBan.nhapSao(viTriDauQuan, saoDauQuan)

    #  Tứ Hóa
    # An theo 10 câu của cụ Thiên Lương trong cuốn
    # Số tử vi dưới mắt khoa học

    if canNam == 1:
        viTriHoaLoc = viTriLiemTrinh
        viTriHoaQuyen = viTriPhaQuan
        viTriHoaKhoa = viTriVuKhuc
        viTriHoaKy = vitriThaiDuong
    elif canNam == 2:
        viTriHoaLoc = viTriThienCo
        viTriHoaQuyen = viTriThienLuong
        viTriHoaKhoa = viTriTuVi
        viTriHoaKy = viTriThaiAm
    elif canNam == 3:
        viTriHoaLoc = viTriThienDong
        viTriHoaQuyen = viTriThienCo
        viTriHoaKhoa = viTriVanXuong
        viTriHoaKy = viTriLiemTrinh
    elif canNam == 4:
        viTriHoaLoc = viTriThaiAm
        viTriHoaQuyen = viTriThienDong
        viTriHoaKhoa = viTriThienCo
        viTriHoaKy = viTriCuMon
    elif canNam == 5:
        viTriHoaLoc = viTriThamLang
        viTriHoaQuyen = viTriThaiAm
        viTriHoaKhoa = viTriHuuBat
        viTriHoaKy = viTriThienCo
    elif canNam == 6:
        viTriHoaLoc = viTriVuKhuc
        viTriHoaQuyen = viTriThamLang
        viTriHoaKhoa = viTriThienLuong
        viTriHoaKy = viTriVanKhuc
    elif canNam == 7:
        viTriHoaLoc = vitriThaiDuong
        viTriHoaQuyen = viTriVuKhuc
        viTriHoaKhoa = viTriThienDong
        viTriHoaKy = viTriThaiAm
    elif canNam == 8:
        viTriHoaLoc = viTriCuMon
        viTriHoaQuyen = vitriThaiDuong
        viTriHoaKhoa = viTriVanKhuc
        viTriHoaKy = viTriVanXuong
    elif canNam == 9:
        viTriHoaLoc = viTriThienLuong
        viTriHoaQuyen = viTriTuVi
        viTriHoaKhoa = viTriThienPhu
        viTriHoaKy = viTriVuKhuc
    elif canNam == 10:
        viTriHoaLoc = viTriPhaQuan
        viTriHoaQuyen = viTriCuMon
        viTriHoaKhoa = viTriThaiAm
        viTriHoaKy = viTriThamLang

    diaBan.nhapSao(viTriHoaLoc, saoHoaLoc)
    diaBan.nhapSao(viTriHoaQuyen, saoHoaQuyen)
    diaBan.nhapSao(viTriHoaKhoa, saoHoaKhoa)
    diaBan.nhapSao(viTriHoaKy, saoHoaKy)

    #  An Lưu Hà - Thiên Trù
    # Sách cụ Thiên Lương không đề cập đến 2 sao này
    # Mong mọi người kiểm chứng
    viTriLuuHa, viTriThienTru = timLuuTru(canNam)
    diaBan.nhapSao(viTriLuuHa, saoLuuHa)
    diaBan.nhapSao(viTriThienTru, saoThienTru)

    # An Tuần, Triệt
    ketThucTuan = dichCung(chiNam, 10 - canNam)
    viTriTuan1 = dichCung(ketThucTuan, 1)
    viTriTuan2 = dichCung(viTriTuan1, 1)
    diaBan.nhapTuan(viTriTuan1, viTriTuan2)

    viTriTriet1, viTriTriet2 = timTriet(canNam)
    diaBan.nhapTriet(viTriTriet1, viTriTriet2)

    # An sao lưu theo năm
    viTriLThaiTue = chiNamXh
    diaBan.nhapSao(viTriLThaiTue, saoLThaiTue)

    viTriLTangMon = dichCung(viTriLThaiTue, 2)
    diaBan.nhapSao(viTriLTangMon, saoLTangMon)

    viTriLBachHo = dichCung(viTriLTangMon, 6)
    diaBan.nhapSao(viTriLBachHo, saoLBachHo)

    viTriLThienHu = dichCung(7, chiNamXh - 1)
    diaBan.nhapSao(viTriLThienHu, saoLThienHu)

    viTriLThienKhoc = dichCung(7, -chiNamXh + 1)
    diaBan.nhapSao(viTriLThienKhoc, saoLThienKhoc)

    viTriLThienMa = timThienMa(chiNamXh)
    diaBan.nhapSao(viTriLThienMa, saoLThienMa)

    viTriLLocTon = timLLocTon(chiNamXh)
    diaBan.nhapSao(viTriLLocTon, saoLLocTon)

    viTriLKinhDuong = dichCung(viTriLLocTon, 1)
    diaBan.nhapSao(viTriLKinhDuong, saoLKinhDuong)

    viTriLDaLa = dichCung(viTriLLocTon, -1)
    diaBan.nhapSao(viTriLDaLa, saoLDaLa)

    viTriLBacSi = viTriLLocTon
    diaBan.nhapSao(viTriLBacSi, saoLBacSi)

    viTriLThienKhong = dichCung(viTriLThaiTue, 1)
    diaBan.nhapSao(viTriLThienKhong, saoLThienKhong)

    viTriLQuanSach = dichCung(viTriLThaiTue, -1)
    diaBan.nhapSao(viTriLQuanSach, saoLQuanSach)

    viTriLThienKhoi = timThienKhoi(canNamXH)
    diaBan.nhapSao(viTriLThienKhoi, saoLThienKhoi)

    viTriLThienViet = dichCung(5, 5 - viTriLThienKhoi)
    diaBan.nhapSao(viTriLThienViet, saoLThienViet) 

    #Lưu vòng tràng sinh
    viTriLTrangSinh = timLTrangSinh(canNamXH)
    diaBan.nhapSao(viTriLTrangSinh, saoLTrangSinh)

    viTriLMocDuc = dichCung(viTriLTrangSinh, amDuongNamXH(canNamXH) * 1)
    diaBan.nhapSao(viTriLMocDuc, saoLMocDuc)

    viTriLQuanDoi = dichCung(viTriLTrangSinh, amDuongNamXH(canNamXH) * 2)
    diaBan.nhapSao(viTriLQuanDoi, saoLQuanDoi)

    viTriLLamQuan = dichCung(viTriLTrangSinh, amDuongNamXH(canNamXH) * 3)
    diaBan.nhapSao(viTriLLamQuan, saoLLamQuan)

    viTriLDeVuong = dichCung(viTriLTrangSinh, amDuongNamXH(canNamXH) * 4)
    diaBan.nhapSao(viTriLDeVuong, saoLDeVuong)

    viTriLSuy = dichCung(viTriLTrangSinh, amDuongNamXH(canNamXH) * 5)
    diaBan.nhapSao(viTriLSuy, saoLSuy)

    viTriLBenh = dichCung(viTriLTrangSinh, amDuongNamXH(canNamXH) * 6)
    diaBan.nhapSao(viTriLBenh, saoLBenh)

    viTriLTu = dichCung(viTriLTrangSinh, amDuongNamXH(canNamXH) * 7)
    diaBan.nhapSao(viTriLTu, saoLTu)

    viTriLMo = dichCung(viTriLTrangSinh, amDuongNamXH(canNamXH) * 8)
    diaBan.nhapSao(viTriLMo, saoLMo)

    viTriLTuyet = dichCung(viTriLTrangSinh, amDuongNamXH(canNamXH) * 9)
    diaBan.nhapSao(viTriLTuyet, saoLTuyet)

    viTriLThai = dichCung(viTriLTrangSinh, amDuongNamXH(canNamXH) * (-1))
    diaBan.nhapSao(viTriLThai, saoLThai)

    viTriLDuong = dichCung(viTriLTrangSinh, amDuongNamXH(canNamXH) * (-2))
    diaBan.nhapSao(viTriLDuong, saoLDuong)

    return (diaBan)