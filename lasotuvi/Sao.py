from lasotuvi.AmDuong import nguHanh


class Sao(object):
    def __init__(self, saoID, saoTen, saoNguHanh, saoLoai=2, saoPhuongVi="",
                 saoAmDuong="", vongTrangSinh=0):
        super(Sao, self).__init__()
        self.saoID = saoID
        self.saoTen = saoTen
        self.saoNguHanh = saoNguHanh
        self.saoLoai = saoLoai
        self.saoPhuongVi = saoPhuongVi
        self.saoAmDuong = saoAmDuong
        self.vongTrangSinh = vongTrangSinh
        self.cssSao = nguHanh(saoNguHanh)['css']
        self.saoDacTinh = None

    def anDacTinh(self, dacTinh):
        dt = {
            "V": "vuongDia",
            "M": "mieuDia",
            "Đ": "dacDia",
            "B": "binhHoa",
            "H": "hamDia",
        }
        self.saoDacTinh = dacTinh
        # self.saoTen += " (%s)" % dacTinh
        # self.cssSao = dt[dacTinh]
        return self

    def anCung(self, saoViTriCung):
        self.saoViTriCung = saoViTriCung
        return self


# Tử vi tinh hệ
saoTuVi = Sao(1, u"Tử vi", "O", 1, u"Đế tinh", 1, 0)
saoLiemTrinh = Sao(2, u"Liêm trinh", "H", 1, u"Bắc đẩu tinh", 1, 0)
saoThienDong = Sao(3, "Thiên đồng", "T", 1, "Bắc đẩu tinh", 1, 0)
saoVuKhuc = Sao(4, "Vũ khúc", "K", 1, "Bắc đẩu tinh", -1, 0)
saoThaiDuong = Sao(5, "Thái Dương", "H", 1, "Nam đẩu tinh", 1, 0)
saoThienCo = Sao(6, "Thiên cơ", "M", 1, "Nam đẩu tinh", -1, 0)

# Thiên phủ tinh hệ
saoThienPhu = Sao(7, "Thiên phủ", "O", 1, "Nam đẩu tinh", 1, 0)
saoThaiAm = Sao(8, "Thái âm", "T", 1, "Bắc đẩu tinh", -1, 0)
saoThamLang = Sao(9, "Tham lang", "T", 1, "Bắc đẩu tinh", -1, 0)
saoCuMon = Sao(10, "Cự môn", "T", 1, "Bắc đẩu tinh", -1, 0)
saoThienTuong = Sao(11, "Thiên tướng", "T", 1, "Nam đẩu tinh", 1, 0)
saoThienLuong = Sao(12, "Thiên lương", "M", 1, "Nam đẩu tinh", -1, 0)
saoThatSat = Sao(13, "Thất sát", "K", 1, "Nam đẩu tinh", 1, 0)
saoPhaQuan = Sao(14, "Phá quân", "T", 1, "Bắc đẩu tinh", -1, 0)

# Vòng Địa chi - Thái tuế
saoThaiTue = Sao(15, "Thái tuế", "H", 15, "", 0)
saoThieuDuong = Sao(16, "Thiếu dương", "H", 5)
saoTangMon = Sao(17, "Tang môn", "M", 12)
saoThieuAm = Sao(18, "Thiếu âm", "T", 5)
saoQuanPhu3 = Sao(19, "Quan phù", "H", 12)
saoTuPhu = Sao(20, "Tử phù", "K", 12)
saoTuePha = Sao(21, "Tuế phá", "H", 12)
saoLongDuc = Sao(22, "Long đức", "T", 5)
saoBachHo = Sao(23, "Bạch hổ", "K", 12)
saoPhucDuc = Sao(24, "Phúc đức", "O", 5)
saoDieuKhach = Sao(25, "Điếu khách", "H", 12)
saoTrucPhu = Sao(26, "Trực phù", "K", 16)

#  Vòng Thiên can - Lộc tồn
saoLocTon = Sao(27, "Lộc tồn", "O", 3, "Bắc đẩu tinh")
saoBacSy = Sao(109, "Bác sỹ", "T", 5, )
saoLucSi = Sao(28, "Lực sĩ", "H", 2)
saoThanhLong = Sao(29, "Thanh long", "T", 5)
saoTieuHao = Sao(30, "Tiểu hao", "H", 12)
saoTuongQuan = Sao(31, "Tướng quân", "M", 4)
saoTauThu = Sao(32, "Tấu thư", "K", 3)
saoPhiLiem = Sao(33, "Phi liêm", "H", 2)
saoHyThan = Sao(34, "Hỷ thần", "H", 5)
saoBenhPhu = Sao(35, "Bệnh phù", "O", 12)
saoDaiHao = Sao(36, "Đại hao", "H", 12)
saoPhucBinh = Sao(37, "Phục binh", "H", 13)
saoQuanPhu2 = Sao(38, "Quan phù", "H", 12)

# Vòng Tràng sinh
saoTrangSinh = Sao(39, "Sinh", "T", 5, vongTrangSinh=1)
saoMocDuc = Sao(40, "Dục", "T", 14, vongTrangSinh=1)
saoQuanDoi = Sao(41, "Đới", "K", 4, vongTrangSinh=1)
saoLamQuan = Sao(42, "Lâm", "K", 7, vongTrangSinh=1)
saoDeVuong = Sao(43, "Vượng", "K", 5, vongTrangSinh=1)
saoSuy = Sao(44, "Suy", "T", 12, vongTrangSinh=1)
saoBenh = Sao(45, "Bệnh", "H", 12, vongTrangSinh=1)
saoTu = Sao(46, "Tử", "H", 12, vongTrangSinh=1)
saoMo = Sao(47, "Mộ", "O", vongTrangSinh=1)
saoTuyet = Sao(48, "Tuyệt", "O", 12, vongTrangSinh=1)
saoThai = Sao(49, "Thai", "O", 14, vongTrangSinh=1)
saoDuong = Sao(50, "Dưỡng", "M", 2, vongTrangSinh=1)

# Lục sát
#    Kình dương đà la
saoDaLa = Sao(51, "Đà la", "K", 11)
saoKinhDuong = Sao(52, "Kình dương", "K", 11)

#    Địa không - Địa kiếp
saoDiaKhong = Sao(53, "Địa không", "H", 11)
saoDiaKiep = Sao(54, "Địa kiếp", "H", 11)

#    Hỏa tinh - Linh tinh
saoLinhTinh = Sao(55, "Linh tinh", "H", 11)
saoHoaTinh = Sao(56, "Hỏa tinh", "H", 11)

# Sao Âm Dương
#    Văn xương - Văn khúc
saoVanXuong = Sao(57, "Văn xương", "K", 6)
saoVanKhuc = Sao(58, "Văn Khúc", "T", 6)

#    Thiên khôi - Thiên Việt
saoThienKhoi = Sao(59, "Thiên khôi", "H", 6)
saoThienViet = Sao(60, "Thiên việt", "H", 6)

#    Tả phù - Hữu bật
saoTaPhu = Sao(61, "Tả phù", "O", 2)
saoHuuBat = Sao(62, "Hữu bật", "O", 2)

#    Long trì - Phượng các
saoLongTri = Sao(63, "Long trì", "T", 3)
saoPhuongCac = Sao(64, "Phượng các", "O", 3)

#    Tam thai - Bát tọa
saoTamThai = Sao(65, "Tam thai", "M", 7)
saoBatToa = Sao(66, "Bát tọa", "T", 7)

#    Ân quang - Thiên quý
saoAnQuang = Sao(67, "Ân quang", "M", 3)
saoThienQuy = Sao(68, "Thiên quý", "O", 3)

# Sao đôi khác
saoThienKhoc = Sao(69, "Thiên khốc", "T", 12)
saoThienHu = Sao(70, "Thiên hư", "T", 12)
saoThienDuc = Sao(71, "Thiên đức", "H", 5)
saoNguyetDuc = Sao(72, "Nguyệt đức", "H", 5)
saoThienHinh = Sao(73, "Thiên hình", "H", 15)
saoThienRieu = Sao(74, "Thiên riêu", "T", 13)
saoThienY = Sao(75, "Thiên y", "T", 5)
saoQuocAn = Sao(76, "Quốc ấn", "O", 6)
saoDuongPhu = Sao(77, "Đường phù", "M", 4)
saoDaoHoa = Sao(78, "Đào hoa", "M", 8)
saoHongLoan = Sao(79, "Hồng loan", "T", 8)
saoThienHy = Sao(80, "Thiên hỷ", "T", 5)
saoThienGiai = Sao(81, "Thiên giải", "H", 5)
saoDiaGiai = Sao(82, "Địa giải", "O", 5)
saoGiaiThan = Sao(83, "Giải thần", "M", 5)
saoThaiPhu = Sao(84, "Thai phụ", "K", 6)
saoPhongCao = Sao(85, "Phong cáo", "O", 4)
saoThienTai = Sao(86, "Thiên tài", "O", 2)
saoThienTho = Sao(87, "Thiên thọ", "O", 5)
saoThienThuong = Sao(88, "Thiên thương", "O", 12)
saoThienSu = Sao(89, "Thiên sứ", "T", 12)
saoThienLa = Sao(90, "Thiên la", "O", 12)
saoDiaVong = Sao(91, "Địa võng", "O", 12)
saoHoaKhoa = Sao(92, "Hóa khoa", "T", 5)
saoHoaQuyen = Sao(93, "Hóa quyền", "T", 4)
saoHoaLoc = Sao(94, "Hóa lộc", "M", 3)
saoHoaKy = Sao(95, "Hóa kỵ", "T", 13)
saoCoThan = Sao(96, "Cô thần", "O", 13)
saoQuaTu = Sao(97, "Quả tú", "O", 13)
saoThienMa = Sao(98, "Thiên mã", "H", 3)
saoPhaToai = Sao(99, "Phá toái", "H", 12)
saoThienQuan = Sao(100, "Thiên quan", "H", 5)
saoThienPhuc = Sao(101, "Thiên phúc", "H", 5)
saoLuuHa = Sao(102, "Lưu hà", "T", 12)
saoThienTru = Sao(103, "Thiên trù", "O", 5)
saoKiepSat = Sao(104, "Kiếp sát", "H", 11)
saoHoaCai = Sao(105, "Hoa cái", "K", 14)
saoVanTinh = Sao(106, "Văn tinh", "H", 6)
saoDauQuan = Sao(107, "Đẩu quân", "H", 5)
saoThienKhong = Sao(108, "Thiên không", "T", 11)
saoThienTruong = Sao(136, "Thiên trượng", "M")
saoThienDi = Sao(137, "Thiên dị", "O")
#saoThienNhan = Sao(138, "Thiên nhẫn")
#saoMaoDau = Sao(139, "Mao đầu")
saothienKho = Sao(140, "Thiên khố", "O")
saoThienLoc = Sao(141, "Thiên lộc", "T")
saoThienAn = Sao(142, "Thiên ấn", "O")

# Sao lưu
saoLThaiTue = Sao(110, "L.Thái tuế", "H", 15)
saoLTangMon = Sao(111, "L.Tang môn", "M", 12)
saoLBachHo = Sao(112, "L.Bạch hổ", "K", 12)
saoLThienHu = Sao(113, "L.Thiên hư", "T", 12)
saoLThienKhoc = Sao(114, "L.Thiên khốc", "T", 12)
saoLThienMa = Sao(115, "L.Thiên mã", "H", 3)
saoLLocTon = Sao(116, "L.Lộc tồn", "O", 3, "Bắc đẩu tinh")
saoLKinhDuong = Sao(117, "L.Kình dương", "K", 11)
saoLDaLa = Sao(118, "L.Đà la", "K", 11)

saoLBacSi = Sao(119, "L.Bác sĩ", "T", 5)
saoLThienKhong = Sao(120, "L.Thiên không", "T", 11)
saoLQuanSach = Sao(121, "L.Quán sách", "H", 12)
saoLThienKhoi = Sao(122, "L.Thiên khôi", "H", 6)
saoLThienViet = Sao(123, "L.Thiên việt", "H", 6)

# Lưu Vòng Tràng sinh
saoLTrangSinh = Sao(124, "L.Sinh", "T", 5, vongTrangSinh=1)
saoLMocDuc = Sao(125, "L.Dục", "T", 14, vongTrangSinh=1)
saoLQuanDoi = Sao(126, "L.Đới", "K", 4, vongTrangSinh=1)
saoLLamQuan = Sao(127, "L.Lâm", "K", 7, vongTrangSinh=1)
saoLDeVuong = Sao(128, "L.Vượng", "K", 5, vongTrangSinh=1)
saoLSuy = Sao(129, "L.Suy", "T", 12, vongTrangSinh=1)
saoLBenh = Sao(130, "L.Bệnh", "H", 12, vongTrangSinh=1)
saoLTu = Sao(131, "L.Tử", "H", 12, vongTrangSinh=1)
saoLMo = Sao(132, "L.Mộ", "O", vongTrangSinh=1)
saoLTuyet = Sao(133, "L.Tuyệt", "O", 12, vongTrangSinh=1)
saoLThai = Sao(134, "L.Thai", "O", 14, vongTrangSinh=1)
saoLDuong = Sao(135, "L.Dưỡng", "M", 2, vongTrangSinh=1)

