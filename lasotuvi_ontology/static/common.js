function dichCung(cungBanDau, soCungDich) {
    var cungSauKhiDich = Math.floor(cungBanDau);
    cungSauKhiDich += Math.floor(soCungDich);
    if (cungSauKhiDich % 12 == 0) {
        return 12;
    }
    else {
        return cungSauKhiDich % 12;
    }
}

function CungXungChieu(cungId){
    $("[cung-id]").removeClass("xungChieu");
    cungXungChieu = dichCung(cungId, 6);
    cungTamHop1 = dichCung(cungId, 4);
    cungTamHop2 = dichCung(cungId, 8);
    $("[cung-id=" + cungId + "]").addClass("xungChieu");
    $("[cung-id=" + cungXungChieu + "]").addClass("xungChieu");
    $("[cung-id=" + cungTamHop1 + "]").addClass("xungChieu");
    $("[cung-id=" + cungTamHop2 + "]").addClass("xungChieu");
}